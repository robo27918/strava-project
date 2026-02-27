# scripts/reset_db.py
from models.base import Base, engine
from utils.db import init_db
import models.summary_activity
#this doesnt actually do anything
#because it doesnt get the key for the 
def main():
    print("Dropping all tables...")
    Base.metadata.drop_all(engine)
    print(Base.metadata.tables.keys())  # shows all tables it knows about 
    print("Creating tables with new schema...")
    init_db()
    
    print("Database reset complete!")

if __name__ == "__main__":
    main()