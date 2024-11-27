# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from enum import Enum
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///./votaciones.db"
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
#
# class QuestionType(Enum):
#      YES_NO = 1
#      CUSTOM = 2
#
# class Questions(Base):
#     __tablename__ = "questions"
#
#     id = Column(Integer, primary_key=True, index=True)
#     content = Column(String)
#     type = Column(String)
#
# Base.metadata.create_all(bind=engine)
#
# db = SessionLocal()