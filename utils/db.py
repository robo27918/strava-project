from contextlib import contextManger
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.base import SessionLocal,engine,Base

@contextManger
def get_db_session():
    """
        usage:
            with get_db_session() as session
                session.add(___)
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print("Error: ",e)
        raise
    finally:
        session.close()
def init_db():
    """
    Initialize database 
    Should be called once at start of app
    """
    try:
        Base.metadata.create_all(bind=engine)
        print("Datatbase tables created successfully")
    except SQLAlchemyError as e:
        print("Error setting connection to database", e)
        raise
# def check_connection