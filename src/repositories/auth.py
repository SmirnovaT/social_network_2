from src.models.user import User

from src.core.config import bcrypt_context
from src.repositories.base_repository import BaseRepository


class CreateUserRepository(BaseRepository):
    def creat_new_user(self, create_user):
        create_user_model = User()
        create_user_model.email = create_user.email
        create_user_model.username = create_user.username
        create_user_model.first_name = create_user.first_name
        create_user_model.last_name = create_user.last_name
        create_user_model.phone_number = create_user.phone_number

        hash_password = _get_password_hash(create_user.password)

        create_user_model.password = hash_password

        self.db.add(create_user_model)
        self.db.commit()
        return create_user_model


def _get_password_hash(password):
    return bcrypt_context.hash(password)