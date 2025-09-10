# AI/ML Tools Tracker API Documentation

## Overview

The AI/ML Tools Tracker provides both command-line tools and programmatic APIs for collecting, processing, and analyzing AI/ML repository data from GitHub.

## Command Line Interface

### GitHub Scraper

Scrape GitHub for trending AI/ML repositories.

```bash
python -m scripts.github_scraper [OPTIONS]
```

#### Options
- `--token, -t`: GitHub API token (or set `GITHUB_TOKEN` environment variable)
- `--days, -d`: Number of days to look back for trending repos (default: 7)
- `--max-repos, -m`: Maximum number of repositories to collect (default: 100)
- `--output, -o`: Output file path (default: `data/tools/trending_repos.json`)

#### Examples
```bash
# Basic usage with environment variable
export GITHUB_TOKEN="your_token_here"
python -m scripts.github_scraper

# Custom parameters
python -m scripts.github_scraper --days 14 --max-repos 200 --output custom_output.json

# With explicit token
python -m scripts.github_scraper --token "ghp_xxxxxxxxxxxx" --days 30
```

### Data Processor

Process and analyze collected repository data.

```bash
python -m scripts.data_processor [OPTIONS]
```

#### Options
- `--input-file, -i`: Input JSON file path (default: `data/tools/trending_repos.json`)
- `--output-dir, -o`: Output directory for analysis files (default: `data/tools/`)

#### Examples
```bash
# Process default data
python -m scripts.data_processor

# Process custom file
python -m scripts.data_processor --input-file custom_data.json --output-dir analysis/
```

## Python API

### GitHubScraper Class

```python
from scripts.github_scraper import GitHubScraper

# Initialize with token
scraper = GitHubScraper(github_token="your_token")

# Search for trending repositories
repos = scraper.search_trending_repos(days_back=7, max_repos=100)

# Get details for specific repository
repo_details = scraper.get_repo_details("tensorflow/tensorflow")
```

#### Methods

##### `__init__(github_token=None)`
Initialize the scraper with optional GitHub token.

**Parameters:**
- `github_token` (str, optional): GitHub API token. If not provided, uses `GITHUB_TOKEN` environment variable.

##### `search_trending_repos(days_back=7, max_repos=100)`
Search for trending AI/ML repositories.

**Parameters:**
- `days_back` (int): Number of days to look back for trending repos
- `max_repos` (int): Maximum number of repositories to collect

**Returns:**
- `List[Dict[str, Any]]`: List of repository data dictionaries

##### `get_repo_details(repo_full_name)`
Get detailed information about a specific repository.

**Parameters:**
- `repo_full_name` (str): Full name of repository (owner/repo)

**Returns:**
- `Dict[str, Any]` or `None`: Repository data dictionary or None if not found

### DataProcessor Class

```python
from scripts.data_processor import DataProcessor

# Initialize processor
processor = DataProcessor()

# Load trending repositories data
data = processor.load_trending_repos()

# Analyze repositories
analysis = processor.analyze_repositories(data)

# Generate markdown report
report = processor.generate_markdown_report(analysis)
```

#### Methods

##### `load_trending_repos()`
Load trending repositories data from default location.

**Returns:**
- `Dict[str, Any]` or `None`: Repository data or None if file not found

##### `analyze_repositories(repos_data)`
Analyze repository data and generate insights.

**Parameters:**
- `repos_data` (Dict[str, Any]): Repository data from scraper

**Returns:**
- `Dict[str, Any]`: Analysis results including statistics and insights

##### `generate_markdown_report(analysis)`
Generate a markdown report from analysis data.

**Parameters:**
- `analysis` (Dict[str, Any]): Analysis results from `analyze_repositories`

**Returns:**
- `str`: Formatted markdown report

##### `process_and_save_analysis()`
Process repository data and save analysis files.

**Returns:**
- `bool`: True if successful, False otherwise

### Utility Functions

```python
from scripts.utils import (
    get_project_root, ensure_data_directories, load_json_file, 
    save_json_file, update_metadata, validate_repo_data
)

# Get project root directory
root = get_project_root()

# Ensure all data directories exist
ensure_data_directories()

# Load JSON data
data = load_json_file(Path("data/file.json"))

# Save JSON data
success = save_json_file(data, Path("data/output.json"))

# Update metadata
update_metadata("scrape", "success", {"repos": 50})

# Validate repository data
is_valid = validate_repo_data(repo_dict)
```

