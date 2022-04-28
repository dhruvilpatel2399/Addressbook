
from sqlalchemy import Float, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Address(Base):
    __tablename__ = "Address"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    address = Column(String)
    longitude = Column(Float,unique=True)
    latitude = Column(Float,unique=True)


