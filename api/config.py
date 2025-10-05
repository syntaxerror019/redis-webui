import os
from dotenv import load_dotenv

load_dotenv()

def load_secret_key():
    return os.getenv('SECRET_KEY')

def load_config():
    UI_HOST = os.getenv('UI_HOST', '0.0.0.0')  # Example for additional config variables
    UI_PORT = os.getenv('UI_PORT', 8080)

    HOST = os.getenv('REDIS_HOST', 'localhost')
    PORT = os.getenv('REDIS_PORT', 6379)
    SSL = os.getenv('REDIS_SSL', 'false').lower() == 'true'

    return {
        "UI_HOST": UI_HOST,
        "UI_PORT": UI_PORT,
        "REDIS_HOST": HOST,
        "REDIS_PORT": PORT,
        "REDIS_SSL": SSL
    }