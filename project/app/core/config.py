import os
from dotenv import load_dotenv

# Змушуємо Python прочитати файл .env і завантажити змінні в пам'ять
load_dotenv()

# Отримуємо значення змінних. 
# Якщо їх немає в .env, беремо значення за замовчуванням (другий аргумент)
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "pet_project")

# Формуємо URL-адресу, яку зрозуміє SQLAlchemy
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"