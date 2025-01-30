from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def register_user(user_data):
        existing_user = UserRepository.find_user_by_email(user_data['email'])
        if existing_user:
            raise ValueError('Bu e-posta zaten kullanılıyor.')
        return UserRepository.create_user(user_data)