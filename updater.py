from tkinter import messagebox

import requests


class UpdateChecker:
    def __init__(self, repo, current_version):
        self.repo = repo
        self.current = current_version

    def check_now(self):
        try:
            url = f"https://api.github.com/repos/{self.repo}/releases/latest"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            latest = response.json().get("tag_name", self.current)
            if latest != self.current:
                messagebox.showinfo("Update Available",
                                    f"New version {latest} available.\nVisit GitHub to download.")
            else:
                messagebox.showinfo("Up-to-Date", "You already have the latest version.")
        except Exception as e:
            print(f"Update check error: {e}")
            messagebox.showerror("Update Error", f"Could not check updates.\n{e}")
