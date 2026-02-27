# scripts/reset_db.py
from models.base import Base, engine
from utils.db import init_db

def main():
    print("Dropping all tables...")
    Base.metadata.drop_all(engine)
    
    print("Creating tables with new schema...")
    init_db()
    
    print("Database reset complete!")

if __name__ == "__main__":
    main()