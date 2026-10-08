from typing import Any


class FakeSpotipyClient:
    """Small controllable stand-in for Spotipy's Spotify client."""

    def __init__(self) -> None:
        self.current_playback: dict[str, Any] | None = None

    def set_current_track(
        self,
        name: str,
        artists: list[str],
        duration_ms: int,
        progress_ms: int = 0,
        is_playing: bool = True,
    ) -> None:
        self.current_playback = {
            "item": {
                "type": "track",
                "name": name,
                "artists": [{"name": artist} for artist in artists],
                "duration_ms": duration_ms,
            },
            "progress_ms": progress_ms,
            "is_playing": is_playing,
        }

    def clear_playback(self) -> None:
        self.current_playback = None

    def current_user_playing_track(self) -> dict[str, Any] | None:
        return self.current_playback
