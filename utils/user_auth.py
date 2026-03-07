import sqlite3
import os

# Hardcoded secret (security issue)
SECRET_KEY = "my_super_secret_password_123"


def connect_db():
    # No error handling
    conn = sqlite3.connect("users.db")
    return conn


def get_user(username):
    conn = connect_db()
    cursor = conn.cursor()

    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchone()


def login(username, password):
    user = get_user(username)

    # Bug: no proper validation
    if user and user[2] == password:
        print("Login successful")
        return True
    else:
        print("Login failed")
        return False


def delete_user_file(filename):
    # Path traversal vulnerability
    file_path = "/tmp/" + filename

    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted")


def inefficient_search(items, target):
    # Inefficient algorithm (bad practice)
    for i in range(len(items)):
        for j in range(len(items)):
            if items[j] == target:
                return j
    return -1


if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    login(username, password)

    # Unused variable (code smell)
    temp_value = 12345
    print(temp_value)
