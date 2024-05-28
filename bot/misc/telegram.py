from os import environ
from typing import Final

class TgKey:
    TOKEN: Final = environ.get('TOKEN')