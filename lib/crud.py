from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func, and_
from datetime import datetime, date, timedelta
from lib.models.models import Category, Habit, Completion, session

def create_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    return category

def create_habit(name, description, category_id):
    habit = Habit(name=name, description=description, category_id=category_id)
    session.add(habit)
    session.commit()
    return habit

def log_completion(habit_id, notes=None):
    today = date.today()
    existing_completion = session.query(Completion).filter(
        and_(Completion.habit_id == habit_id, Completion.date == today)
    ).first()
    
    if existing_completion:
        return existing_completion
    
    completion = Completion(habit_id=habit_id, notes=notes, date=today)
    session.add(completion)
    
    habit = session.query(Habit).filter(Habit.id == habit_id).first()
    if habit:
        habit.streak += 1
    
    session.commit()
    return completion

def get_habit_streak(habit_id):
    habit = session.query(Habit).filter(Habit.id == habit_id).first()
    return habit.streak if habit else 0

def get_all_categories():
    return session.query(Category).all()

def get_all_habits():
    return session.query(Habit).all()

def get_habits_by_category(category_id):
    return session.query(Habit).filter(Habit.category_id == category_id).all()

def get_completions_by_habit(habit_id):
    return session.query(Completion).filter(Completion.habit_id == habit_id).all()

def get_habit_by_id(habit_id):
    return session.query(Habit).filter(Habit.id == habit_id).first()

def get_category_by_id(category_id):
    return session.query(Category).filter(Category.id == category_id).first()
