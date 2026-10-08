from pathlib import Path

from PySide6.QtCore import QPropertyAnimation, Qt, QTimer
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QGraphicsOpacityEffect,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from interface.model import ConsoleConfig


class Console:
    def __init__(
        self, config: ConsoleConfig, app: QApplication, config_directory: Path
    ) -> None:
        self.app = app
        self.window = QMainWindow()

        self.window.setWindowTitle(config.ui.title)
        self.window.resize(config.ui.width, config.ui.height)
        self.window.setWindowIcon(
            QIcon(
                str(self._resolve_asset_path(config.ui.favicon_path, config_directory))
            )
        )

        self._fade_animation: QPropertyAnimation | None = None
        self._show_start_screen(
            config.ui.start_screen_path,
            config.ui.start_screen_duration_seconds,
            config_directory,
        )

    @staticmethod
    def _resolve_asset_path(path: Path, config_directory: Path) -> Path:
        if path.is_absolute():
            return path
        return config_directory / path

    def _show_start_screen(
        self,
        image_path: Path,
        duration_seconds: float,
        config_directory: Path,
    ) -> None:
        pixmap = QPixmap(str(self._resolve_asset_path(image_path, config_directory)))
        screen = self.app.primaryScreen()
        if pixmap.isNull() or screen is None:
            self.window.show()
            return

        window_size = self.window.size()
        screen_geometry = screen.availableGeometry()
        scaled_pixmap = pixmap.scaled(
            window_size,
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation,
        )
        x_offset = (scaled_pixmap.width() - window_size.width()) // 2
        y_offset = (scaled_pixmap.height() - window_size.height()) // 2
        screen_pixmap = scaled_pixmap.copy(
            x_offset,
            y_offset,
            window_size.width(),
            window_size.height(),
        )

        self.start_screen = QWidget(
            None,
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint,
        )
        layout = QVBoxLayout(self.start_screen)
        layout.setContentsMargins(0, 0, 0, 0)
        image = QLabel()
        image.setPixmap(screen_pixmap)
        layout.addWidget(image)

        self._start_screen_opacity = QGraphicsOpacityEffect(self.start_screen)
        self.start_screen.setGraphicsEffect(self._start_screen_opacity)
        x_position = (
            screen_geometry.x() + (screen_geometry.width() - window_size.width()) // 2
        )
        y_position = (
            screen_geometry.y() + (screen_geometry.height() - window_size.height()) // 2
        )
        self.start_screen.setGeometry(
            x_position,
            y_position,
            window_size.width(),
            window_size.height(),
        )
        self.start_screen.show()
        duration_ms = round(duration_seconds * 1000)
        QTimer.singleShot(duration_ms, self._fade_out_start_screen)

    def _fade_out_start_screen(self) -> None:
        self._fade_animation = QPropertyAnimation(
            self._start_screen_opacity, b"opacity"
        )
        self._fade_animation.setDuration(700)
        self._fade_animation.setStartValue(1.0)
        self._fade_animation.setEndValue(0.0)
        self._fade_animation.finished.connect(self._finish_start_screen)
        self._fade_animation.start()

    def _finish_start_screen(self) -> None:
        self.start_screen.close()
        self.window.show()

    def start(self) -> int:
        return self.app.exec()
