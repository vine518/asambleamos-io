# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///./votaciones.db"
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
#
# class Vote(Base):
#     __tablename__ = "votes"
#
#     id = Column(Integer, primary_key=True, index=True)
#     opcion = Column(String)
#     opcion = Column(String)
#     asamblea_id = Column(Integer, ForeignKey("asambleas.id"))
#
# Base.metadata.create_all(bind=engine)
#
# db = SessionLocal()
