
import sqlite3

def get_user(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # SECURE: Parameterized SQL query
    query = "SELECT * FROM users WHERE username = ?"

    cursor.execute(query, (username,))

    result = cursor.fetchall()

    connection.close()

    return result


if __name__ == "__main__":
    get_user("admin")
