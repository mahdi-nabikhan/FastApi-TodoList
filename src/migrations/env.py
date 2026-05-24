import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from pathlib import Path
from dotenv import load_dotenv
from tasks.models import *
from users.models import *

BASE_DIR = Path(__file__).resolve().parent.parent / 'core'
ENV_PATH = BASE_DIR / '.env'
load_dotenv(ENV_PATH)


from core.database import Base   

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')
if DATABASE_URL:
    config.set_main_option('sqlalchemy.url', DATABASE_URL)
else:
    raise ValueError('SQLALCHEMY_DATABASE_URL is not set in the environment variables')
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,

    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,render_as_batch=True
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()