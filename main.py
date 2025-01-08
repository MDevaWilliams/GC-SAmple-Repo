import os
def connect_to_db():
    db_user = os.getenv('DB_USER', 'default_user')
    db_pass = os.getenv('DB_PASS', 'default_pass')
    print(f"Connecting to database with user: {db_user}")
if __name__ == "__main__":
    connect_to_db()
