APP_VERSION = "1.0.1"
import sys
import os
import json
import socket
import getpass
from datetime import datetime

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation
from PySide6.QtGui import QFont


CONFIG_FILE = "config.json"


def is_first_login():
    if not os.path.exists(CONFIG_FILE):
        return True

    with open(CONFIG_FILE, "r") as f:
        data = json.load(f)
        return not data.get("shown", False)


def mark_as_shown():
    with open(CONFIG_FILE, "w") as f:
        json.dump({"shown": True}, f)


class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        # User & system info
        username = getpass.getuser()
        pc_name = socket.gethostname()

        self.setWindowTitle("Welcome")
        self.setFixedSize(550, 300)

        # Splash style
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        # Start transparent for fade-in
        self.setWindowOpacity(0.0)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.welcome_label = QLabel("Welcome")
        self.welcome_label.setFont(QFont("Arial", 26, QFont.Bold))
        self.welcome_label.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel(f"{username} ({pc_name})")
        self.name_label.setFont(QFont("Arial", 20))
        self.name_label.setAlignment(Qt.AlignCenter)

        self.time_label = QLabel()
        self.time_label.setFont(QFont("Arial", 18))
        self.time_label.setAlignment(Qt.AlignCenter)

        self.date_label = QLabel()
        self.date_label.setFont(QFont("Arial", 16))
        self.date_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.welcome_label)
        layout.addWidget(self.name_label)
        layout.addSpacing(15)
        layout.addWidget(self.time_label)
        layout.addWidget(self.date_label)

        self.setLayout(layout)

        # Time updater
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

        # Fade-in animation
        self.fade_anim = QPropertyAnimation(self, b"windowOpacity")
        self.fade_anim.setDuration(1500)
        self.fade_anim.setStartValue(0.0)
        self.fade_anim.setEndValue(1.0)
        self.fade_anim.start()

        # Auto close
        QTimer.singleShot(8000, self.close)

        # Mark as shown
        mark_as_shown()

    def update_time(self):
        now = datetime.now()
        self.time_label.setText(now.strftime("%H:%M:%S"))
        self.date_label.setText(now.strftime("%A, %d %B %Y"))
        
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
    check_for_update()
    if not is_first_login():
        sys.exit(0)

    app = QApplication(sys.argv)
    window = WelcomeScreen()
    window.show()
    sys.exit(app.exec())
