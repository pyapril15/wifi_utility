import os

import pystray
from PIL import Image
from pystray import MenuItem


class SystemTray:
    def __init__(self, app, icon_path):
        self.app = app
        self.icon = None
        self.icon_path = icon_path

    def create_icon(self):
        try:
            if not os.path.exists(self.icon_path):
                raise FileNotFoundError(f"{self.icon_path} not found")
            image = Image.open(self.icon_path)
            menu = (
                MenuItem("Show App", lambda: self.app.restore_from_tray()),
                MenuItem("Check Updates",
                         lambda: getattr(self.app, "update_checker", None) and self.app.update_checker.check_now()),
                MenuItem("Exit", lambda: self.app.destroy())
            )
            self.icon = pystray.Icon("wifi_app", image, "WiFi Utility", menu)
        except Exception as e:
            print(f"Tray icon creation error: {e}")

    def show_icon(self):
        try:
            if not self.icon:
                self.create_icon()
            if self.icon:
                self.icon.run_detached()
        except Exception as e:
            print(f"Show icon error: {e}")

    def hide_icon(self):
        try:
            if self.icon:
                self.icon.stop()
        except Exception as e:
            print(f"Hide icon error: {e}")
