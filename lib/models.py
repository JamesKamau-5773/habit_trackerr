import os
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

db_dir = 'db'
db_file = 'habit_tracker.db'

if not os.path.exists(db_dir):
    os.makedirs(db_dir)

db_path = os.path.join(db_dir, db_file)

if not os.path.exists(db_path):
    open(db_path, 'w').close()

engine = create_engine(f'sqlite:///{db_path}')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Habit(Base):
    __tablename__ = 'habits'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', backref='habits')
    streak = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

class Completion(Base):
    __tablename__ = 'completions'
    id = Column(Integer, primary_key=True)
    habit_id = Column(Integer, ForeignKey('habits.id'))
    habit = relationship('Habit', backref='completions')
    completed_at = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text)

Base.metadata.create_all(engine)