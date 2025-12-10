import tkinter as tk


class SplashScreen:
    def __init__(self, duration=3000, icon=None):
        try:
            splash = tk.Tk()
            splash.overrideredirect(True)

            width, height = 300, 150
            x = (splash.winfo_screenwidth() // 2) - (width // 2)
            y = (splash.winfo_screenheight() // 2) - (height // 2)
            splash.geometry(f"{width}x{height}+{x}+{y}")

            if icon:
                try:
                    splash.iconbitmap(icon)
                except Exception:
                    pass

            tk.Label(splash, text="WiFi Utility", font=("Segoe UI", 16, "bold")).pack(pady=20)
            tk.Label(splash, text="Loading...", font=("Segoe UI", 10)).pack()

            splash.after(duration, splash.destroy)
            splash.mainloop()
        except Exception as e:
            print(f"SplashScreen error: {e}")
