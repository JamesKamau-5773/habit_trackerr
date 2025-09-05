import click
from rich.console import Console
from rich.table import Table
from lib.crud import (
    create_category, create_habit, log_completion, get_habit_streak,
    get_all_categories, get_all_habits, get_habits_by_category,
    get_completions_by_habit, get_habit_by_id, get_category_by_id
)

console = Console()

@click.group()
def cli():
    """Habit Tracker CLI - Manage your daily habits"""
    pass

@cli.command()
@click.option('--name', prompt='Category name', help='Name of the category')
def add_category(name):
    """Add a new habit category"""
    category = create_category(name)
    console.print(f"[green]Category '{category.name}' created successfully![/green]")

@cli.command()
@click.option('--name', prompt='Habit name', help='Name of the habit')
@click.option('--description', prompt='Habit description', help='Description of the habit')
@click.option('--category-id', prompt='Category ID', type=int, help='ID of the category')
def add_habit(name, description, category_id):
    """Add a new habit"""
    habit = create_habit(name, description, category_id)
    console.print(f"[green]Habit '{habit.name}' created successfully![/green]")

@cli.command()
@click.option('--habit-id', prompt='Habit ID', type=int, help='ID of the habit')
@click.option('--notes', default='', help='Notes for the completion')
def log_habit(habit_id, notes):
    """Log completion of a habit for today"""
    completion = log_completion(habit_id, notes)
    console.print(f"[green]Habit completion logged for {completion.date}![/green]")

@cli.command()
@click.option('--habit-id', prompt='Habit ID', type=int, help='ID of the habit')
def view_streak(habit_id):
    """View current streak for a habit"""
    streak = get_habit_streak(habit_id)
    habit = get_habit_by_id(habit_id)
    if habit:
        console.print(f"[yellow]Current streak for '{habit.name}': {streak} days[/yellow]")
    else:
        console.print("[red]Habit not found![/red]")

@cli.command()
def list_categories():
    """List all categories"""
    categories = get_all_categories()
    table = Table(title="Categories")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Created At", style="green")
    
    for category in categories:
        table.add_row(str(category.id), category.name, str(category.created_at))
    
    console.print(table)

@cli.command()
def list_habits():
    """List all habits"""
    habits = get_all_habits()
    table = Table(title="Habits")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Description", style="yellow")
    table.add_column("Streak", style="green")
    table.add_column("Category", style="blue")
    
    for habit in habits:
        category = get_category_by_id(habit.category_id)
        table.add_row(
            str(habit.id), 
            habit.name, 
            habit.description or "", 
            str(habit.streak),
            category.name if category else "Unknown"
        )
    
    console.print(table)

@cli.command()
@click.option('--habit-id', prompt='Habit ID', type=int, help='ID of the habit')
def view_completions(habit_id):
    """View completion history for a habit"""
    completions = get_completions_by_habit(habit_id)
    habit = get_habit_by_id(habit_id)
    
    if habit:
        table = Table(title=f"Completions for '{habit.name}'")
        table.add_column("Date", style="cyan")
        table.add_column("Notes", style="magenta")
        table.add_column("Created At", style="green")
        
        for completion in completions:
            table.add_row(str(completion.date), completion.notes or "", str(completion.created_at))
        
        console.print(table)
    else:
        console.print("[red]Habit not found![/red]")

if __name__ == '__main__':
    cli()
