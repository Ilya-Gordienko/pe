import uuid

class SessionService:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id: int) -> str:
        token = str(uuid.uuid4())
        self.sessions[token] = user_id
        return token

    def get_user_by_token(self, token: str):
        return self.sessions.get(token)
