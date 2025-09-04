# Clase User y funciones relacionadas

class User:
    def __init__(self, user_id, email, password):
        self.user_id = user_id
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.user_id,
            "email": self.email,
            "password": self.password
        }
