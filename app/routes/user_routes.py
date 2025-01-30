from flask import Blueprint
from app.controllers.user_controller import UserController

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    return UserController.register()