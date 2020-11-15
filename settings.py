import os

DEBUG = os.getenv("DEBUG", False)

if DEBUG:
    print("You are now in DEBUG mode!")
    from pathlib import Path
    from dotenv import load_dotenv

    env_path = Path(".") / ".env.debug"
    load_dotenv(dotenv_path=env_path)
    from settings_files.development import *
else:
    print("You are now in PRODUCTION mode!")
    from settings_files.production import *
