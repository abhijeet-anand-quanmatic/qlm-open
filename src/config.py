import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), ".env")
    )

    DWAVE_API_TOKEN: str = ""
    FIXSTARS_API_TOKEN: str = ""
    QUPIT_API_TOKEN: str = ""
