import httpx
from app.core.config import settings

async def normalize_location(query: str) -> str:
    payload = {
        "prompt": f"Normalize this location input: {query}",
        "max_tokens": 128,
        "use_chat_format": False
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{settings.LLAMA_ENDPOINT}/raw", json=payload)
        res.raise_for_status()
        return res.json().get("response", query).strip()