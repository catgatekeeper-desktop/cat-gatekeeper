import json
import time
import threading
import tkinter as tk
from typing import Dict, Any

# NOTE: In a production cross-platform app, you will need OS-specific modules 
# (like pywin32 for Windows or AppKit for macOS) to accurately get the active process name.
# We use a dummy function here to represent the tracking logic.
import psutil
import pygetwindow as gw

class CatOverlay:
    """
    Handles the UI overlay (The Cat) that blocks the screen.
    """
    def __init__(self, rest_time_minutes: int):
        self.rest_time_seconds = rest_time_minutes * 60
        self.root = tk.Tk()
        
        # Setup full-screen, borderless, always-on-top window
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        
        # Make background transparent (Windows specific, adjust for macOS if needed)
        self.root.attributes("-transparentcolor", "black")
        self.root.configure(bg="black")
        
        # Load the cat image/gif (Requires a valid path to an image file)
        # For simplicity, using a label with text if image is not found
        try:
            # self.cat_image = tk.PhotoImage(file="assets/cat_sleeping.gif")
            # label = tk.Label(self.root, image=self.cat_image, bg="black")
            label = tk.Label(self.root, text="🐈 MEOW! TIME TO REST!", font=("Arial", 50, "bold"), fg="orange", bg="black")
        except tk.TclError:
            label = tk.Label(self.root, text="🐈 MEOW! TIME TO REST!", font=("Arial", 50, "bold"), fg="orange", bg="black")
            
        label.pack(expand=True)
        
    def start_blocking(self):
        """Starts the blocking overlay and closes it after the rest time ends."""
        # Close the window after the rest time is over
        self.root.after(self.rest_time_seconds * 1000, self.root.destroy)
        self.root.mainloop()


class CatGatekeeperCore:
    """
    Main engine for tracking active apps and managing timers.
    """
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self._load_config()
        self.app_usage: Dict[str, int] = {}  # Tracks seconds spent in each app
        self.is_resting = False
        
    def _load_config(self) -> Dict[str, Any]:
        """Loads configuration from JSON file."""
        try:
            with open(self.config_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Config file not found. Using default settings.")
            return {"global_rest_time_minutes": 5, "apps": []}

    def get_active_process_name(self) -> str:
        """
        Retrieves the name of the currently active window's process.
        TODO: Implement precise OS-specific tracking (macOS AppKit / Windows pywin32).
        """
        try:
            active_window = gw.getActiveWindow()
            if active_window is not None:
                # Placeholder: In reality, you need process ID from window handle to get .exe name
                # Currently returning window title just for PoC demonstration purposes
                title = active_window.title.lower()
                if "chrome" in title:
                    return "chrome.exe"
                elif "code" in title or "visual studio" in title:
                    return "Code.exe"
        except Exception as e:
            pass
        return "unknown"

    def is_fullscreen_video_playing(self) -> bool:
        """
        Detects if a user is watching a full-screen video to prevent interruptions.
        TODO: Implement logic to check if active window size equals screen size.
        """
        if not self.config.get("smart_video_detection", False):
            return False
        # Placeholder for smart detection
        return False

    def trigger_rest(self, process_name: str):
        """Triggers the Cat overlay and resets the timer for the app."""
        print(f"Time limit reached for {process_name}! The Cat is taking over the screen.")
        self.is_resting = True
        
        rest_minutes = self.config.get("global_rest_time_minutes", 5)
        overlay = CatOverlay(rest_minutes)
        overlay.start_blocking()
        
        # Reset the timer after the break
        self.app_usage[process_name] = 0
        self.is_resting = False
        print("Rest is over. Back to work!")

    def start_tracking(self):
        """Main loop that tracks time every second."""
        print("Cat Gatekeeper is awake and watching your apps... 🐈")
        
        # Build limits dictionary for faster lookup (Seconds)
        limits = {
            app["process_name"]: app["time_limit_minutes"] * 60 
            for app in self.config.get("apps", [])
        }

        while True:
            time.sleep(1) # Check every second
            
            if self.is_resting:
                continue
                
            if self.is_fullscreen_video_playing():
                continue

            active_process = self.get_active_process_name()
            
            if active_process in limits:
                # Initialize tracking for the process if not exists
                if active_process not in self.app_usage:
                    self.app_usage[active_process] = 0
                    
                self.app_usage[active_process] += 1
                
                # Check if the limit is exceeded
                if self.app_usage[active_process] >= limits[active_process]:
                    self.trigger_rest(active_process)


if __name__ == "__main__":
    # Run the tracker in the main thread (or a separate thread if building a GUI control panel)
    gatekeeper = CatGatekeeperCore()
    gatekeeper.start_tracking()
