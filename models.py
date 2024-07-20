from sqlalchemy import Float, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    ip = Column(String(15), index=True)

    cities = relationship("City", secondary = "user_cities")
    last_city_id = Column(Integer, default=-1)


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True)
    fias_id = Column(String(300), index=True)
    lat = Column(Float)
    lon = Column(Float)
    cnt = Column(Integer)


class UserCity(Base):
    __tablename__ = "user_cities"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    city_id = Column(Integer, ForeignKey("cities.id"))
    order = Column(Integer)
