from flask import jsonify, request
from app.services.user_service import UserService
from bson import ObjectId

class UserController:
    @staticmethod
    def register():
        try:
            user_data = request.get_json()
            user = UserService.register_user(user_data)
            response = {
                "message": user_data["name"] + " - " +  "User registered successfully",
                "user_id": str(user.inserted_id)  # ObjectId'yi string'e çevir
            }
            return jsonify(response), 201
        except ValueError as e:
            return jsonify({'message': str(e)}), 400