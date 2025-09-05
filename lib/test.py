from lib.models.models import session, Habit, Category, Completion
from lib.crud import create_habit, get_habit_by_name, get_all_habits, log_completion, calculate_streak, delete_habit
import datetime

def run_tests():
    print("Running tests...")

    session.query(Completion).delete()
    session.query(Habit).delete()
    session.query(Category).delete()
    session.commit()

    print("Test 1: Creating a new habit...")
    new_habit = create_habit('Exercise', 'Go for a run or walk', 'Fitness')
    assert new_habit is not None
    assert new_habit.name == 'Exercise'
    print("Test 1 passed.")

    print("Test 2: Retrieving habit by name...")
    retrieved_habit = get_habit_by_name('Exercise')
    assert retrieved_habit is not None
    assert retrieved_habit.name == 'Exercise'
    print("Test 2 passed.")

    print("Test 3: Logging completion for a habit...")
    success, message = log_completion(retrieved_habit.id)
    assert success is True
    assert message == 'Completion logged successfully.'
    print("Test 3 passed.")

    print("Test 4: Checking streak after one completion...")
    streak = calculate_streak(retrieved_habit.id)
    assert streak == 1
    print("Test 4 passed.")

    print("Test 5: Attempting to log completion for the same day...")
    success, message = log_completion(retrieved_habit.id)
    assert success is False
    assert message == 'Habit already completed for today.'
    print("Test 5 passed.")

    print("Test 6: Deleting a habit...")
    delete_success = delete_habit(retrieved_habit.id)
    assert delete_success is True
    deleted_habit = get_habit_by_name('Exercise')
    assert deleted_habit is None
    print("Test 6 passed.")

    print("\nAll tests passed successfully!")

if __name__ == '__main__':
    run_tests()