import os
from dotenv import load_dotenv

load_dotenv()
print(f"BOT_TOKEN: {os.getenv('BOT_TOKEN')}")
