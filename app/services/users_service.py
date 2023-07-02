from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user_data):
        return self.user_repository.create(user_data)

    def get_all_users(self):
        return self.user_repository.get_all()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def update_user(self, user, user_data):
        self.user_repository.update(user, user_data)

    def delete_user(self, user):
        self.user_repository.delete(user)
