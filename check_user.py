from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import User

SQLALCHEMY_DATABASE_URL = "sqlite:///./purchase_system.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

user = db.query(User).filter(User.email == 'azozhero54@gmail.com').first()
if user:
    print(f"Found user: {user.username}, email: {user.email}")
else:
    print("User not found")
db.close()
