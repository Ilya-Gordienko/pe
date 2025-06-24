import pytest
from services.auth_service import AuthService
from services.session_service import SessionService
from models.user import User

# Фейковый репозиторий
class FakeUserRepo:
    def __init__(self):
        self.users = {}

    def find_by_email(self, email):
        return self.users.get(email)

    def save(self, user):
        self.users[user.email] = user

@pytest.fixture
def auth_service():
    repo = FakeUserRepo()
    session = SessionService()
    return AuthService(repo, session), repo

def test_register_new_user(auth_service):
    service, _ = auth_service
    assert service.register("user@example.com", "123")

def test_register_existing_user(auth_service):
    service, _ = auth_service
    service.register("user@example.com", "123")
    assert not service.register("user@example.com", "123")

def test_login_success(auth_service):
    service, _ = auth_service
    service.register("user@example.com", "123")
    assert service.login("user@example.com", "123")

def test_login_failure(auth_service):
    service, _ = auth_service
    assert not service.login("notfound@example.com", "123")

# интеграционный тест: проверка, что создаётся токен и сохраняется сессия
def test_session_token_created_on_login(auth_service):
    service, _ = auth_service
    service.register("test@example.com", "pass")
    token = service.login("test@example.com", "pass")
    assert token in service.session_service.sessions
