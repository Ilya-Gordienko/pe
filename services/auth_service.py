from repositories.user_repository import UserRepository
from services.session_service import SessionService
from utils.password_utils import hash_password, verify_password
from models.user import User

class AuthService:
    def __init__(self, user_repo: UserRepository, session_service: SessionService):
        self.user_repo = user_repo
        self.session_service = session_service

    def register(self, email: str, password: str) -> bool:
        if self.user_repo.find_by_email(email):
            return False
        user = User(email=email, password_hash=hash_password(password))
        self.user_repo.save(user)
        return True

    def login(self, email: str, password: str):
        user = self.user_repo.find_by_email(email)
        if not user or not verify_password(password, user.password_hash):
            return None
        return self.session_service.create_session(user.id)
