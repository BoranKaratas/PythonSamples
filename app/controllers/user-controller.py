from flask import jsonify, request
from app.services.user_service import UserService

class UserController:
    @staticmethod
    def register():
        try:
            user_data = request.get_json()
            user = UserService.register_user(user_data)
            return jsonify(user), 201
        except ValueError as e:
            return jsonify({'message': str(e)}), 400