from models import initialize_database
from models.group import Group

def seed():
    initialize_database()
    Group.create("Family")
    Group.create("Friends")
    Group.create("Work")
    print("Database seeded successfully.")

if __name__ == "__main__":
    seed()