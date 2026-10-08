import sys

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory


def apply_dark_theme(app: QApplication) -> None:
    app.setStyle(QStyleFactory.create("Fusion"))

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#202124"))
    palette.setColor(QPalette.ColorRole.WindowText, QColor("#f1f3f4"))
    palette.setColor(QPalette.ColorRole.Base, QColor("#17181a"))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#292a2d"))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#292a2d"))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor("#f1f3f4"))
    palette.setColor(QPalette.ColorRole.Text, QColor("#f1f3f4"))
    palette.setColor(QPalette.ColorRole.Button, QColor("#292a2d"))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor("#f1f3f4"))
    palette.setColor(QPalette.ColorRole.BrightText, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Link, QColor("#8ab4f8"))
    palette.setColor(QPalette.ColorRole.Highlight, QColor("#8ab4f8"))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#17181a"))
    app.setPalette(palette)


def main() -> int:
    app = QApplication(sys.argv)
    apply_dark_theme(app)

    window = QMainWindow()
    window.setWindowTitle("Holden Console")
    window.resize(1100, 700)
    window.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
