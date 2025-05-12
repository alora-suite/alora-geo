from pydantic import BaseSettings

class Settings(BaseSettings):
    LLAMA_ENDPOINT: str = "http://llama.dev01.apibox.link"
    REDIS_HOST: str = "host.docker.internal"
    ELASTIC_URL: str = "http://localhost:9200"
    PELIAS_URL: str = "http://localhost:4000"

    class Config:
        env_file = ".env"

settings = Settings()