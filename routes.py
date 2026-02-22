# pylint: disable=W0212

import logging

import aiohttp_jinja2
from aiohttp import web
from aiohttp.web_routedef import RouteDef

from tgfs.config import Config
from tgfs.database import DB
from tgfs.routes import routes
from tgfs.utils.utils import human_bytes, parse_token

log = logging.getLogger(__name__)

conflicting_paths = [
    "/wt/{payload}/{sig}",
    "/group/{payload}/{sig}"
]

for route in routes:
    route: RouteDef
    if route.path in conflicting_paths:
        log.debug("Removed %s path", route.path)
        routes._items.remove(route)

@routes.get("/wt/{payload}/{sig}")
async def handle_watch_request(req: web.Request) -> web.Response:
    payload = req.match_info["payload"]
    sig = req.match_info["sig"]
    pt = parse_token(payload, sig)
    if not pt:
        return web.Response(status=404, text="File not found")
    user_id, file_id = pt

    file = await DB.db.get_file(file_id, user_id)
    if not file:
        return web.Response(status=404, text="File not found")

    return aiohttp_jinja2.render_template("watch.html", req, {
        "id": file.id,
        "dc_id": file.dc_id,
        "file_size": human_bytes(file.file_size),
        "mime_type": file.mime_type,
        "file_name": file.file_name,
        "url": f"{Config.PUBLIC_URL}/dl/{payload}/{sig}",
        "user_id": user_id,
        "tag": file.mime_type.split('/')[0].strip(),
    })

@routes.get("/group/{payload}/{sig}")
async def handle_group_request(req: web.Request) -> web.Response:
    payload = req.match_info["payload"]
    sig = req.match_info["sig"]
    pt = parse_token(payload, sig)
    if not pt:
        return web.Response(status=404, text="File not found")
    user_id, group_id = pt
    group = await DB.db.get_group(group_id, user_id)
    if group is None:
        return web.Response(status=404, text="Group not found")
    files = [file async for file in DB.db.get_files2(user_id, group.files, full=True)]
    return aiohttp_jinja2.render_template("group.html", req, {
        "group": group,
        "files": files,
        "public_url": Config.PUBLIC_URL
    })
