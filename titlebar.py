import tkinter as tk


class CustomTitlebar(tk.Frame):
    def __init__(self, parent, title="App", icon=None, bg_color="#2b2b2b", fg_color="white"):
        super().__init__(parent, bg=bg_color, height=32)
        self.parent = parent

        # Icon
        if icon:
            try:
                self.icon_img = tk.PhotoImage(file=icon)
                tk.Label(self, image=self.icon_img, bg=bg_color).pack(side="left", padx=5)
            except Exception:
                tk.Label(self, text="■", bg=bg_color, fg=fg_color).pack(side="left", padx=5)

        # Title
        tk.Label(self, text=title, bg=bg_color, fg=fg_color, font=("Segoe UI", 10)).pack(side="left", padx=3)

        # Minimize button
        tk.Button(self, text="—", command=self.parent.minimize_to_tray,
                  bg=bg_color, fg=fg_color, borderwidth=0, width=3).pack(side="right")

        # Close button
        tk.Button(self, text="✕", command=self.parent.destroy,
                  bg=bg_color, fg=fg_color, borderwidth=0, width=3).pack(side="right")

        # Drag to move
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<B1-Motion>", self.on_move)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def on_move(self, event):
        x = event.x_root - self.x
        y = event.y_root - self.y
        self.parent.geometry(f"+{x}+{y}")
