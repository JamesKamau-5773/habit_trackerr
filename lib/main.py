import sys
sys.path.insert(0, '/home/james/clas-practice-folders/code/se-prep/habit_tracker')

import click
from rich.console import Console
from rich.table import Table
from lib.crud import *

console = Console()

def display_categories():
    categories = get_all_categories()
    if not categories:
        console.print("No categories found")
        return
    
    table = Table(title="Habit Categories", show_header=True)
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Created")
    
    for category in categories:
        table.add_row(
            str(category.id),
            category.name,
            category.created_at.strftime("%Y-%m-%d")
        )
    
    console.print(table)

def display_habits():
    habits = get_all_habits()
    if not habits:
        console.print("No habits found")
        return
    
    table = Table(title="Your Habits", show_header=True)
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Category")
    table.add_column("Streak")
    
    for habit in habits:
        table.add_row(
            str(habit.id),
            habit.name,
            habit.category.name,
            str(habit.streak)
        )
    
    console.print(table)

def add_category_menu():
    console.print("Add a new habit category")
    name = input("Enter the category name: ")
    create_category(name)
    console.print("Category added successfully")

def add_habit_menu():
    console.print("Add a new habit")
    display_categories()
    name = input("Enter the habit name: ")
    description = input("Enter the habit description: ")
    category_id = int(input("Enter the category ID: "))
    create_habit(name, description, category_id)
    console.print("Habit added successfully")

def log_completion_menu():
    console.print("Log completion of a habit")
    display_habits()
    habit_id = int(input("Enter the habit ID: "))
    notes = input("Enter any notes: ")
    log_completion(habit_id, notes)
    console.print("Completion logged successfully")

def view_streak_menu():
    console.print("View current streak for a habit")
    display_habits()
    habit_id = int(input("Enter the habit ID: "))
    streak = get_habit_streak(habit_id)
    console.print(f"Current streak for habit {habit_id}: {streak} days")

@click.command()
def main_menu():
    while True:
        console.print("Habit Tracker CLI")
        console.print("Select an option:")
        console.print("[1] Add a new habit category")
        console.print("[2] Add a new habit")
        console.print("[3] Log completion of a habit")
        console.print("[4] View current streak for a habit")
        console.print("[5] View all categories")
        console.print("[6] View all habits")
        console.print("[7] Quit")

        option = input("Enter your choice: ")

        if option == "1":
            add_category_menu()
        elif option == "2":
            add_habit_menu()
        elif option == "3":
            log_completion_menu()
        elif option == "4":
            view_streak_menu()
        elif option == "5":
            display_categories()
        elif option == "6":
            display_habits()
        elif option == "7":
            console.print("Goodbye")
            break
        else:
            console.print("Invalid option")

if __name__ == "__main__":
    main_menu()