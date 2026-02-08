import os
import streamlit as st 
from sqlalchemy import create_engine
from dotenv import load_dotenv

def get_db_url():
    try:
        return st.secrets["DATABASE_URL"]
    except (FileNotFoundError, KeyError):
        load_dotenv()
        return os.getenv("DATABASE_URL")

DB_URL = get_db_url()

def get_db_engine():
    if not DB_URL:
        return None
    return create_engine(DB_URL)