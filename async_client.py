import aiohttp
import asyncio
import async_timeout


async def fetch(session, url, headers=None):
    async with async_timeout.timeout(10):
        async with session.get(url, headers=headers) as response:
            return await response.json()


async def async_main():
    async with aiohttp.ClientSession() as session:
        response = await fetch(
            session,
            'http://127.0.0.1:9090/',
            headers={
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.pyNsXX_vNsUvdt6xu13F1Gs1zGELT4Va8a38eG5svBA'
            }
        )
        print(response)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())
