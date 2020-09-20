import jwt

from aiohttp import web
from aiohttp_jwt import JWTMiddleware

secret = 'secret'

middlewares = [
    JWTMiddleware(secret)
]

app = web.Application(
    middlewares=middlewares
)

run_configurations = {
    'host': '127.0.0.1',
    'port': 9090
}

from async_rest_api.async_app import routers

