# 🤖 AI/ML Tools Tracker

[![Daily Update](https://github.com/SimplyAISolution/ai-ml-tools-tracker/actions/workflows/daily-update.yml/badge.svg)](https://github.com/SimplyAISolution/ai-ml-tools-tracker/actions/workflows/daily-update.yml)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Automated collection and tracking of the latest AI & Machine Learning technologies, tools, and curated prompt libraries. Updated daily via GitHub Actions to keep you informed about the rapidly evolving AI/ML landscape.

## ✨ Features

- **🔍 Automated GitHub Scraping**: Daily collection of trending AI/ML repositories
- **📊 Data Analysis**: Statistical insights and trends analysis
- **📝 Comprehensive Reporting**: Markdown and JSON reports with detailed metrics
- **🎯 Curated Prompt Library**: Organized collection of prompts for different AI models
- **⚙️ GitHub Actions Integration**: Fully automated daily updates
- **📈 Historical Tracking**: Track changes and trends over time
- **🔧 Extensible Architecture**: Easy to customize and extend

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- GitHub account and personal access token
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SimplyAISolution/ai-ml-tools-tracker.git
   cd ai-ml-tools-tracker
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   # Create .env file
   echo "GITHUB_TOKEN=your_github_token_here" > .env
   ```

4. **Run your first collection**:
   ```bash
   python -m scripts.github_scraper --days 7 --max-repos 50
   ```

### GitHub Token Setup

1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Select scopes: `public_repo`, `read:org`
4. Copy the token and add it to your `.env` file

## 📁 Project Structure

```
ai-ml-tools-tracker/
├── .github/
│   └── workflows/
│       └── daily-update.yml          # GitHub Actions automation
├── scripts/
│   ├── __init__.py
│   ├── github_scraper.py             # Main scraping logic
│   ├── data_processor.py             # Data analysis and processing
│   └── utils.py                      # Utility functions
├── data/
│   ├── tools/
│   │   ├── trending_repos.json       # Latest repository data
│   │   ├── analysis.json             # Statistical analysis
│   │   └── analysis_report.md        # Human-readable report
│   └── metadata/
│       └── last_update.json          # Update tracking
├── prompts/
│   ├── README.md                     # Prompt library documentation
│   ├── categories/                   # Categorized prompts
│   │   ├── code_generation/         # Programming and code prompts
│   │   ├── text_analysis/           # Text processing prompts
│   │   ├── image_generation/        # Image creation prompts
│   │   ├── data_science/            # Data analysis prompts
│   │   └── general/                 # General-purpose prompts
│   └── templates/                    # Reusable prompt templates
├── docs/
│   └── api.md                       # API documentation
├── requirements.txt                  # Python dependencies
├── setup.py                         # Package configuration
└── README.md                        # This file
```

## 🔧 Usage

### Command Line Interface

#### Scrape GitHub Repositories
```bash
# Basic usage
python -m scripts.github_scraper

# Custom parameters
python -m scripts.github_scraper --days 14 --max-repos 200

# Specify output file
python -m scripts.github_scraper --output custom_data.json
```

#### Process and Analyze Data
```bash
# Process latest data
python -m scripts.data_processor

# Process custom file
python -m scripts.data_processor --input-file custom_data.json
```

### Python API

```python
from scripts.github_scraper import GitHubScraper
from scripts.data_processor import DataProcessor

# Initialize scraper
scraper = GitHubScraper(github_token="your_token")

# Collect repositories
repos = scraper.search_trending_repos(days_back=7, max_repos=100)

# Analyze data
processor = DataProcessor()
analysis = processor.analyze_repositories({"repositories": repos})

# Generate report
report = processor.generate_markdown_report(analysis)
```

### Automated Daily Updates

The project includes GitHub Actions workflow that automatically:
1. Scrapes trending AI/ML repositories daily
2. Processes and analyzes the collected data
3. Generates updated reports and statistics
4. Commits changes back to the repository

The workflow runs daily at 08:00 UTC and can also be triggered manually.

## 📊 Data Collection

### What We Track

- **Repository Metadata**: Name, description, URL, stars, forks
- **Technical Details**: Primary language, topics, license
- **Activity Metrics**: Creation date, last update, recent pushes
- **Community Data**: Open issues, contributors, README content
- **Owner Information**: User vs organization, profile links

### Search Criteria

The scraper focuses on repositories with:
- AI/ML related keywords in name, description, or topics
- Recent activity (configurable timeframe)
- Minimum star threshold (configurable)
- Active development (recent commits)

### Keywords Tracked

```
artificial-intelligence, machine-learning, deep-learning, neural-networks,
computer-vision, natural-language-processing, nlp, ai, ml, tensorflow,
pytorch, keras, scikit-learn, opencv, transformers, huggingface, llm,
gpt, bert, stable-diffusion, langchain, prompt-engineering, rag
```

## 🎯 Prompt Library

Our curated prompt library includes:

### Categories
- **🔧 Code Generation**: Programming assistance and code review
- **📝 Text Analysis**: Content processing and understanding
- **🎨 Image Generation**: Visual content creation prompts
- **📊 Data Science**: Analysis and machine learning prompts
- **💡 General**: Versatile prompts for common tasks

### Features
- Model compatibility indicators (GPT, Claude, Gemini, etc.)
- Difficulty levels (beginner, intermediate, advanced)
- Usage examples and best practices
- Performance metrics and tips

[📖 Browse the Prompt Library](prompts/README.md)

## 📈 Sample Output

### Repository Analysis Report

```markdown
# AI/ML Tools Analysis Report

## Summary
- **Total Repositories**: 100
- **Total Stars**: 150,000
- **Average Stars**: 1,500
- **Recently Active**: 85 repositories
- **Languages Represented**: 12
- **Unique Topics**: 45

## Top Programming Languages
| Language   | Count |
|------------|-------|
| Python     | 45    |
| JavaScript | 20    |
| Go         | 15    |
| Rust       | 10    |

## Popular Topics
| Topic              | Count |
|--------------------|-------|
| machine-learning   | 30    |
| deep-learning      | 25    |
| transformers       | 20    |
| computer-vision    | 18    |
```

## ⚡ Performance

- **Collection Speed**: ~100 repositories per minute
- **API Efficiency**: Respects GitHub rate limits (5,000/hour)
- **Data Processing**: Sub-second analysis for 1,000+ repositories
- **Storage**: Efficient JSON structure, ~1KB per repository

## 🛠️ Development

### Setup Development Environment

1. **Clone and install**:
   ```bash
   git clone https://github.com/SimplyAISolution/ai-ml-tools-tracker.git
   cd ai-ml-tools-tracker
   pip install -r requirements.txt
   pip install -e .
   ```

2. **Run tests**:
   ```bash
   pytest tests/
   ```

3. **Code formatting**:
   ```bash
   black scripts/
   flake8 scripts/
   ```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Adding New Features

- **New Data Sources**: Extend `GitHubScraper` class
- **Analysis Metrics**: Add methods to `DataProcessor`
- **Prompt Categories**: Create new directories in `prompts/categories/`
- **Automation**: Modify `.github/workflows/daily-update.yml`

## 📋 API Reference

Detailed API documentation is available in [docs/api.md](docs/api.md).

### Key Classes

- `GitHubScraper`: Repository data collection
- `DataProcessor`: Analysis and reporting
- Utility functions for data handling

### Configuration Options

- Search timeframes and result limits
- Output formats and destinations
- Analysis parameters and metrics
- Automation schedules

## 🔒 Privacy & Ethics

- Only collects publicly available repository data
- Respects GitHub's Terms of Service and API limits
- No personal user data collection
- Open source and transparent methodology

## 🤝 Community

- **Issues**: [GitHub Issues](https://github.com/SimplyAISolution/ai-ml-tools-tracker/issues)
- **Discussions**: [GitHub Discussions](https://github.com/SimplyAISolution/ai-ml-tools-tracker/discussions)
- **Contributing**: See [Contributing Guidelines](#contributing)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- GitHub API for data access
- Open source AI/ML community
- Contributors and maintainers

---

**⭐ Star this repository** if you find it useful for tracking AI/ML tools and trends!

*Last updated: Daily via automated GitHub Actions*
