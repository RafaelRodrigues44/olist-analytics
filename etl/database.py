import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")

def get_db_engine():
    if not DB_URL:
        return None
    return create_engine(DB_URL)