from pathlib import Path

from pydantic import BaseModel, Field


class UIConfig(BaseModel):
    width: int = Field(gt=0)
    height: int = Field(gt=0)
    title: str
    dark_theme: bool
    favicon_path: Path
    start_screen_path: Path
    start_screen_duration_seconds: float = Field(gt=0)


class SpotifyConfig(BaseModel):
    client_id: str
    client_secret: str
    redirect_uri: str


class ObsConfig(BaseModel):
    host: str
    port: int = Field(ge=1, le=65535)
    password: str


class ConsoleConfig(BaseModel):
    ui: UIConfig
    spotify: SpotifyConfig
    obs: ObsConfig
