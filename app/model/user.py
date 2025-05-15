from sqlalchemy import Column, Integer, String

from app.extension.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    username = Column(String(50), nullable=True)
    password = Column(String(100), nullable=False)
    email = Column(String(50), unique=True, nullable=False)

    role = Column(String(20), nullable=False, default='user')