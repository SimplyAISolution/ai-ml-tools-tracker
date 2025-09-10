"""Data processing utilities for AI/ML Tools Tracker."""

import json
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

import click
from .utils import (
    get_project_root,
    load_json_file,
    save_json_file,
    print_success,
    print_error,
    print_info,
    get_current_timestamp,
)


class DataProcessor:
    """Process and analyze collected repository data."""

    def __init__(self):
        """Initialize the data processor."""
        self.root = get_project_root()
        self.data_dir = self.root / "data" / "tools"

    def load_trending_repos(self) -> Optional[Dict[str, Any]]:
        """Load the trending repositories data."""
        trending_file = self.data_dir / "trending_repos.json"
        return load_json_file(trending_file)

    def analyze_repositories(self, repos_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze repository data and generate insights."""
        repositories = repos_data.get("repositories", [])

        if not repositories:
            return {"error": "No repositories to analyze"}

        # Language analysis
        languages = [repo["language"] for repo in repositories if repo["language"]]
        language_stats = Counter(languages)

        # Topic analysis
        all_topics = []
        for repo in repositories:
            all_topics.extend(repo.get("topics", []))
        topic_stats = Counter(all_topics)

        # Stars analysis
        star_counts = [repo["stars"] for repo in repositories]
        star_stats = {
            "total": sum(star_counts),
            "average": sum(star_counts) / len(star_counts) if star_counts else 0,
            "median": sorted(star_counts)[len(star_counts) // 2] if star_counts else 0,
            "max": max(star_counts) if star_counts else 0,
            "min": min(star_counts) if star_counts else 0,
        }

        # Owner type analysis
        owner_types = Counter(repo["owner"]["type"] for repo in repositories)

        # Recent activity analysis
        recent_repos = []
        cutoff_date = datetime.now() - timedelta(days=30)

        for repo in repositories:
            if repo.get("updated_at"):
                updated_at = datetime.fromisoformat(repo["updated_at"].replace("Z", "+00:00"))
                if updated_at.replace(tzinfo=None) > cutoff_date:
                    recent_repos.append(repo)

        # License analysis
        licenses = [repo["license"] for repo in repositories if repo["license"]]
        license_stats = Counter(licenses)

        analysis = {
            "summary": {
                "total_repositories": len(repositories),
                "total_stars": star_stats["total"],
                "average_stars": round(star_stats["average"], 2),
                "recently_active": len(recent_repos),
                "unique_languages": len(language_stats),
                "unique_topics": len(topic_stats),
            },
            "languages": dict(language_stats.most_common(10)),
            "topics": dict(topic_stats.most_common(15)),
            "star_statistics": star_stats,
            "owner_types": dict(owner_types),
            "licenses": dict(license_stats.most_common(10)),
            "top_repositories": self._get_top_repositories(repositories, 10),
            "generated_at": get_current_timestamp(),
        }

        return analysis

    def _get_top_repositories(self, repositories: List[Dict], limit: int = 10) -> List[Dict]:
        """Get top repositories by stars."""
        sorted_repos = sorted(repositories, key=lambda x: x["stars"], reverse=True)

        top_repos = []
        for repo in sorted_repos[:limit]:
            top_repos.append(
                {
                    "name": repo["name"],
                    "full_name": repo["full_name"],
                    "description": repo["description"],
                    "html_url": repo["html_url"],
                    "stars": repo["stars"],
                    "language": repo["language"],
                    "topics": repo.get("topics", [])[:5],  # Limit topics for readability
                }
            )

        return top_repos

    def generate_markdown_report(self, analysis: Dict[str, Any]) -> str:
        """Generate a markdown report from analysis data."""
        if "error" in analysis:
            return f"# Analysis Report\n\nError: {analysis['error']}\n"

        summary = analysis["summary"]

        markdown = f"""# AI/ML Tools Analysis Report

*Generated on {analysis['generated_at']}*

## Summary

- **Total Repositories**: {summary['total_repositories']:,}
- **Total Stars**: {summary['total_stars']:,}
- **Average Stars**: {summary['average_stars']}
- **Recently Active**: {summary['recently_active']} repositories
- **Languages Represented**: {summary['unique_languages']}
- **Unique Topics**: {summary['unique_topics']}

## Top Programming Languages

| Language | Count |
|----------|-------|"""

        for lang, count in list(analysis["languages"].items())[:10]:
            markdown += f"\n| {lang or 'Unknown'} | {count} |"

        markdown += f"""

## Popular Topics

| Topic | Count |
|-------|-------|"""

        for topic, count in list(analysis["topics"].items())[:15]:
            markdown += f"\n| {topic} | {count} |"

        markdown += f"""

## Star Statistics

- **Total Stars**: {analysis['star_statistics']['total']:,}
- **Average Stars**: {analysis['star_statistics']['average']:.1f}
- **Median Stars**: {analysis['star_statistics']['median']:,}
- **Most Starred**: {analysis['star_statistics']['max']:,}
- **Least Starred**: {analysis['star_statistics']['min']:,}

## Top Repositories by Stars

| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|"""

        for repo in analysis["top_repositories"]:
            desc = (
                (repo["description"][:80] + "...")
                if len(repo.get("description", "")) > 80
                else repo.get("description", "")
            )
            markdown += f"\n| [{repo['name']}]({repo['html_url']}) | {repo['stars']:,} | {repo['language'] or 'N/A'} | {desc} |"

        markdown += f"""

## License Distribution

| License | Count |
|---------|-------|"""

        for license_name, count in analysis["licenses"].items():
            markdown += f"\n| {license_name} | {count} |"

        markdown += """

---
*This report was automatically generated by the AI/ML Tools Tracker*
"""

        return markdown

    def process_and_save_analysis(self) -> bool:
        """Process repository data and save analysis."""
        print_info("Processing repository data...")

        # Load trending repositories data
        repos_data = self.load_trending_repos()
        if not repos_data:
            print_error("No repository data found to process")
            return False

        # Generate analysis
        analysis = self.analyze_repositories(repos_data)

        # Save analysis as JSON
        analysis_file = self.data_dir / "analysis.json"
        if not save_json_file(analysis, analysis_file):
            print_error("Failed to save analysis data")
            return False

        # Generate and save markdown report
        markdown_report = self.generate_markdown_report(analysis)
        report_file = self.data_dir / "analysis_report.md"

        try:
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(markdown_report)
            print_success(f"Generated analysis report: {report_file}")
        except Exception as e:
            print_error(f"Failed to save markdown report: {e}")
            return False

        print_success("Data processing completed successfully")
        return True


@click.command()
@click.option("--input-file", "-i", help="Input JSON file path")
@click.option("--output-dir", "-o", help="Output directory for analysis files")
def main(input_file: Optional[str], output_dir: Optional[str]):
    """Process and analyze repository data."""
    print_info("🔍 AI/ML Tools Tracker - Data Processor")
    print_info("=" * 50)

    processor = DataProcessor()

    # Override paths if specified
    if input_file:
        data = load_json_file(Path(input_file))
        if not data:
            print_error(f"Could not load data from {input_file}")
            return
    else:
        data = processor.load_trending_repos()
        if not data:
            print_error("No trending repositories data found")
            return

    # Generate analysis
    analysis = processor.analyze_repositories(data)

    # Determine output directory
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = processor.data_dir

    # Save analysis
    analysis_file = output_path / "analysis.json"
    if save_json_file(analysis, analysis_file):
        print_success(f"Saved analysis to {analysis_file}")

    # Save markdown report
    markdown_report = processor.generate_markdown_report(analysis)
    report_file = output_path / "analysis_report.md"

    try:
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(markdown_report)
        print_success(f"Generated report: {report_file}")
    except Exception as e:
        print_error(f"Failed to save report: {e}")


if __name__ == "__main__":
    main()
