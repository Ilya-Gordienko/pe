from utils.password_utils import hash_password, verify_password

def test_hash_password_returns_string():
    assert isinstance(hash_password("abc123"), str)

def test_password_verification_success():
    password = "abc123"
    hashed = hash_password(password)
    assert verify_password(password, hashed)

def test_password_verification_failure():
    hashed = hash_password("abc123")
    assert not verify_password("wrongpass", hashed)
