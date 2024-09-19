from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base, session

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    contacts = relationship("Contact", back_populates="group")

    @classmethod
    def create(cls, name):
        group = cls(name=name)
        session.add(group)
        session.commit()
        return group

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()
