"""
TraceMind AI Configuration

Central configuration file for project constants,
paths, and environment variables.
"""

from pathlib import Path
import os

from dotenv import load_dotenv

# ----------------------------
# Load Environment Variables
# ----------------------------

load_dotenv()

# ----------------------------
# Project Root
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent

# ----------------------------
# Directories
# ----------------------------

LOGS_DIR = BASE_DIR / "logs"

REPORTS_DIR = BASE_DIR / "reports"

DOCS_DIR = BASE_DIR / "docs"

SCREENSHOTS_DIR = BASE_DIR / "screenshots"

# ----------------------------
# Gemini
# ----------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ----------------------------
# Detection Thresholds
# ----------------------------

FAILED_LOGIN_THRESHOLD = 3

HIGH_RISK_SCORE = 80

MEDIUM_RISK_SCORE = 50

LOW_RISK_SCORE = 20

# ----------------------------
# Application
# ----------------------------

APP_NAME = "TraceMind AI"

VERSION = "1.0.0"