from flask import Flask, request, jsonify
from repositories.user_repository import UserRepository
from services.auth_service import AuthService
from services.session_service import SessionService
from database.db import init_db

app = Flask(__name__)

# Инициализация зависимостей
user_repo = UserRepository()
session_service = SessionService()
auth_service = AuthService(user_repo, session_service)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    if not auth_service.register(email, password):
        return jsonify({"error": "User already exists"}), 409
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    token = auth_service.login(email, password)
    if token:
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
