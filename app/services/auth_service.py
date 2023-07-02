from app.repositories.auth_repository import AuthRepository


class AuthService:
    @staticmethod
    def login(email, password):
        user = AuthRepository.find_by_email(email)
        if user and user.password == password:
            # Implementar a lógica de autenticação aqui
            return True
        return False

    @staticmethod
    def logout():
        # Implementar a lógica de logout aqui
        pass
