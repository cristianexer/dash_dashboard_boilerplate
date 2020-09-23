
from dotenv import load_dotenv
import os
from types import SimpleNamespace


def settings():
    load_dotenv(verbose=True)
    ns = dict(
        APP_NAME=os.getenv('APP_NAME', 'DASH Dashboard Template'),
        APP_PORT=os.getenv('APP_PORT', 3000),
        APP_DEBUG=os.getenv('APP_DEBUG', True),
        APP_THREADED=os.getenv('APP_THREADED', True)
    )

    return SimpleNamespace(**ns)
