from aiogram import Router

from .admin import router as router_admin


router = Router(name=__name__)

router.include_routers(
    router_admin,
)

__all__ = ("router")