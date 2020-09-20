from aiohttp.web import json_response


async def resource_1(request):
    print(request.get('payload'))
    return json_response(request.get('payload'))


async def resource_2(request):
    print(request.get('payload'))
    return json_response(request.get('payload'))
