from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llama_client import normalize_location
from app.services.rag_search import search_rag
from app.services.pelias import query_pelias
from app.services.cache import get_cached_location, set_cached_location

router = APIRouter()

class GeocodeRequest(BaseModel):
    query: str

@router.post("/geocode")
async def geocode(req: GeocodeRequest):
    normalized = await normalize_location(req.query)
    cached = await get_cached_location(normalized)
    if cached:
        return {"source": "cache", "result": cached}
    
    rag_result = search_rag(normalized)
    if rag_result:
        await set_cached_location(normalized, rag_result)
        return {"source": "rag", "result": rag_result}
    
    pelias_result = await query_pelias(normalized)
    if pelias_result:
        await set_cached_location(normalized, pelias_result)
        return {"source": "pelias", "result": pelias_result}
    
    raise HTTPException(status_code=404, detail="Location not found")