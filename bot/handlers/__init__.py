from aiogram import Router

from .admin import router as router_admin
from .start_handlers import router as router_other
from .user import router as router_user

router = Router(name=__name__)

router.include_routers(
    router_admin,
    router_user,
    router_other,
)

__all__ = ("router")