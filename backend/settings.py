import os

# Environment variables set in .env file.
SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False


JWT_TOKEN_LOCATION = ["cookies"]
JWT_ACCESS_COOKIE_PATH = "/login"
JWT_COOKIE_CSRF_PROTECT = True
JWT_CSRF_IN_COOKIES = True
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
