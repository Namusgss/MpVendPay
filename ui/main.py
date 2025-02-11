

import tkinter as tk
from gui import VendingMachineApp

if __name__ == "__main__":
    # Set the FastAPI server URL
    api_url = "http://localhost:8000"  # Replace with your FastAPI server URL if needed

    # Initialize the Tkinter root window and pass the API URL to the GUI
    root = tk.Tk()
    app = VendingMachineApp(root, api_url)
    root.mainloop()
