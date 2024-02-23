import requests
import argparse

def fetch_todo(todo_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{todo_id}')
    return response.json()

def fetch_even_todos():
    even_todos = []
    for i in range(2, 42, 2):  # Fetching the first 20 even numbered TODOs
        todo = fetch_todo(i)
        even_todos.append(todo)
    return even_todos

def display_todos(todos):
    for todo in todos:
        title = todo['title']
        completed = todo['completed']
        print(f"Title: {title} - Completed: {'Yes' if completed else 'No'}")

def main():
    parser = argparse.ArgumentParser(description='Fetch and display first 20 even numbered TODOs')
    parser.parse_args()

    even_todos = fetch_even_todos()
    display_todos(even_todos)

if __name__ == "__main__":
    main()
