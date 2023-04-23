from app.interfaces.base_repository import IBaseRepository
from app.repositories.user_repository import UserRepository
from app.services.base_service import BaseService


class UserService(BaseService):
    def __init__(self, user_repository: IBaseRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)
