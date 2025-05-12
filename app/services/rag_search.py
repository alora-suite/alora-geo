from elasticsearch import Elasticsearch
from app.core.config import settings

es = Elasticsearch(settings.ELASTIC_URL)

def search_rag(query: str):
    res = es.search(index="geo_locations", query={"match": {"name": query}})
    hits = res.get("hits", {}).get("hits", [])
    if hits:
        return hits[0]["_source"]
    return None