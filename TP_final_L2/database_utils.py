import os
from sqlalchemy import create_engine
from models import Base


def create_engine_instance(db_folder, db_name):
    # Create the folder if it does not exist
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    # Full path to the database file
    DATABASE_URL = os.path.join(db_folder, db_name)

    # Create an engine instance for the SQLite database in the specified path
    engine = create_engine(f'sqlite:///{DATABASE_URL}')

    return engine


def create_database_tables(engine):
    # Create the table in the database (Class must be defined).
    Base.metadata.create_all(engine)
