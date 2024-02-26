from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

GITLAB_API_URL = os.environ.get("GITLAB_API_URL")
GITLAB_SSH_PORT = os.environ.get("GITLAB_SSH_PORT")
GITLAB_APP_ID = os.environ.get("GITLAB_APP_ID")
GITLAB_SECRET = os.environ.get("GITLAB_SECRET_KEY")
GITLAB_GOD_LOGIN = os.environ.get("GITLAB_GOD_LOGIN")
GITLAB_GOD_PASSWORD = os.environ.get("GITLAB_GOD_PASSWORD")


JWT_SECRET_CODE = os.environ.get("JWT_SECRET_CODE")