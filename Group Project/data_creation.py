import mysql.connector
def setup_database():
    host = 'localhost'
    user = input('Enter the database user: ')
    password = input('Enter the database password: ')

    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        cursor = connection.cursor()

        database_name = input('Please enter the name of the database: ')
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
        print(f"Database '{database_name}' created successfully.")
        cursor.execute(f'USE {database_name}')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        ''')
        print("User table created successfully.")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS post (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                info TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(id)
            )
        ''')
        print("Post table created successfully.")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    setup_database()
