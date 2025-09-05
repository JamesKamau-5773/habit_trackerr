from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    habits = relationship('Habit', back_populates='category')

class Habit(Base):
    __tablename__ = 'habits'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    streak = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    category = relationship('Category', back_populates='habits')
    completions = relationship('Completion', back_populates='habit')

class Completion(Base):
    __tablename__ = 'completions'
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, default=datetime.now().date)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    habit_id = Column(Integer, ForeignKey('habits.id'))
    
    habit = relationship('Habit', back_populates='completions')

engine = create_engine('sqlite:///db/habit_tracker.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()