## Data Formats

### Repository Data Structure

```json
{
  "metadata": {
    "generated_at": "2024-01-01T12:00:00Z",
    "days_back": 7,
    "max_repos": 100,
    "total_repos": 50,
    "search_keywords": ["machine-learning", "ai", "..."]
  },
  "repositories": [
    {
      "name": "repository-name",
      "full_name": "owner/repository-name",
      "description": "Repository description",
      "html_url": "https://github.com/owner/repo",
      "clone_url": "https://github.com/owner/repo.git",
      "stars": 1500,
      "forks": 250,
      "language": "Python",
      "topics": ["machine-learning", "pytorch"],
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2024-01-01T12:00:00Z",
      "pushed_at": "2024-01-01T11:30:00Z",
      "size": 2048,
      "open_issues": 15,
      "license": "MIT",
      "default_branch": "main",
      "archived": false,
      "disabled": false,
      "private": false,
      "owner": {
        "login": "username",
        "type": "User",
        "html_url": "https://github.com/username"
      },
      "readme_url": "https://raw.githubusercontent.com/...",
      "collected_at": "2024-01-01T12:00:00Z"
    }
  ]
}
```

### Analysis Data Structure

```json
{
  "summary": {
    "total_repositories": 100,
    "total_stars": 150000,
    "average_stars": 1500.0,
    "recently_active": 80,
    "unique_languages": 15,
    "unique_topics": 45
  },
  "languages": {
    "Python": 45,
    "JavaScript": 20,
    "Go": 15
  },
  "topics": {
    "machine-learning": 30,
    "artificial-intelligence": 25,
    "deep-learning": 20
  },
  "star_statistics": {
    "total": 150000,
    "average": 1500.0,
    "median": 800,
    "max": 25000,
    "min": 10
  },
  "owner_types": {
    "User": 60,
    "Organization": 40
  },
  "licenses": {
    "MIT": 40,
    "Apache-2.0": 25,
    "GPL-3.0": 10
  },
  "top_repositories": [...],
  "generated_at": "2024-01-01T12:00:00Z"
}
```

## Error Handling

The API uses standard HTTP status codes and provides detailed error messages:

```python
try:
    repos = scraper.search_trending_repos()
except Exception as e:
    print(f"Error: {e}")
    # Handle specific error types
```

Common errors:
- **Authentication Error**: Invalid or missing GitHub token
- **Rate Limit Error**: GitHub API rate limit exceeded
- **Network Error**: Connection issues
- **Data Error**: Invalid or corrupted data files

## Rate Limiting

GitHub API has rate limits:
- **Authenticated requests**: 5,000 requests per hour
- **Unauthenticated requests**: 60 requests per hour

The scraper includes automatic rate limiting with delays between requests.

## Environment Variables

- `GITHUB_TOKEN`: GitHub Personal Access Token for API authentication

## Configuration

Create a `.env` file in the project root:

```env
GITHUB_TOKEN=your_github_token_here
```

## Examples

### Complete Workflow Example

```python
import os
from scripts.github_scraper import GitHubScraper
from scripts.data_processor import DataProcessor
from scripts.utils import ensure_data_directories

# Set up environment
ensure_data_directories()

# Initialize scraper
scraper = GitHubScraper(github_token=os.getenv('GITHUB_TOKEN'))

# Collect data
repos = scraper.search_trending_repos(days_back=14, max_repos=200)

# Process and analyze
processor = DataProcessor()
analysis = processor.analyze_repositories({"repositories": repos})

# Generate reports
report = processor.generate_markdown_report(analysis)
print(report)
```

### Custom Analysis Example

```python
from scripts.data_processor import DataProcessor
from scripts.utils import load_json_file

# Load custom data
data = load_json_file("custom_repos.json")

# Custom analysis
processor = DataProcessor()
analysis = processor.analyze_repositories(data)

# Extract specific insights
top_languages = list(analysis["languages"].keys())[:5]
high_star_repos = [r for r in data["repositories"] if r["stars"] > 1000]

print(f"Top languages: {top_languages}")
print(f"High-star repositories: {len(high_star_repos)}")
```

## Contributing

See the main [README.md](../README.md) for contribution guidelines and development setup instructions.