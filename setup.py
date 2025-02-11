from database.database import engine, Base, SessionLocal

Base.metadata.create_all(engine)


# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()