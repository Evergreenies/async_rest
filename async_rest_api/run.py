from aiohttp import web
from async_rest_api.async_app import app, run_configurations

if __name__ == '__main__':
    web.run_app(app=app, **run_configurations)
