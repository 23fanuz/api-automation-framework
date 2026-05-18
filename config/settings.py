import os

from dotenv import load_dotenv

# Load env variables from .env
load_dotenv()

class Settings:
    """
    Centralized framework config.

    This class provides environment specific settings
    """

    BASE_URL = os.getenv("BASE_URL")