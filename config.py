import os

# ---------------- BOT CORE ----------------
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = int(os.getenv("OWNER_ID"))

# ---------------- DATABASE ----------------
MONGO_URI = os.getenv("MONGO_URI")

# ---------------- CHANNELS ----------------
# Force users to join updates channel (optional feature)
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL")  # example: @yourchannel

# Log channel for bot activities (uploads, errors, users)
LOG_CHANNEL = os.getenv("LOG_CHANNEL")  # example: -100xxxxxxxxxx
