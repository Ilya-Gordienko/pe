from database.db import SessionLocal
from models.user import User

class UserRepository:
    def find_by_email(self, email: str):
        db = SessionLocal()
        try:
            return db.query(User).filter(User.email == email).first()
        finally:
            db.close()

    def save(self, user: User):
        db = SessionLocal()
        try:
            db.add(user)
            db.commit()
        finally:
            db.close()
