import os


def read_secret(secret_name: str, default: str = None) -> str:
    secret_path = f"/run/secrets/{secret_name}"
    if os.path.exists(secret_path):
        with open(secret_path, "r") as f:
            return f.read().strip()


DB_HOST = read_secret("db_host")
DB_PORT = read_secret("db_port")
DB_NAME = read_secret("db_name")
DB_USER = read_secret("db_user")
DB_PASS = read_secret("db_pass")
SECRET_AUTH = read_secret("secret_auth")

# DB_HOST = "postgres"
# DB_PORT = "5432"
# DB_NAME = "clean_db"
# DB_USER = "admin"
# DB_PASS = "admin"
# SECRET_AUTH = "SECRET"