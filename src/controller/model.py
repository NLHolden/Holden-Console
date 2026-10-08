from pydantic import BaseModel, Field


class SpotifyTrack(BaseModel):
    name: str
    artist: list[str]
    duration_ms : int = Field(gt=0)
