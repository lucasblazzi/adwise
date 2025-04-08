import logging
from pydantic_settings import BaseSettings


class Environment(BaseSettings):
    open_ai_api_key: str = "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"


logger = logging.getLogger("app")
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

env = Environment()
