import os

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

SOURCE_CHANNEL = int(os.environ.get("SOURCE_CHANNEL", ""))  # Example: -1001234567890
TARGET_CHANNEL = int(os.environ.get("TARGET_CHANNEL", ""))  # Example: -1009876543210

AUTOFILTER_BOT_USERNAME = os.environ.get("AUTOFILTER_BOT_USERNAME", "YourAutoFilterBot")  # without @
HOW_TO_DOWNLOAD_URL = os.environ.get("HOW_TO_DOWNLOAD_URL", "https://t.me/yourchannel/123")
