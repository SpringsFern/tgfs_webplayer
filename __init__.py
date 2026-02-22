import logging
from pathlib import Path

import jinja2
import aiohttp_jinja2
from aiohttp import web

from tgfs.app import init_handlers
from tgfs.config import Config
from tgfs.utils.utils import human_bytes, make_token
from . import routes

path = Path(__file__).parent

log = logging.getLogger(__name__)

def init_jinja2(app: web.Application) -> None:
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(path / 'templates')
    )
    aiohttp_jinja2.get_env(app).globals["human_bytes"] = human_bytes
    aiohttp_jinja2.get_env(app).globals["make_token"] = make_token
    aiohttp_jinja2.get_env(app).globals["Config"] = Config
    log.debug("Jinja2 setup done")

init_handlers.append(init_jinja2)
