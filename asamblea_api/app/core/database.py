from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.settings import get_property

# Fetch database URL from settings
database_url = get_property('database_url')

# Dynamically set connect_args for SQLite
connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}

# Initialize the engine
try:
    engine = create_engine(database_url, connect_args=connect_args)
except Exception as e:
    raise RuntimeError(f"Failed to initialize the database engine: {e}")

# Create sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarative class
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as ex:
        # Optional logging for debugging
        print(f"Database session error: {ex}")
        raise
    finally:
        db.close()
