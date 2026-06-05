import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.core.database import get_db
from app.models import Base, Owner
from app.core.config import TEST_DATABASE_URL

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функція-замінник для FastAPI, яка повертає сесію ТЕСТОВОЇ бази
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    # Підміняємо оригінальний get_db у FastAPI на наш override_get_db
    app.dependency_overrides[get_db] = override_get_db
    
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    yield
    
    app.dependency_overrides.clear()

# Фікстура клієнта, щоб зручно викликати його в тестах
@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def sample_owner():
    """Створює власника в базі для тестів, де потрібен готовий користувач"""
    db = TestingSessionLocal()
    
    owner = Owner(
        name="Петренко", 
        first_name="Орест", 
        person_nomber=99999
    )
    
    db.add(owner)
    db.commit()
    db.refresh(owner)
    
    yield owner
    
    db.close()