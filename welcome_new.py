APP_VERSION = "1.0.0"
import sys
import os
import subprocess
import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout
)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont
from datetime import datetime


class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome")
        self.setFixedSize(500, 300)

        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Welcome label
        self.welcome_label = QLabel("Welcome")
        self.welcome_label.setFont(QFont("Arial", 26, QFont.Bold))
        self.welcome_label.setAlignment(Qt.AlignCenter)

        # Name label (CHANGE YOUR NAME HERE)
        self.name_label = QLabel("IPINLOJU MUSIBAU OPEYEMI")
        self.name_label.setFont(QFont("Arial", 20))
        self.name_label.setAlignment(Qt.AlignCenter)

        # Time label
        self.time_label = QLabel()
        self.time_label.setFont(QFont("Arial", 18))
        self.time_label.setAlignment(Qt.AlignCenter)

        # Date label
        self.date_label = QLabel()
        self.date_label.setFont(QFont("Arial", 16))
        self.date_label.setAlignment(Qt.AlignCenter)

        # Add widgets to layout
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.name_label)
        layout.addSpacing(15)
        layout.addWidget(self.time_label)
        layout.addWidget(self.date_label)

        self.setLayout(layout)

        # Timer to update time/date
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        now = datetime.now()
        self.time_label.setText(now.strftime("%H:%M:%S"))
        self.date_label.setText(now.strftime("%A, %d %B %Y"))
        self.check_for_update()

    def check_for_update(self):
        try:
            with open("version.txt", "r") as f:
                latest_version = f.read().strip()

            if latest_version != APP_VERSION:
                subprocess.Popen(["updater.exe"])
                sys.exit(0)

        except FileNotFoundError:
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeScreen()
    window.show()
    sys.exit(app.exec())
