import os
from dotenv import load_dotenv

load_dotenv()

print("DB URL =", os.getenv("DATABASE_URL"))
print("DB USER =", os.getenv("DB_USER"))
print("DB PASSWORD =", os.getenv("DB_PASSWORD"))