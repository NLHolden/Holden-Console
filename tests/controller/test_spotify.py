from controller.model import SpotifyTrack
from controller.spotify import SpotifyClient
from tests.mocks.fake_spotify import FakeSpotipyClient


def test_get_current_track_returns_track_details(
    fake_spotify: FakeSpotipyClient,
    spotify_client: SpotifyClient,
) -> None:
    fake_spotify.set_current_track(
        name="The Example Song",
        artists=["Example Artist", "Guest Artist"],
        duration_ms=210_000,
        progress_ms=42_000,
    )

    assert spotify_client.get_current_track() == SpotifyTrack(
        name="The Example Song",
        artist=["Example Artist", "Guest Artist"],
        duration_ms=210_000,
    )


def test_get_current_track_returns_none_when_nothing_is_playing(
    fake_spotify: FakeSpotipyClient,
    spotify_client: SpotifyClient,
) -> None:
    fake_spotify.clear_playback()

    assert spotify_client.get_current_track() is None


def test_get_playback_progress_returns_position_ms(
    fake_spotify: FakeSpotipyClient,
    spotify_client: SpotifyClient,
) -> None:
    fake_spotify.set_current_track(
        name="The Example Song",
        artists=["Example Artist"],
        duration_ms=210_000,
        progress_ms=42_000,
    )

    assert spotify_client.get_playback_progress() == 42_000


def test_get_playback_progress_returns_none_when_nothing_is_playing(
    fake_spotify: FakeSpotipyClient,
    spotify_client: SpotifyClient,
) -> None:
    fake_spotify.clear_playback()

    assert spotify_client.get_playback_progress() is None
