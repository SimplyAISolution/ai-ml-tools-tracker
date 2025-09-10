"""Utility functions for AI/ML Tools Tracker."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

import colorama
from colorama import Fore, Style


# Initialize colorama for cross-platform colored output
colorama.init()


def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent


def ensure_data_directories():
    """Ensure all required data directories exist."""
    root = get_project_root()
    directories = [
        root / "data" / "tools",
        root / "data" / "metadata",
        root / "prompts" / "categories" / "code_generation",
        root / "prompts" / "categories" / "text_analysis",
        root / "prompts" / "categories" / "image_generation",
        root / "prompts" / "categories" / "data_science",
        root / "prompts" / "categories" / "general",
        root / "prompts" / "templates",
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def load_json_file(file_path: Path) -> Optional[Dict[str, Any]]:
    """Load JSON data from file."""
    try:
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print_error(f"Error loading JSON from {file_path}: {e}")
    return None


def save_json_file(data: Dict[str, Any], file_path: Path) -> bool:
    """Save data to JSON file."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print_error(f"Error saving JSON to {file_path}: {e}")
        return False


def get_current_timestamp() -> str:
    """Get current timestamp in ISO format."""
    return datetime.utcnow().isoformat() + "Z"


def print_success(message: str):
    """Print success message in green."""
    print(f"{Fore.GREEN}✓ {message}{Style.RESET_ALL}")


def print_error(message: str):
    """Print error message in red."""
    print(f"{Fore.RED}✗ {message}{Style.RESET_ALL}")


def print_info(message: str):
    """Print info message in blue."""
    print(f"{Fore.BLUE}ℹ {message}{Style.RESET_ALL}")


def print_warning(message: str):
    """Print warning message in yellow."""
    print(f"{Fore.YELLOW}⚠ {message}{Style.RESET_ALL}")


def update_metadata(update_type: str, status: str, details: Optional[Dict] = None):
    """Update metadata about the last operation."""
    root = get_project_root()
    metadata_file = root / "data" / "metadata" / "last_update.json"

    metadata = {
        "last_update": get_current_timestamp(),
        "update_type": update_type,
        "status": status,
        "details": details or {},
    }

    save_json_file(metadata, metadata_file)


def validate_repo_data(repo_data: Dict[str, Any]) -> bool:
    """Validate repository data structure."""
    required_fields = [
        "name",
        "full_name",
        "description",
        "html_url",
        "stars",
        "language",
        "created_at",
        "updated_at",
    ]

    for field in required_fields:
        if field not in repo_data:
            return False

    return True
