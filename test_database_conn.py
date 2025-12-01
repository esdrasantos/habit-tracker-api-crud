import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()  # carrega o .env na raiz

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("CONNECTED OK", result.scalar())

except Exception as e:
    print("ERROR:", e)