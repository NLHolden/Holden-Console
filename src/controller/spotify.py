import spotipy
from spotipy.oauth2 import SpotifyOAuth

from controller.model import SpotifyTrack

class SpotifyClient:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
    ) -> None:
        self._client = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="user-read-currently-playing",
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
            )
        )

    def get_current_track(self) -> SpotifyTrack | None:
        current = self._client.current_user_playing_track()

        if current is None or current["item"] is None:
            return None

        track = current["item"]
        if track.get("type") != "track":
            return None

        return SpotifyTrack(
            name=track["name"],
            artist=[artist["name"] for artist in track["artists"]],
            duration_ms=track["duration_ms"],
        )

    def get_playback_progress(self) -> int:
        current = self._client.current_user_playing_track()

        if current is None or current["item"] is None:
            return None

        return current.get("progress_ms") or 0