from lib.models import Category, Habit, Completion, session
from datetime import datetime, timedelta

def seed_data():
    session.query(Completion).delete()
    session.query(Habit).delete()
    session.query(Category).delete()
    session.commit()
    
    health_category = Category(name="Health & Wellness")
    productivity_category = Category(name="Productivity")
    personal_category = Category(name="Personal Development")
    
    session.add_all([health_category, productivity_category, personal_category])
    session.commit()
    
    water_habit = Habit(
        name="Drink 8 glasses of water",
        description="Stay hydrated throughout the day",
        category_id=health_category.id
    )
    
    exercise_habit = Habit(
        name="30 minutes exercise",
        description="Daily physical activity",
        category_id=health_category.id
    )
    
    reading_habit = Habit(
        name="Read 20 pages",
        description="Daily reading habit",
        category_id=personal_category.id
    )
    
    session.add_all([water_habit, exercise_habit, reading_habit])
    session.commit()
    
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    
    water_completion1 = Completion(habit_id=water_habit.id, date=yesterday)
    water_completion2 = Completion(habit_id=water_habit.id, date=today)
    
    exercise_completion = Completion(habit_id=exercise_habit.id, date=today)
    
    session.add_all([water_completion1, water_completion2, exercise_completion])
    session.commit()
    
    water_habit.streak = 2
    exercise_habit.streak = 1
    session.commit()
    
    print("Seed data created successfully!")

if __name__ == "__main__":
    seed_data()
