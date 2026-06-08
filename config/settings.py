import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    BASE_URL = os.getenv("BASE_URL")

    USERNAME = os.getenv("USERNAME")

    PASSWORD = os.getenv("PASSWORD")

    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"

    BROWSER = os.getenv("BROWSER", "chromium")

    TIMEOUT = int(os.getenv("TIMEOUT", 30000))