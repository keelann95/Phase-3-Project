from models import initialize_database

def create_tables():
    initialize_database()
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()