"""
Centralized configuration for the AI Chat Assistant.
Loads settings from environment variables with sensible defaults.
"""

import os
from dotenv import load_dotenv

# ── Load .env ────────────────────────────────────────────────
load_dotenv()

# ── LLM Settings ─────────────────────────────────────────────
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.0-flash")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1024"))

# ── Memory Settings ──────────────────────────────────────────
MEMORY_WINDOW_SIZE = 10  # Number of conversation turns to retain

# ── Prompt Chaining ──────────────────────────────────────────
ENABLE_PROMPT_CHAINING = True  # Enable multi-step reasoning by default
CHAIN_COMPLEXITY_THRESHOLD = 50  # Word count threshold to trigger chaining

# ── Response Evaluation ──────────────────────────────────────
ENABLE_SELF_EVALUATION = True
CONFIDENCE_THRESHOLD = 0.7  # Minimum confidence score to accept a response
MAX_RETRIES = 2  # Maximum retry attempts for low-confidence responses

# ── Available Agent Roles ─────────────────────────────────────
AVAILABLE_ROLES = {
    "default": "Helpful AI Assistant",
    "coder": "Expert Software Engineer",
    "tutor": "Patient and Thorough Tutor",
    "analyst": "Data Analyst & Researcher",
    "creative": "Creative Writer & Storyteller",
}

DEFAULT_ROLE = "default"
