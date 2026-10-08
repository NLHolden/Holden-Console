import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMessageBox

from interface.config_loader import ConfigLoadError, load_console_config
from interface.console import Console


def run_console(config_path: Path) -> int:
    app = QApplication(sys.argv[:1])

    try:
        config = load_console_config(config_path)
    except ConfigLoadError as error:
        QMessageBox.critical(None, "Configuration error", str(error))
        return 1

    return Console(config, app, config_path.resolve().parent).start()
