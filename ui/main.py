# import tkinter as tk
# from gui import VendingMachineApp
# from product_data import products

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = VendingMachineApp(root, products)
#     root.mainloop()

import tkinter as tk
from gui import VendingMachineApp

if __name__ == "__main__":
    # Set the FastAPI server URL
    api_url = "http://127.0.0.1:8000"  # Replace with your FastAPI server URL if needed

    # Initialize the Tkinter root window and pass the API URL to the GUI
    root = tk.Tk()
    app = VendingMachineApp(root, api_url)
    root.mainloop()
