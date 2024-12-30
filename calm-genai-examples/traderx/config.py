# Configuration settings for the TraderX Python implementation

import os

# Database configuration settings
@CALMDatabaseConfig("Database configuration settings for TraderX")
DATABASE_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
    'user': os.getenv('DB_USER', 'traderx_user'),
    'password': os.getenv('DB_PASSWORD', 'traderx_password'),
    'database': os.getenv('DB_NAME', 'traderx_db')
}

# Other necessary configurations
@CALMAppConfig("Application configuration settings for TraderX")
APP_CONFIG = {
    'debug': os.getenv('DEBUG', 'False').lower() in ('true', '1', 't'),
    'secret_key': os.getenv('SECRET_KEY', 'your_secret_key')
}
