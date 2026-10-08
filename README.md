# Holden Console ♠️ ♥️

Holden Console is a local control app for the [NLHolden live poker stream on
Twitch](https://www.twitch.tv/nlholden). 🟣📺 It is designed to make session
information easy to manage while playing and keep the on-screen overlay in sync
with the stream.

## Project concept 🃏

The project brings together two main parts:

1. **Operator interface 🎛️** — add tournaments to a session, assign tables,
   remove tournaments when play ends, and record cashouts.
2. **Session and broadcast engine 🔴** — maintain the current session state and
   send updates to OBS for the stream overlay.

The overlay is expected to show active tournaments, session buy-ins and cashes,
and other stream information.

## Development setup 🛠️

The project requires Python 3.11 or newer. From the repository root, activate
the project's virtual environment and install the package with its development
tools:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Install the Git hooks once per checkout:

```powershell
python -m pre_commit install
```

## Project layout 📁

```text
src/
  controller/   OBS and Spotify integrations
  data/         Pydantic models and poker-site types
  interface/    PySide6 desktop application
assets/images/  Application image assets
tests/          Unit tests and reusable test doubles
```
