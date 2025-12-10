import os
import sys
import tkinter as tk
from tkinter import scrolledtext, messagebox

from splash import SplashScreen
from titlebar import CustomTitlebar
from tray import SystemTray
from updater import UpdateChecker

APP_VERSION = "1.0.1"

# Colors
COLOR_PRIMARY = "#2DC0A9"  # Teal from icon
COLOR_PRIMARY_DARK = "#238F7D"
COLOR_BG = "#E0F2EF"  # lighter teal
COLOR_TEXT = "#000000"


class WiFiGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.overrideredirect(True)
        self.geometry("550x380")
        self.minsize(400, 250)
        self.configure(bg=COLOR_BG)

        # Set window icon
        try:
            icon_path = self.resource_path("app.ico")
            self.iconbitmap(icon_path)
        except Exception as e:
            print(f"Set icon error: {e}")

        # Titlebar
        try:
            self.titlebar = CustomTitlebar(self, title="WiFi Utility", icon=self.resource_path("app.ico"),
                                           bg_color=COLOR_PRIMARY_DARK, fg_color="white")
            self.titlebar.pack(fill="x")
        except Exception as e:
            print(f"Titlebar error: {e}")

        self.body = tk.Frame(self, bg=COLOR_BG, padx=10, pady=10)
        self.body.pack(fill="both", expand=True)

        tk.Label(self.body, text="WiFi Utility Panel", font=("Segoe UI", 13, "bold"),
                 bg=COLOR_BG, fg=COLOR_PRIMARY_DARK).pack(pady=(5, 10))

        btn_row = tk.Frame(self.body, bg=COLOR_BG)
        btn_row.pack(pady=5)

        btn_style = {"width": 18, "font": ("Segoe UI", 10, "bold"), "bg": COLOR_PRIMARY, "fg": "white",
                     "borderwidth": 0}

        tk.Button(btn_row, text="Show WiFi Password", command=self.run_action, **btn_style).pack(side="left", padx=5)
        tk.Button(btn_row, text="Clear Text", command=self.clear_text, **btn_style).pack(side="left", padx=5)

        self.text = scrolledtext.ScrolledText(self.body, wrap="word", font=("Segoe UI", 10),
                                              bg="white", fg=COLOR_TEXT, relief="flat", borderwidth=1)
        self.text.pack(fill="both", expand=True)
        self.text.config(state="disabled")

        try:
            self.tray = SystemTray(self, icon_path)
        except Exception as e:
            print(f"Tray error: {e}")

        try:
            self.update_checker = UpdateChecker("pyapril15/wifi_utility", APP_VERSION)
        except Exception as e:
            print(f"Updater error: {e}")

    def write_text(self, content, append=False):
        try:
            self.text.config(state="normal")
            if append:
                self.text.insert("end", "\n" + str(content))
            else:
                self.text.delete("1.0", "end")
                self.text.insert("end", content)
            self.text.config(state="disabled")
        except Exception as e:
            print(f"Write text error: {e}")

    def clear_text(self):
        try:
            self.text.config(state="normal")
            self.text.delete("1.0", "end")
            self.text.config(state="disabled")
        except Exception as e:
            print(f"Clear text error: {e}")

    def run_action(self):
        try:
            messagebox.showinfo("Info", "Place your WiFi logic here.")
            self.write_text("Your output will appear here...")
        except Exception as e:
            print(f"Run action error: {e}")

    def minimize_to_tray(self):
        try:
            self.withdraw()
            if hasattr(self, "tray"):
                self.tray.show_icon()
        except Exception as e:
            print(f"Minimize tray error: {e}")

    def restore_from_tray(self):
        try:
            self.deiconify()
            if hasattr(self, "tray"):
                self.tray.hide_icon()
        except Exception as e:
            print(f"Restore tray error: {e}")

    def resource_path(self, relative):
        try:
            base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
            return os.path.join(base_path, relative)
        except Exception:
            return relative


if __name__ == "__main__":
    try:
        SplashScreen(duration=3000, icon="app.ico")
    except Exception as e:
        print(f"Splash error: {e}")

    try:
        app = WiFiGUI()
        app.mainloop()
    except Exception as e:
        print(f"App launch error: {e}")
