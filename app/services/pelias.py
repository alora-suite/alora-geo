import httpx
from app.core.config import settings

async def query_pelias(query: str):
    async with httpx.AsyncClient() as client:
        url = f"{settings.PELIAS_URL}/v1/search?text={query}"
        res = await client.get(url)
        if res.status_code == 200:
            data = res.json()
            if data.get("features"):
                return data["features"][0]
    return None