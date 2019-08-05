# Y2 CS Summer Starter Kit

This is the starter kit for the websites for the Y2 Summer 2019.

## Instructions:

To use this starter kit: **DO NOT FORK!**

```bash
git clone https://github.com/meet-projects/y2s19-d4-final.git
```

## File descriptions:

### `app.py`:

`app.py` contains all your Flask logic for app **routing and backend processing**.

### `databases.py`:

`databases.py` contains the database related functions (like adding items, querying, deleting, etc.). This is done for a more organized code.

### `model.py`:

`model.py` contains the schema, also known as **table structure**, of your database. You should define all the tables that you will need to use in your web app in this file. For example, you might create a `User` table here.

### `print_databases.py`:

`print_databases.py` is a helpful file that can display the items in your database for easier debugging! Example usage: `python print_databases.py project.db`

### `Procfile`:

`Procfile` provides the instructions Heroku needs to start the server. You do not need to change this.

### `requirements.txt`:

`requirements.txt` contains all the python libraries your app needs - such as Flask.