# from sqlalchemy import create_engine, Column, Integer, String, Double, Numeric
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from datetime import datetime
# from enum import Enum as PyEnum
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///./votaciones.db"
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
#
#
# class Units(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     description = Column(String(255), nullable=True)
#     coeficient = Column(Numeric(10,2), nullable=False)
#     userId = Column(Integer, nullable=False, index=True, ForeignKey("asambleas.id"))
#
# class AssemblyStatus(PyEnum):
#     OPEN = "Abierta"
#     CLOSE = "Cerrada"
#     FINISHED = "Finalizada"
#
#
# class Assembly(Base):
#     __tablename__ = "assembly"
#
#     id = Column(Integer, primary_key=True, index=True)
#     date = Column(datetime, default=datetime.now, nullable=False)
#     status = Column(PyEnum(AssemblyStatus), default=AssemblyStatus.ABIERTA, nullable=False)
#     order_of_the_day = Column(String(255), nullable=True)
#     # Relación con RegistroVotante
#
#
# # voter_registry = relationship("RegistroVotante", back_populates="assembly")
# # votaciones = relationship("Votes", back_populates="assembly")
#
#
# db = SessionLocal()
