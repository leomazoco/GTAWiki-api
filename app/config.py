import os
import configparser
from urllib.parse import quote_plus


def get_env_or_default(key, default):
    return os.environ.get(key, default)

def load_postgresql_config(app, config):
    if "PostgreSQL" in config:
        postgresql = config["PostgreSQL"]
        user = postgresql.get("user", get_env_or_default('POSTGRES_USER', ''))
        password = quote_plus(postgresql.get("password", get_env_or_default('POSTGRES_PASS', '')))
        host = postgresql.get("host", get_env_or_default('POSTGRES_HOST', 'localhost'))
        port = postgresql.get("port", get_env_or_default('POSTGRES_PORT', '5432'))
        database = postgresql.get("databse", get_env_or_default('POSTGRES_DATABASE', 'gtawikidb'))
    else:
        user = get_env_or_default('POSTGRES_USER', '')
        password = quote_plus(get_env_or_default('POSTGRES_PASSWORD', ''))
        host = get_env_or_default('POSTGRES_HOST', '')
        port = get_env_or_default('POSTGRES_PORT', '')
        database = get_env_or_default('POSTGRES_DB', '')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/{database}'

def read_config(app):
    config = configparser.ConfigParser()
    config_file = 'config.ini'

    if os.path.isfile(config_file):
        config.read(config_file)

    load_postgresql_config(app, config)
