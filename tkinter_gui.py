import tkinter as tk
import requests
import sys

class PoseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pose Prediction Control Panel")
        self.geometry("300x200")

        self.start_button = tk.Button(self, text="Start Predictions", command=self.start_predictions)
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(self, text="Stop", command=self.quit_app)
        self.stop_button.pack(pady=20)

    def start_predictions(self):
        # Make a request to Flask backend to serve the web page (or you can open the browser manually)
        print("Starting the prediction process...")

    def quit_app(self):
        print("Quitting the app...")
        self.destroy()
        sys.exit()

if __name__ == '__main__':
    app = PoseApp()
    app.mainloop()
