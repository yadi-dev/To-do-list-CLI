# To-do List with CLI
A command-line interface (CLI) application for managing your to-do list using Python and MySQL.
## Setup
### Prerequisites
- Python 3.x
- MySQL Server
### Installation
1. Clone this repository:
   ```
   git clone https://github.com/yadi-dev/To-do-list-CLI.git
   cd To-do-list-CLI
   ```
2. Install the required Python packages:
   ```
   pip install mysql-connector-python
   ```
3. Set up your MySQL database:
   ```sql
   mysql -u root -p
   CREATE DATABASE todolist_db;
   USE todolist_db;
   CREATE TABLE tasks (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       description TEXT,
       due_date DATE,
       is_completed BOOLEAN DEFAULT FALSE,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```
## Run
   ```
   python todolist.py
   ```
## Features
- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- [Add any other features your application has]
## Project Structure
- `todolist.py`: Main application file
- `db.py`: Database connection and operations
