"""
Storage utilities for IrrVerEnglish.
Handles local storage of settings and statistics.
"""

import json
import os
from typing import Dict, Any
from pathlib import Path


class StorageManager:
    """Manages local storage of application data."""

    def __init__(self):
        self.app_dir = Path.home() / '.irrverenglish'
        self.app_dir.mkdir(exist_ok=True)

        self.settings_file = self.app_dir / 'settings.json'
        self.stats_file = self.app_dir / 'statistics.json'

    def save_settings(self, settings: Dict[str, Any]) -> bool:
        """Save application settings to local storage."""
        try:
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=4)
            return True
        except Exception:
            return False

    def load_settings(self) -> Dict[str, Any]:
        """Load application settings from local storage."""
        default_settings = {
            'theme': 'light',
            'creator_name': 'not_alviii',
            'language': 'en'
        }

        if not self.settings_file.exists():
            return default_settings

        try:
            with open(self.settings_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
                # Merge with defaults to ensure all keys exist
                default_settings.update(settings)
                return default_settings
        except Exception:
            return default_settings

    def save_statistics(self, stats: Dict[str, Any]) -> bool:
        """Save statistics to local storage."""
        try:
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=4)
            return True
        except Exception:
            return False

    def load_statistics(self) -> Dict[str, Any]:
        """Load statistics from local storage."""
        default_stats = {
            'total_questions': 0,
            'total_correct': 0,
            'total_incorrect': 0,
            'sessions': []
        }

        if not self.stats_file.exists():
            return default_stats

        try:
            with open(self.stats_file, 'r', encoding='utf-8') as f:
                stats = json.load(f)
                # Merge with defaults
                default_stats.update(stats)
                return default_stats
        except Exception:
            return default_stats

    def reset_statistics(self) -> bool:
        """Reset all statistics to default values."""
        default_stats = {
            'total_questions': 0,
            'total_correct': 0,
            'total_incorrect': 0,
            'sessions': []
        }
        return self.save_statistics(default_stats)
