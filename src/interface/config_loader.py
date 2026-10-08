from pathlib import Path

from pydantic import ValidationError

from interface.model import ConsoleConfig


class ConfigLoadError(Exception):
    """Raised when a console config file cannot be read or validated."""


def load_console_config(config_path: Path) -> ConsoleConfig:
    try:
        config_json = config_path.read_text(encoding="utf-8")
        return ConsoleConfig.model_validate_json(config_json)
    except (OSError, UnicodeError) as error:
        raise ConfigLoadError(f"Could not read {config_path}: {error}") from error
    except ValidationError as error:
        details = "; ".join(
            f"{'.'.join(str(part) for part in issue['loc'])}: {issue['msg']}"
            for issue in error.errors()
        )
        raise ConfigLoadError(
            f"Invalid configuration in {config_path}: {details}"
        ) from error
