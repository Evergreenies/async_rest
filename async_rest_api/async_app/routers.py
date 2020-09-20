from async_rest_api.async_app import app

from aiohttp import web
from async_rest_api.async_app.views import resource_1, resource_2

routes = [
    web.get('/', resource_1),
    web.post('/', resource_1),
    web.get('/home', resource_2),
]

app.add_routes(routes)
