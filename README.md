# Habit Tracker CLI

A command-line interface application for tracking personal habits and building consistency.

## Features

- Create and manage habit categories
- Add new habits with descriptions
- Log daily habit completions
- View current streaks for each habit
- Track completion history
- Rich terminal interface with formatted output

## Installation

1. Clone the repository
2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   pipenv shell
   
   Usage
Initialize the database
bash

python -m lib.seed

Available Commands

    Add a category: python -m lib.main add-category

    Add a habit: python -m lib.main add-habit

    Log a completion: python -m lib.main log-habit

    View streak: python -m lib.main view-streak

    List categories: python -m lib.main list-categories

    List habits: python -m lib.main list-habits

    View completions: python -m lib.main view-completions

Example Workflow

    Create a category:
    bash

python -m lib.main add-category --name "Health & Wellness"

Add a habit:
bash

python -m lib.main add-habit --name "Drink water" --description "8 glasses daily" --category-id 1

Log a completion:
bash

python -m lib.main log-habit --habit-id 1 --notes "Stayed hydrated"

Check your streak:
bash

python -m lib.main view-streak --habit-id 1

Database Schema

The application uses SQLite with three main tables:

    categories: Habit categories (Health, Productivity, etc.)

    habits: Individual habits with streak tracking

    completions: Daily completion records

Development

Run the debug script to see current data:
bash

python -m lib.debug

Seed the database with sample data:
bash

python -m lib.seed

text


## 9. .gitignore

pycache/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
ENV/
env.bak/
venv.bak/
pipenv/
*.sqlite3
db/
.DS_Store
*.log
alembic.ini
text


## 10. alembic.ini

```ini
[alembic]
script_location = alembic
sqlalchemy.url = sqlite:///db/habit_tracker.db
file_template = %%(rev)s_%%(slug)s

[formatters]
keys = generic

[handlers]
keys = console

[logger_root]
level = WARN
handlers = console

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S

Setup Instructions

    Create the project structure:

bash

mkdir -p habit-tracker/lib/models
mkdir -p habit-tracker/db
cd habit-tracker

    Create all the files with the content above.

    Install dependencies:

bash

pipenv install
pipenv shell

    Initialize the database:

bash

python -m lib.seed

    Run the application:

bash

python -m lib.main --help

The application now meets all your requirements:

    ✅ Uses Pipenv for dependency management

    ✅ SQLAlchemy ORM with 3 related tables

    ✅ CLI with Click and Rich for beautiful output

    ✅ Proper package structure

    ✅ Data structures (lists, dicts, tuples)

    ✅ Input validation and user-friendly prompts

    ✅ Complete documentation in README.md