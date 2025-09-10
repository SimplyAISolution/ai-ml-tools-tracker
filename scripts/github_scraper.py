"""GitHub scraper for trending AI/ML repositories."""

import os
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any

import click
import requests
from github import Github
from tqdm import tqdm

from .utils import (
    get_project_root,
    ensure_data_directories,
    load_json_file,
    save_json_file,
    print_success,
    print_error,
    print_info,
    print_warning,
    update_metadata,
    validate_repo_data,
    get_current_timestamp,
)


class GitHubScraper:
    """Scraper for GitHub trending AI/ML repositories."""

    def __init__(self, github_token: Optional[str] = None):
        """Initialize the GitHub scraper."""
        self.github_token = github_token or os.getenv("GITHUB_TOKEN")
        self.github = Github(self.github_token) if self.github_token else Github()
        self.ai_ml_keywords = [
            "artificial-intelligence",
            "machine-learning",
            "deep-learning",
            "neural-networks",
            "computer-vision",
            "natural-language-processing",
            "nlp",
            "ai",
            "ml",
            "tensorflow",
            "pytorch",
            "keras",
            "scikit-learn",
            "opencv",
            "transformers",
            "huggingface",
            "llm",
            "gpt",
            "bert",
            "stable-diffusion",
            "langchain",
            "prompt-engineering",
            "rag",
        ]

    def search_trending_repos(
        self, days_back: int = 7, max_repos: int = 100
    ) -> List[Dict[str, Any]]:
        """Search for trending AI/ML repositories."""
        print_info(f"Searching for trending AI/ML repositories (last {days_back} days)")

        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_back)
        date_filter = f"created:>={start_date.strftime('%Y-%m-%d')}"

        trending_repos = []

        # Search with different keyword combinations
        search_queries = [
            f"machine learning {date_filter} stars:>10",
            f"artificial intelligence {date_filter} stars:>10",
            f"deep learning {date_filter} stars:>10",
            f"tensorflow {date_filter} stars:>5",
            f"pytorch {date_filter} stars:>5",
            f"llm {date_filter} stars:>5",
            f"langchain {date_filter} stars:>5",
            f"stable diffusion {date_filter} stars:>5",
            f"transformers {date_filter} stars:>5",
        ]

        for query in tqdm(search_queries, desc="Searching repositories"):
            try:
                repos = self.github.search_repositories(query=query, sort="stars", order="desc")

                # Process first 20 repos from each query
                for repo in repos[:20]:
                    if len(trending_repos) >= max_repos:
                        break

                    repo_data = self._extract_repo_data(repo)
                    if repo_data and repo_data["full_name"] not in [
                        r["full_name"] for r in trending_repos
                    ]:
                        trending_repos.append(repo_data)

                # Rate limiting
                time.sleep(2)

            except Exception as e:
                print_error(f"Error searching with query '{query}': {e}")
                continue

        print_success(f"Found {len(trending_repos)} trending AI/ML repositories")
        return trending_repos[:max_repos]

    def _extract_repo_data(self, repo) -> Optional[Dict[str, Any]]:
        """Extract relevant data from a repository object."""
        try:
            # Check if repository is AI/ML related
            if not self._is_ai_ml_repo(repo):
                return None

            repo_data = {
                "name": repo.name,
                "full_name": repo.full_name,
                "description": repo.description or "",
                "html_url": repo.html_url,
                "clone_url": repo.clone_url,
                "stars": repo.stargazers_count,
                "forks": repo.forks_count,
                "language": repo.language,
                "topics": repo.get_topics(),
                "created_at": repo.created_at.isoformat() if repo.created_at else None,
                "updated_at": repo.updated_at.isoformat() if repo.updated_at else None,
                "pushed_at": repo.pushed_at.isoformat() if repo.pushed_at else None,
                "size": repo.size,
                "open_issues": repo.open_issues_count,
                "license": repo.license.name if repo.license else None,
                "default_branch": repo.default_branch,
                "archived": repo.archived,
                "disabled": repo.disabled,
                "private": repo.private,
                "owner": {
                    "login": repo.owner.login,
                    "type": repo.owner.type,
                    "html_url": repo.owner.html_url,
                },
                "collected_at": get_current_timestamp(),
            }

            # Add README content if available
            try:
                readme = repo.get_readme()
                repo_data["readme_url"] = readme.download_url
            except:
                repo_data["readme_url"] = None

            return repo_data

        except Exception as e:
            print_warning(f"Error extracting data for repo {repo.full_name}: {e}")
            return None

    def _is_ai_ml_repo(self, repo) -> bool:
        """Check if repository is related to AI/ML."""
        # Check topics
        topics = repo.get_topics()
        if any(keyword in topics for keyword in self.ai_ml_keywords):
            return True

        # Check name and description
        text_to_check = f"{repo.name} {repo.description or ''}".lower()
        return any(keyword.replace("-", " ") in text_to_check for keyword in self.ai_ml_keywords)

    def get_repo_details(self, repo_full_name: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a specific repository."""
        try:
            repo = self.github.get_repo(repo_full_name)
            return self._extract_repo_data(repo)
        except Exception as e:
            print_error(f"Error getting details for repo {repo_full_name}: {e}")
            return None


@click.command()
@click.option("--token", "-t", help="GitHub API token (or set GITHUB_TOKEN env var)")
@click.option("--days", "-d", default=7, help="Number of days to look back for trending repos")
@click.option("--max-repos", "-m", default=100, help="Maximum number of repositories to collect")
@click.option("--output", "-o", help="Output file path (default: data/tools/trending_repos.json)")
def main(token: Optional[str], days: int, max_repos: int, output: Optional[str]):
    """Scrape GitHub for trending AI/ML repositories."""
    print_info("🤖 AI/ML Tools Tracker - GitHub Scraper")
    print_info("=" * 50)

    # Ensure directories exist
    ensure_data_directories()

    # Initialize scraper
    scraper = GitHubScraper(github_token=token)

    try:
        # Search for trending repositories
        trending_repos = scraper.search_trending_repos(days_back=days, max_repos=max_repos)

        if not trending_repos:
            print_warning("No trending repositories found")
            update_metadata("github_scrape", "no_data", {"repos_found": 0})
            return

        # Prepare output data
        output_data = {
            "metadata": {
                "generated_at": get_current_timestamp(),
                "days_back": days,
                "max_repos": max_repos,
                "total_repos": len(trending_repos),
                "search_keywords": scraper.ai_ml_keywords,
            },
            "repositories": trending_repos,
        }

        # Save to file
        if not output:
            output = get_project_root() / "data" / "tools" / "trending_repos.json"
        else:
            output = Path(output)

        if save_json_file(output_data, output):
            print_success(f"Saved {len(trending_repos)} repositories to {output}")
            update_metadata(
                "github_scrape",
                "success",
                {"repos_collected": len(trending_repos), "output_file": str(output)},
            )
        else:
            print_error("Failed to save repository data")
            update_metadata("github_scrape", "error", {"error": "Failed to save data"})

    except Exception as e:
        print_error(f"Scraping failed: {e}")
        update_metadata("github_scrape", "error", {"error": str(e)})


if __name__ == "__main__":
    main()
