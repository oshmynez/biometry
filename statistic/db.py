import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    operation_id = Column(Integer, ForeignKey('operation.id'))
    operation = relationship('Operation', back_populates='transaction')


class Operations(Base):
    __tablename__ = 'operations'

    id = Column(primary_key=True)
    status = Column(Integer, nullable=False)
    transaction = relationship("Transaction", back_populates="operation")

