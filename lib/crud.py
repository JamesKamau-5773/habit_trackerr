from lib.models import session, Category, Habit, Completion
from datetime import datetime

def create_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    return category

def get_all_categories():
    return session.query(Category).order_by(Category.name).all()

def create_habit(name, description, category_id):
    habit = Habit(name=name, description=description, category_id=category_id)
    session.add(habit)
    session.commit()
    return habit

def get_all_habits():
    return session.query(Habit).order_by(Habit.name).all()

def get_habit_by_id(habit_id):
    return session.query(Habit).filter(Habit.id == habit_id).first()

def log_completion(habit_id, notes=''):
    completion = Completion(habit_id=habit_id, notes=notes)
    session.add(completion)
    habit = get_habit_by_id(habit_id)
    if habit:
        habit.streak += 1
    session.commit()
    return completion

def get_habit_streak(habit_id):
    habit = get_habit_by_id(habit_id)
    return habit.streak if habit else 0