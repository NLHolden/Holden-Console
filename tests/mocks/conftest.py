import pytest

from controller.spotify import SpotifyClient
from tests.mocks.fake_spotify import FakeSpotipyClient


@pytest.fixture
def fake_spotify() -> FakeSpotipyClient:
    return FakeSpotipyClient()


@pytest.fixture
def spotify_client(fake_spotify: FakeSpotipyClient) -> SpotifyClient:
    return SpotifyClient(
        client_id="test-client-id",
        client_secret="test-client-secret",
        redirect_uri="http://localhost/callback",
        spotify_api=fake_spotify,
    )
