from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base, session
from models.group import Group

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship("Group", back_populates="contacts")

    @classmethod
    def create(cls, name, phone, email, group_name):
        group = Group.find_by_name(group_name)
        if not group:
            print(f"Group '{group_name}' not found!")
            return None
        contact = cls(name=name, phone=phone, email=email, group=group)
        session.add(contact)
        session.commit()
        return contact

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def delete(cls, contact):
        session.delete(contact)
        session.commit()

    @classmethod
    def update(cls, contact, name=None, phone=None, email=None, group_name=None):
        if name:
            contact.name = name
        if phone:
            contact.phone = phone
        if email:
            contact.email = email
        if group_name:
            group = Group.find_by_name(group_name)
            if group:
                contact.group = group
        session.commit()
