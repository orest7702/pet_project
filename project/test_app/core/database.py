from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL

# 1. Створюємо "двигун" (engine). Він відповідає за фізичне TCP-з'єднання з PostgreSQL.
engine = create_engine(DATABASE_URL)

# 2. Створюємо фабрику сесій. 
# Коли нам треба буде зробити запит (наприклад, зберегти юзера), ми будемо викликати SessionLocal()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Створюємо базовий клас.
# Усі наші майбутні таблиці (User, Task) будуть успадковуватися від нього.
Base = declarative_base()

# Додай це в кінець файлу database.py
def get_db():
    db = SessionLocal()
    try:
        yield db  # Видаємо сесію для використання
    finally:
        db.close()  # Обов'язково закриваємо після завершення запиту