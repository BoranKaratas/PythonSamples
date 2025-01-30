from app.models.user import User

class UserRepository:
    @staticmethod
    def create_user(user_data):
        return User.create(user_data)

    @staticmethod
    def find_user_by_email(email):
        return User.find_by_email(email)