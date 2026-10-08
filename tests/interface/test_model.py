from pathlib import Path

from interface.model import ConsoleConfig, ObsConfig, SpotifyConfig, UIConfig


def test_ui_config_json_round_trip() -> None:
    config = UIConfig(
        width=1100,
        height=700,
        title="Holden Console",
        dark_theme=True,
        favicon_path=Path("assets/images/favicon.ico"),
        start_screen_path=Path("assets/images/start_screen.png"),
        start_screen_duration_seconds=3,
    )

    restored = UIConfig.model_validate_json(config.model_dump_json())

    assert restored == config


def test_spotify_config_json_round_trip() -> None:
    config = SpotifyConfig(
        client_id="client-id",
        client_secret="client-secret",
        redirect_uri="http://localhost:8888/callback",
    )

    restored = SpotifyConfig.model_validate_json(config.model_dump_json())

    assert restored == config


def test_obs_config_json_round_trip() -> None:
    config = ObsConfig(host="127.0.0.1", port=4455, password="obs-password")

    restored = ObsConfig.model_validate_json(config.model_dump_json())

    assert restored == config


def test_console_config_json_round_trip() -> None:
    config = ConsoleConfig(
        ui=UIConfig(
            width=1100,
            height=700,
            title="Holden Console",
            dark_theme=True,
            favicon_path=Path("assets/images/favicon.ico"),
            start_screen_path=Path("assets/images/start_screen.png"),
            start_screen_duration_seconds=3,
        ),
        spotify=SpotifyConfig(
            client_id="client-id",
            client_secret="client-secret",
            redirect_uri="http://localhost:8888/callback",
        ),
        obs=ObsConfig(host="127.0.0.1", port=4455, password="obs-password"),
    )

    restored = ConsoleConfig.model_validate_json(config.model_dump_json())

    assert restored == config
    assert isinstance(restored.ui, UIConfig)
    assert isinstance(restored.spotify, SpotifyConfig)
    assert isinstance(restored.obs, ObsConfig)
