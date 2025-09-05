from lib.models import session, Category, Habit, Completion
from crud import get_all_categories, get_all_habits, get_completions_by_habit

def debug_data():
    print("=== DEBUG MODE ===")
    
    categories = get_all_categories()
    print(f"Categories: {len(categories)}")
    for cat in categories:
        print(f"  - {cat.name} (ID: {cat.id})")
    
    habits = get_all_habits()
    print(f"Habits: {len(habits)}")
    for habit in habits:
        print(f"  - {habit.name} (Streak: {habit.streak}, Category ID: {habit.category_id})")
    
    for habit in habits:
        completions = get_completions_by_habit(habit.id)
        print(f"Completions for '{habit.name}': {len(completions)}")
        for comp in completions:
            print(f"  - {comp.date}: {comp.notes or 'No notes'}")

if __name__ == "__main__":
    debug_data()