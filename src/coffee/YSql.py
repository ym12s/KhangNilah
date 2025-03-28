import os
import sqlite3
from datetime import datetime
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DB_PATH = os.path.join(BASE_DIR, "../sqlite/coffee_mtu.db")   

def get_connection():
    if not os.path.exists(DB_PATH):
         raise FileNotFoundError(f"Database file not found: {DB_PATH}")
    return sqlite3.connect(DB_PATH)    

