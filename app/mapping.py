# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.index
import app.controllers.error
endpoints = {
    "index": app.controllers.index.index,
    "notfound": app.controllers.error.notfound,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/", "index"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
