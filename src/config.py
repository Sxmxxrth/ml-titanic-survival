import os

APP_ENV = os.getenv('APP_ENV', 'production')
PORT = int(os.getenv('PORT', 8000))
