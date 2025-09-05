# Habit Tracker CLI

A command-line interface application for tracking personal habits and building consistency. This tool helps users create, manage, and monitor their daily habits with streak tracking and completion history.

## Features

- Create and manage habit categories
- Add new habits with descriptions
- Log daily habit completions
- View current streaks for each habit
- Track completion history with notes
- Beautiful terminal interface with formatted output
- SQLite database with proper migrations

---

## Prerequisites

- Python 3.8 or higher
- `pipenv` (Python package manager)
- Git

---

## Installation and Setup

### Clone the Repository

```bash
git clone [https://github.com/qalicha-dev28/habit_tracker.git](https://github.com/qalicha-dev28/habit_tracker.git)
cd habit-tracker

Set Up Virtual Environment and Dependencies

Bash

pipenv install
pipenv shell

Initialize Database with Alembic Migrations

Bash

# Create and apply initial migration
alembic revision --autogenerate -m "initial migration"
alembic upgrade head

Troubleshooting Migration Issues
If you encounter errors like "Target database is not up to date" during initial migration setup, run these commands to reset the database:

bash
# Remove the existing database
rm -rf db/

# Create new database directory and file
mkdir db
touch db/habit_tracker.db

# Now you can create new migrations
alembic revision --autogenerate -m "initial migration"
alembic upgrade head


Troubleshooting Migration Issues
If you encounter errors like "Target database is not up to date" during initial migration setup, run these commands to reset the database:

bash
# Remove the existing database
rm -rf db/

# Create new database directory and file
mkdir db
touch db/habit_tracker.db

# Now you can create new migrations
alembic revision --autogenerate -m "initial migration"
alembic upgrade head


Seed the Database with Sample Data (Optional)

Bash

python -m lib.seed

How to Use

Run the main script to access all available commands:
Bash

python -m lib.main --help

Available Commands

Manage Categories:

    add-category - Add a new habit category

    list-categories - List all categories

Manage Habits:

    add-habit - Add a new habit with description and category

    list-habits - List all habits with streaks and categories

Track Progress:

    log-habit - Log completion of a habit for today

    view-streak - View current streak for a habit

    view-completions - View completion history for a habit

Usage Examples

Bash

# Add a new category
python -m lib.main add-category --name "Health & Wellness"

# Add a new habit
python -m lib.main add-habit --name "Morning Run" --description "5km daily run" --category-id 1

# Log a completion
python -m lib.main log-habit --habit-id 1 --notes "Felt great today!"

# View streaks
python -m lib.main view-streak --habit-id 1

# List all habits
python -m lib.main list-habits

Project Structure

Plaintext

habit-tracker/
├── alembic/              # Alembic migration files
│   ├── versions/         # Migration scripts
│   └── env.py            # Migration environment
├── lib/
│   ├── models/           # SQLAlchemy database models
│   │   └── models.py     # Category, Habit, and Completion models
│   ├── crud.py           # CRUD operations and database queries
│   ├── main.py           # Main CLI application using Click and Rich
│   ├── seed.py           # Database seeding with sample data
│   └── __init__.py
├── db/                   # Database directory
├── alembic.ini           # Alembic configuration
├── Pipfile               # Dependencies: sqlalchemy, alembic, click, rich
├── Pipfile.lock
├── README.md
└── .gitignore

Database Schema

The application uses SQLite with three related tables:

    categories: id, name, created_at

    habits: id, name, description, streak, created_at, category_id (FK)

    completions: id, date, notes, created_at, habit_id (FK)

Dependencies

    SQLAlchemy - ORM for database management

    Alembic - Database migrations

    Click - CLI interface

    Rich - Beautiful terminal formatting

    python-dotenv - Environment variable management

Author

    Name: Najma Boru

    GitHub: qalicha-dev28




License

This project is licensed under the MIT License.










