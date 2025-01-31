
# # # to generate qr in json format
# # # import tkinter as tk
# # # from PIL import Image, ImageTk
# # # import qrcode
# # # import json


# # # # Function to generate QR code in JSON format
# # # def generate_qr_code(product):
# # #     """
# # #     Generate a QR code containing the product details in JSON format.
# # #     """
# # #     # Prepare the product data as a JSON object
# # #     product_data = {
# # #         "name": product["name"],
# # #         "price": product["price"],
# # #         "quantity": product["quantity"]
# # #     }
# # #     json_data = json.dumps(product_data)  # Convert dictionary to JSON string

# # #     # Generate QR code
# # #     qr = qrcode.QRCode(
# # #         version=1,
# # #         error_correction=qrcode.constants.ERROR_CORRECT_L,
# # #         box_size=10,
# # #         border=4,
# # #     )
# # #     qr.add_data(json_data)  # Add JSON data to the QR code
# # #     qr.make(fit=True)
# # #     return qr.make_image(fill_color="black", back_color="white")


# # # # Main Vending Machine App Class
# # # class VendingMachineApp:
# # #     def __init__(self, root, products):
# # #         self.root = root
# # #         self.root.geometry("800x600")
# # #         self.root.title("Vending Machine")
# # #         self.root.configure(bg="#f2f2f2")
# # #         self.products = products
# # #         self.selected_product = None

# # #         # Main layout frames
# # #         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # #         self.left_frame.pack(side="left", fill="y")

# # #         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # #         self.right_frame.pack(side="right", fill="y")

# # #         # Top label for "Smart Vending Machine" at the top center
# # #         self.top_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # #         self.top_frame.pack(side="top", fill="x")
# # #         self.details_label = tk.Label(self.top_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
# # #                                       bg="#f2f2f2")
# # #         self.details_label.pack(pady=10, side="top")

# # #         # Create product frame to hold product images
# # #         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # #         self.product_frame.pack(side="top", fill="both", expand=True)

# # #         # Container to center the images
# # #         self.product_container = tk.Frame(self.product_frame, bg="#f2f2f2")
# # #         self.product_container.pack(side="top", fill="x", padx=50)

# # #         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
# # #         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

# # #         # Buttons and quantity frame
# # #         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # #         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
# # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
# # #         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
# # #         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
# # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)

# # #         self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14),
# # #                                       bg="#f2f2f2")
# # #         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
# # #                                         bg="#FF5722", fg="white", relief="solid", width=10)

# # #         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
# # #                                      bg="#FF5722", fg="white", relief="solid", width=10)

# # #         self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
# # #         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

# # #         # Add the "A Major Project" text and details below the images
# # #         self.footer_label = tk.Label(self.product_frame, text="A Major Project by BEI077", font=("Arial", 12, "italic"),
# # #                                      bg="#f2f2f2")
# # #         self.footer_label.pack(pady=10)

# # #         self.names_label = tk.Label(self.product_frame, text="Suman Bhandari\tACE077BEI037",
# # #                                     font=("Arial", 12), bg="#f2f2f2")
# # #         self.names_label.pack(pady=5)

# # #         self.load_products()

# # #     def load_products(self):
# # #         for product in self.products:
# # #             image_path = product["image"]
# # #             product_img = Image.open(image_path).resize((150, 150))
# # #             product_img_tk = ImageTk.PhotoImage(product_img)
# # #             button = tk.Button(self.product_container, image=product_img_tk, text=product['name'], compound="top",
# # #                                command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
# # #                                bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
# # #             button.image = product_img_tk
# # #             button.pack(side="left", padx=20, pady=20)

# # #     def on_product_click(self, product):
# # #         self.selected_product = product
# # #         self.product_frame.pack_forget()
# # #         self.details_label.config(text=f"Selected Product: {product['name']}")

# # #         # Display product image
# # #         product_img = Image.open(product["image"]).resize((200, 200))
# # #         product_img_tk = ImageTk.PhotoImage(product_img)
# # #         self.product_image_label.config(image=product_img_tk)
# # #         self.product_image_label.image = product_img_tk
# # #         self.product_image_label.pack(pady=10)

# # #         # Display price
# # #         self.price_label.config(text=f"Price: NRs {product['price']}")
# # #         self.price_label.pack(pady=10)

# # #         # Display quantity frame
# # #         self.quantity_label.config(text=f"{product['quantity']}")
# # #         self.quantity_frame.pack(pady=10)
# # #         self.increase_button.pack(side="left", padx=10)
# # #         self.quantity_label.pack(side="left", padx=10)
# # #         self.decrease_button.pack(side="left", padx=10)

# # #         # Display payable amount
# # #         self.update_details()

# # #         # Display "Buy Now" button
# # #         self.buy_now_button.pack(pady=20)

# # #         # Show Back button
# # #         self.back_button.pack(side="bottom", pady=10)

# # #     def go_back(self):
# # #         self.product_frame.pack()
# # #         self.details_label.config(text="Smart Vending Machine")
# # #         self.product_image_label.pack_forget()
# # #         self.price_label.pack_forget()
# # #         self.quantity_frame.pack_forget()
# # #         self.payable_label.pack_forget()
# # #         self.buy_now_button.pack_forget()
# # #         self.qr_code_label.config(image="")  # Clear QR code
# # #         self.scan_label.pack_forget()

# # #         # Hide Back button
# # #         self.back_button.pack_forget()

# # #     def increase_quantity(self):
# # #         if self.selected_product:
# # #             self.selected_product["quantity"] += 1
# # #             self.update_details()

# # #             # Hide the QR code if it exists
# # #             self.qr_code_label.pack_forget()
# # #             self.scan_label.pack_forget()

# # #     def decrease_quantity(self):
# # #         if self.selected_product:
# # #             self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
# # #             self.update_details()

# # #             # Hide the QR code if it exists
# # #             self.qr_code_label.pack_forget()
# # #             self.scan_label.pack_forget()

# # #     def update_details(self):
# # #         if self.selected_product:
# # #             quantity = self.selected_product["quantity"]
# # #             price = self.selected_product["price"]
# # #             total = price * quantity
# # #             self.quantity_label.config(text=f"{quantity}")
# # #             self.payable_label.config(text=f"Payable Amount: {price} * {quantity} = {total}")
# # #             self.payable_label.pack(pady=10)

# # #     def buy_now(self):
# # #         qr_img = generate_qr_code(self.selected_product)
# # #         qr_img_tk = ImageTk.PhotoImage(qr_img)

# # #         # Show "Scan to Pay" label and QR code
# # #         self.scan_label.pack(pady=10)
# # #         self.qr_code_label.config(image=qr_img_tk)
# # #         self.qr_code_label.image = qr_img_tk
# # #         self.qr_code_label.pack(pady=20)

# # main code 
# import tkinter as tk
# from PIL import Image, ImageTk
# from qr_code_generator import generate_qr_code
# import requests
# from io import BytesIO
# import threading


# class VendingMachineApp:
#     def __init__(self, root, api_url):
#         self.root = root
#         self.root.geometry("1024x600")
#         self.root.title("Vending Machine")
#         self.root.configure(bg="#f2f2f2")
#         self.api_url = api_url
#         self.products = self.fetch_products()
#         self.selected_product = None
#         self.selected_quantity = 1  # Default quantity

#         # Main layout frames
#         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
#         self.left_frame.pack(side="left", fill="y")

#         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
#         self.right_frame.pack(side="right", fill="y")

#         # Top label for "Smart Vending Machine" at the top center
#         self.top_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.top_frame.pack(side="top", fill="x")
#         self.details_label = tk.Label(self.top_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
#                                       bg="#f2f2f2")
#         self.details_label.pack(pady=10, side="top")

#         # Create product frame to hold product images
#         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.product_frame.pack(side="top", fill="both", expand=True)

#         # Container to center the images
#         self.product_container = tk.Frame(self.product_frame, bg="#f2f2f2")
#         self.product_container.pack(side="top", fill="x", padx=50)  # Padding to avoid tight edges

#         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
#         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")
#         self.available_quantity_label = tk.Label(self.left_frame, text="", font=("Arial", 14), bg="#f2f2f2")
#         self.selected_quantity_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

#         # Buttons and quantity frame
#         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
#                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
#         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
#         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
#                                          font=("Arial", 16), bg="#F57220", fg="white", relief="solid", width=5)

#         self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14), bg="#f2f2f2")
#         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
#                                         bg="#4CAF50", fg="white", relief="solid", width=10)

#         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
#                                      bg="#FF5722", fg="white", relief="solid", width=10)

#         self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
#         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

#         # Footer labels
#         self.footer_label = tk.Label(self.product_frame, text="A Major Project by BEI077", font=("Arial", 12, "italic"),
#                                      bg="#f2f2f2")
#         self.footer_label.pack(pady=10)
#         self.names_label = tk.Label(self.product_frame, text="Suman Bhandari\tACE077BEI037",
#                                     font=("Arial", 12), bg="#f2f2f2")
#         self.names_label.pack(pady=5)

#         self.load_products()

#     def fetch_products(self):
#         """Fetch product data from the FastAPI backend."""
#         try:
#             response = requests.get(f"{self.api_url}/items")
#             response.raise_for_status()
#             return response.json()  # List of products
#         except requests.RequestException as e:
#             print(f"Error fetching products: {e}")
#             return []

#     def load_products(self):
#         """Dynamically create buttons for products."""
#         for product in self.products:
#             image_path = product["image"].strip()

#             # Load product image from URL
#             if image_path.startswith("http"):
#                 threading.Thread(target=self.load_product_image, args=(product, image_path)).start()
#             else:
#                 print("Local image paths are not currently supported.")

#     def load_product_image(self, product, image_path):
#         """Load product image in a separate thread."""
#         try:
#             response = requests.get(image_path)
#             response.raise_for_status()

#             if "image" in response.headers.get("Content-Type", ""):
#                 img_data = BytesIO(response.content)
#                 product_img = Image.open(img_data).resize((150, 150))
#                 product_img_tk = ImageTk.PhotoImage(product_img)

#                 # Add product button on the main thread
#                 self.root.after(0, self.add_product_button, product, product_img_tk)
#         except requests.RequestException as e:
#             print(f"Error fetching image: {e}")

#     def add_product_button(self, product, product_img_tk):
#         """Update the UI with a new product button."""
#         button = tk.Button(self.product_container, image=product_img_tk, text=product['name'], compound="top",
#                            command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
#                            bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
#         button.image = product_img_tk
#         button.pack(side="left", padx=20, pady=20)

#     def on_product_click(self, product):
#         """Handle product selection."""
#         self.selected_product = product
#         self.selected_quantity = 1  # Reset to default
#         self.update_details_gui()        




#     # def on_product_click(self, product):
#     #     """Handle product selection."""
#     #     self.selected_product = product
#     #     self.selected_quantity = 1  # Reset to default
#     #     self.product_frame.pack_forget()
#     #     self.details_label.config(text=f"Selected Product: {product['name']}")

#         # Display product image
#         product_img = Image.open(product["image"]).resize((200, 200))
#         product_img_tk = ImageTk.PhotoImage(product_img)
#         self.product_image_label.config(image=product_img_tk)
#         self.product_image_label.image = product_img_tk
#         self.product_image_label.pack(pady=10)

#         # Display price and quantity
#         self.price_label.config(text=f"Price: NRs {product['price']}/-")
#         self.available_quantity_label.config(text=f"Available Quantity: {product['quantity']}")
#         self.selected_quantity_label.config(text=f"Selected Quantity: {self.selected_quantity}")
#         self.price_label.pack(pady=10)
#         self.available_quantity_label.pack(pady=10)
#         self.selected_quantity_label.pack(pady=10)

#         # Quantity adjustment buttons
#         self.quantity_frame.pack(pady=10)
#         self.decrease_button.pack(side="left", padx=10)
#         self.quantity_label.pack(side="left", padx=10)
#         self.increase_button.pack(side="left", padx=10)
#         # Display payable amount
#         self.update_details()

#         # Display "Buy Now" button
#         self.buy_now_button.pack(pady=20)

#         # Show Back button
#         self.back_button.pack(side="bottom", pady=10)

#     def go_back(self):
#         """Handle 'Back' action to return to the product list."""
#         self.product_frame.pack()
#         self.details_label.config(text="Smart Vending Machine")
#         self.product_image_label.pack_forget()
#         self.price_label.pack_forget()
#         self.available_quantity_label.pack_forget()
#         self.selected_quantity_label.pack_forget()
#         self.quantity_frame.pack_forget()
#         self.payable_label.pack_forget()
#         self.buy_now_button.pack_forget()
#         self.qr_code_label.config(image="")  # Clear QR code
#         self.scan_label.pack_forget()
#         self.back_button.pack_forget()

#     def increase_quantity(self):
#         """Increase the selected quantity."""
#         if self.selected_product:
#             max_quantity = int(self.selected_product["quantity"])  # Ensure the quantity is an integer
#         if self.selected_quantity < max_quantity:
#             self.selected_quantity += 1
#             self.quantity_label.config(text=str(self.selected_quantity))  # Update the displayed quantity
#             self.update_details()  # Update the payable amount
#              # Clear the QR code and scan label
#             self.qr_code_label.pack_forget()
#             self.scan_label.pack_forget()
#             self.qr_code_label.config(image="")  # Clear the image

#     def decrease_quantity(self):
#         """Decrease the selected quantity."""
#         if self.selected_product:
#             if self.selected_quantity > 1:
#                 self.selected_quantity -= 1
#                 self.quantity_label.config(text=str(self.selected_quantity))  # Update the displayed quantity
#                 self.update_details()  # Update the payable amount
#                  # Clear the QR code and scan label
#             self.qr_code_label.pack_forget()
#             self.scan_label.pack_forget()
#             self.qr_code_label.config(image="")  # Clear the image


#     def update_details_gui(self):
#         """Update the payable amount based on the selected quantity."""
#         if self.selected_product:
#             price = int(self.selected_product["price"])  # Ensure price is an integer
#             total = price * self.selected_quantity  # Correct multiplication
#             self.selected_quantity_label.config(text=f"Selected Quantity: {self.selected_quantity}")
#             self.payable_label.config(text=f"Payable Amount: {price} * {self.selected_quantity} = NPR {total}/-")
#             self.payable_label.pack(pady=10)


#     def buy_now(self):
#         """Generate a QR code for the selected product and quantity."""
#         if self.selected_product:
#             try:
#                 # Clear any existing QR code
#                 self.qr_code_label.pack_forget()
#                 self.scan_label.pack_forget()
            
#                 # Validate product data
#                 required_fields = ["name", "price", "quantity"]
#                 if not all(key in self.selected_product for key in required_fields):
#                     raise ValueError("Product data is incomplete")
            
#             # Validate quantities
#                 if self.selected_quantity > int(self.selected_product["quantity"]):
#                     raise ValueError("Selected quantity exceeds available stock")
            
#             # Calculate total price
#                 unit_price = float(self.selected_product["price"])
#                 total_price = unit_price * self.selected_quantity
            
#             # Prepare data for QR code
#                 qr_data = {
#                     "name": self.selected_product["name"],
#                     "price": total_price,
#                     "quantity": self.selected_quantity
#                 }
            
#             # Generate QR code
#                 qr_img = generate_qr_code(qr_data)
#                 qr_img_tk = ImageTk.PhotoImage(qr_img)
            
#             # Display QR code and label
#                 self.scan_label.pack(pady=10)
#                 self.qr_code_label.config(image=qr_img_tk)
#                 self.qr_code_label.image = qr_img_tk
#                 self.qr_code_label.pack(pady=20)
            
            # Optional: Update remaining stock (if implementing stock management)
            # self.selected_product["quantity"] -= self.selected_quantity
            # self.available_quantity_label.config(text=f"Available Quantity: {self.selected_product['quantity']}")
            
    #         except ValueError as ve:
    #             print(f"Error: {ve}")
    #             # You might want to show this error to the user in the GUI
    #             self.show_error_message(str(ve))
    #         except Exception as e:
    #             print(f"Error generating QR code: {e}")
    #             self.show_error_message("Failed to generate QR code")
            
    # def show_error_message(self, message):
    #     """Display error message to user"""
    #     error_label = tk.Label(self.right_frame, 
    #                          text=message,
    #                          fg="red",
    #                          bg="#f2f2f2",
    #                          font=("Arial", 12))
    #     error_label.pack(pady=10)
    #     # Remove error message after 3 seconds
    #     self.root.after(3000, error_label.destroy)



# import tkinter as tk
# from PIL import Image, ImageTk
# from io import BytesIO
# import requests
# import threading

# class VendingMachineApp:
#     def __init__(self, root, api_url):
#         self.root = root
#         self.root.geometry("800x600")
#         self.root.title("Vending Machine")
#         self.root.configure(bg="#f2f2f2")
#         self.api_url = api_url
#         self.products = self.fetch_products()
#         self.selected_product = None
#         self.selected_quantity = 1  # Default quantity

#         # Main layout frames
#         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
#         self.left_frame.pack(side="left", fill="y")

#         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
#         self.right_frame.pack(side="right", fill="y")

#         # Top label for "Smart Vending Machine"
#         self.top_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.top_frame.pack(side="top", fill="x")
#         self.details_label = tk.Label(self.top_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
#                                       bg="#f2f2f2")
#         self.details_label.pack(pady=10, side="top")

#         # Create product frame to hold product images
#         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.product_frame.pack(side="top", fill="both", expand=True)

#         self.product_container = tk.Frame(self.product_frame, bg="#f2f2f2")
#         self.product_container.pack(side="top", fill="x", padx=50)

#         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
#         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")
#         self.available_quantity_label = tk.Label(self.left_frame, text="", font=("Arial", 14), bg="#f2f2f2")
#         self.selected_quantity_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

#         # Buttons and quantity frame
#         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
#                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
#         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
#         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
#                                          font=("Arial", 16), bg="#F57220", fg="white", relief="solid", width=5)

#         self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 0", font=("Arial", 14), bg="#f2f2f2")
#         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
#                                         bg="#4CAF50", fg="white", relief="solid", width=10)

#         # Footer labels
#         self.footer_label = tk.Label(self.product_frame, text="A Major Project by BEI077", font=("Arial", 12, "italic"),
#                                      bg="#f2f2f2")
#         self.footer_label.pack(pady=10)

#         self.load_products()

#     def fetch_products(self):
#         """Fetch product data from the FastAPI backend."""
#         try:
#             response = requests.get(f"{self.api_url}/items")
#             response.raise_for_status()
#             return response.json()  # List of products
#         except requests.RequestException as e:
#             print(f"Error fetching products: {e}")
#             return []

#     def load_products(self):
#         """Dynamically create buttons for products."""
#         for product in self.products:
#             image_path = product["image"].strip()

#             # Load product image from URL
#             if image_path.startswith("http"):
#                 threading.Thread(target=self.load_product_image, args=(product, image_path)).start()
#             else:
#                 print("Local image paths are not currently supported.")

#     def load_product_image(self, product, image_path):
#         """Load product image in a separate thread."""
#         try:
#             response = requests.get(image_path)
#             response.raise_for_status()

#             if "image" in response.headers.get("Content-Type", ""):
#                 img_data = BytesIO(response.content)
#                 product_img = Image.open(img_data).resize((150, 150))
#                 product_img_tk = ImageTk.PhotoImage(product_img)

#                 # Add product button on the main thread
#                 self.root.after(0, self.add_product_button, product, product_img_tk)
#         except requests.RequestException as e:
#             print(f"Error fetching image: {e}")

#     def add_product_button(self, product, product_img_tk):
#         """Update the UI with a new product button."""
#         button = tk.Button(self.product_container, image=product_img_tk, text=product['name'], compound="top",
#                            command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
#                            bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
#         button.image = product_img_tk
#         button.pack(side="left", padx=20, pady=20)

#     def on_product_click(self, product):
#         """Handle product selection."""
#         self.selected_product = product
#         self.selected_quantity = 1  # Reset to default
#         self.update_details_gui()

#     def update_details_gui(self):
#         """Update the UI with product details."""
#         product = self.selected_product
#         if not product:
#             return

#         self.details_label.config(text=f"Selected Product: {product['name']}")
#         self.price_label.config(text=f"Price: {product['price']}")
#         self.available_quantity_label.config(text=f"Available Quantity: {product['quantity']}")
#         self.quantity_label.config(text=str(self.selected_quantity))
#         self.payable_label.config(
#             text=f"Payable Amount: {product['price']} * {self.selected_quantity} = {product['price'] * self.selected_quantity}"
#         )

#         self.product_image_label.pack(pady=20)
#         self.price_label.pack(pady=10)
#         self.available_quantity_label.pack(pady=10)
#         self.quantity_frame.pack(pady=20)
#         self.increase_button.pack(side="left", padx=5)
#         self.quantity_label.pack(side="left", padx=5)
#         self.decrease_button.pack(side="left", padx=5)
#         self.payable_label.pack(pady=20)
#         self.buy_now_button.pack(pady=10)

#     def increase_quantity(self):
#         """Increase the selected product quantity."""
#         if self.selected_product:
#             max_quantity = self.selected_product.get("quantity", 0)
#             if self.selected_quantity < max_quantity:
#                 self.selected_quantity += 1
#                 self.update_details_gui()

#     def decrease_quantity(self):
#         """Decrease the selected product quantity."""
#         if self.selected_product and self.selected_quantity > 1:
#             self.selected_quantity -= 1
#             self.update_details_gui()

#     def buy_now(self):
#         """Handle the Buy Now button click."""
#         print(f"Buying {self.selected_quantity} of {self.selected_product['name']}!")



       

# import tkinter as tk
# from PIL import Image, ImageTk
# from qr_code_generator import generate_qr_code
# import requests


# class VendingMachineApp:
#     def __init__(self, root, api_url):
#         self.root = root
#         self.root.geometry("800x600")
#         self.root.title("Vending Machine")
#         self.root.configure(bg="#f2f2f2")
#         self.api_url = api_url
#         self.products = self.fetch_products()
#         self.selected_product = None
#         self.selected_quantity = 1  # Default quantity

#         # Main layout frames
#         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
#         self.left_frame.pack(side="left", fill="y")

#         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
#         self.right_frame.pack(side="right", fill="y")

#         # Top label for "Smart Vending Machine" at the top center
#         self.top_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.top_frame.pack(side="top", fill="x")
#         self.details_label = tk.Label(self.top_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
#                                       bg="#f2f2f2")
#         self.details_label.pack(pady=10, side="top")

#         # Create product frame to hold product images
#         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.product_frame.pack(side="top", fill="both", expand=True)

#         # Container to center the images
#         self.product_container = tk.Frame(self.product_frame, bg="#f2f2f2")
#         self.product_container.pack(side="top", fill="x", padx=50)  # Padding to avoid tight edges

#         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
#         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")
#         self.available_quantity_label = tk.Label(self.left_frame, text="", font=("Arial", 14), bg="#f2f2f2")
#         self.selected_quantity_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

#         # Buttons and quantity frame
#         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
#                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
#         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
#         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
#                                          font=("Arial", 16), bg="#F57220", fg="white", relief="solid", width=5)

#         self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14), bg="#f2f2f2")
#         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
#                                         bg="#4CAF50", fg="white", relief="solid", width=10)

#         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
#                                      bg="#FF5722", fg="white", relief="solid", width=10)

#         self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
#         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

#         # Footer labels
#         self.footer_label = tk.Label(self.product_frame, text="A Major Project by BEI077", font=("Arial", 12, "italic"),
#                                      bg="#f2f2f2")
#         self.footer_label.pack(pady=10)
#         self.names_label = tk.Label(self.product_frame, text="Suman Bhandari\tACE077BEI037",
#                                     font=("Arial", 12), bg="#f2f2f2")
#         self.names_label.pack(pady=5)

#         self.load_products()

#     def fetch_products(self):
#         """Fetch product data from the FastAPI backend."""
#         try:
#             response = requests.get(f"{self.api_url}/items")
#             response.raise_for_status()
#             return response.json()  # List of products
#         except requests.RequestException as e:
#             print(f"Error fetching products: {e}")
#             return []

#     def load_products(self):
#         """Dynamically create buttons for products."""
#         for product in self.products:
#             image_path = product["image"]  # Ensure the image path is valid
#             product_img = Image.open(image_path).resize((150, 150))
#             product_img_tk = ImageTk.PhotoImage(product_img)
#             button = tk.Button(self.product_container, image=product_img_tk, text=product['name'], compound="top",
#                                command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
#                                bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
#             button.image = product_img_tk
#             button.pack(side="left", padx=20, pady=20)

#     def on_product_click(self, product):
#         """Handle product selection."""
#         self.selected_product = product
#         self.selected_quantity = 1  # Reset to default
#         self.product_frame.pack_forget()
#         self.details_label.config(text=f"Selected Product: {product['name']}")

#         # Display product image
#         product_img = Image.open(product["image"]).resize((200, 200))
#         product_img_tk = ImageTk.PhotoImage(product_img)
#         self.product_image_label.config(image=product_img_tk)
#         self.product_image_label.image = product_img_tk
#         self.product_image_label.pack(pady=10)

#         # Display price and quantity
#         self.price_label.config(text=f"Price: NRs {product['price']}/-")
#         self.available_quantity_label.config(text=f"Available Quantity: {product['quantity']}")
#         self.selected_quantity_label.config(text=f"Selected Quantity: {self.selected_quantity}")
#         self.price_label.pack(pady=10)
#         self.available_quantity_label.pack(pady=10)
#         self.selected_quantity_label.pack(pady=10)

#         # Quantity adjustment buttons
#         self.quantity_frame.pack(pady=10)
#         self.decrease_button.pack(side="left", padx=10)
#         self.quantity_label.pack(side="left", padx=10)
#         self.increase_button.pack(side="left", padx=10)
#         # Display payable amount
#         self.update_details()

#         # Display "Buy Now" button
#         self.buy_now_button.pack(pady=20)

#         # Show Back button
#         self.back_button.pack(side="bottom", pady=10)

#     def go_back(self):
#         """Handle 'Back' action to return to the product list."""
#         self.product_frame.pack()
#         self.details_label.config(text="Smart Vending Machine")
#         self.product_image_label.pack_forget()
#         self.price_label.pack_forget()
#         self.available_quantity_label.pack_forget()
#         self.selected_quantity_label.pack_forget()
#         self.quantity_frame.pack_forget()
#         self.payable_label.pack_forget()
#         self.buy_now_button.pack_forget()
#         self.qr_code_label.config(image="")  # Clear QR code
#         self.scan_label.pack_forget()
#         self.back_button.pack_forget()

#     def increase_quantity(self):
#         """Increase the selected quantity."""
#         if self.selected_product:
#             max_quantity = int(self.selected_product["quantity"])  # Ensure the quantity is an integer
#         if self.selected_quantity < max_quantity:
#             self.selected_quantity += 1
#             self.quantity_label.config(text=str(self.selected_quantity))  # Update the displayed quantity
#             self.update_details()  # Update the payable amount
#              # Clear the QR code and scan label
#             self.qr_code_label.pack_forget()
#             self.scan_label.pack_forget()
#             self.qr_code_label.config(image="")  # Clear the image

#     def decrease_quantity(self):
#         """Decrease the selected quantity."""
#         if self.selected_product:
#             if self.selected_quantity > 1:
#                 self.selected_quantity -= 1
#                 self.quantity_label.config(text=str(self.selected_quantity))  # Update the displayed quantity
#                 self.update_details()  # Update the payable amount
#                  # Clear the QR code and scan label
#             self.qr_code_label.pack_forget()
#             self.scan_label.pack_forget()
#             self.qr_code_label.config(image="")  # Clear the image


#     def update_details(self):
#         """Update the payable amount based on the selected quantity."""
#         if self.selected_product:
#             price = int(self.selected_product["price"])  # Ensure price is an integer
#             total = price * self.selected_quantity  # Correct multiplication
#             self.selected_quantity_label.config(text=f"Selected Quantity: {self.selected_quantity}")
#             self.payable_label.config(text=f"Payable Amount: {price} * {self.selected_quantity} = NRs {total}/-")
#             self.payable_label.pack(pady=10)


#     def buy_now(self):
#         """Generate a QR code for the selected product and quantity."""
#         if self.selected_product:
#             try:
#                 # Clear any existing QR code
#                 self.qr_code_label.pack_forget()
#                 self.scan_label.pack_forget()
            
#                 # Validate product data
#                 required_fields = ["name", "price", "quantity"]
#                 if not all(key in self.selected_product for key in required_fields):
#                     raise ValueError("Product data is incomplete")
            
#             # Validate quantities
#                 if self.selected_quantity > int(self.selected_product["quantity"]):
#                     raise ValueError("Selected quantity exceeds available stock")
            
#             # Calculate total price
#                 unit_price = float(self.selected_product["price"])
#                 total_price = unit_price * self.selected_quantity
            
#             # Prepare data for QR code
#                 qr_data = {
#                     "name": self.selected_product["name"],
#                     "price": total_price,
#                     "quantity": self.selected_quantity
#                 }
            
#             # Generate QR code
#                 qr_img = generate_qr_code(qr_data)
#                 qr_img_tk = ImageTk.PhotoImage(qr_img)
            
#             # Display QR code and label
#                 self.scan_label.pack(pady=10)
#                 self.qr_code_label.config(image=qr_img_tk)
#                 self.qr_code_label.image = qr_img_tk
#                 self.qr_code_label.pack(pady=20)
            
#             # Optional: Update remaining stock (if implementing stock management)
#             # self.selected_product["quantity"] -= self.selected_quantity
#             # self.available_quantity_label.config(text=f"Available Quantity: {self.selected_product['quantity']}")
            
#             except ValueError as ve:
#                 print(f"Error: {ve}")
#                 # You might want to show this error to the user in the GUI
#                 self.show_error_message(str(ve))
#             except Exception as e:
#                 print(f"Error generating QR code: {e}")
#                 self.show_error_message("Failed to generate QR code")
            
#     def show_error_message(self, message):
#         """Display error message to user"""
#         error_label = tk.Label(self.right_frame, 
#                              text=message,
#                              fg="red",
#                              bg="#f2f2f2",
#                              font=("Arial", 12))
#         error_label.pack(pady=10)
#         # Remove error message after 3 seconds
#         self.root.after(3000, error_label.destroy)



import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from qr_code_generator import generate_qr_code
import os


class VendingMachineApp:
    def __init__(self, root, api_url):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Vending Machine")
        self.root.configure(bg="#f2f2f2")
        self.api_url = api_url
        self.products = self.fetch_products()
        self.selected_product = None
        self.selected_quantity = 1  # Default quantity

        # Main layout frames
        self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
        self.left_frame.pack(side="left", fill="y")

        self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
        self.right_frame.pack(side="right", fill="y")

        # Top label for "Smart Vending Machine" at the top center
        self.top_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
        self.top_frame.pack(side="top", fill="x")
        self.details_label = tk.Label(self.top_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
                                      bg="#f2f2f2")
        self.details_label.pack(pady=10, side="top")

        # Create product frame to hold product images
        self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
        self.product_frame.pack(side="top", fill="both", expand=True)

        # Container to center the images
        self.product_container = tk.Frame(self.product_frame, bg="#f2f2f2")
        self.product_container.pack(side="top", fill="x", padx=50)  # Padding to avoid tight edges

        self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
        self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")
        self.available_quantity_label = tk.Label(self.left_frame, text="", font=("Arial", 14), bg="#f2f2f2")
        self.selected_quantity_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

        # Buttons and quantity frame
        self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
        self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
                                         font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
        self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
        self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
                                         font=("Arial", 16), bg="#F57220", fg="white", relief="solid", width=5)

        self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14), bg="#f2f2f2")
        self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
                                        bg="#4CAF50", fg="white", relief="solid", width=10)

        self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
                                     bg="#FF5722", fg="white", relief="solid", width=10)

        self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
        self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

        # Footer labels
        self.footer_label = tk.Label(self.product_frame, text="A Major Project by BEI077", font=("Arial", 12, "italic"),
                                     bg="#f2f2f2")
        self.footer_label.pack(pady=10)
        self.names_label = tk.Label(self.product_frame, text="Suman Bhandari\tACE077BEI037",
                                    font=("Arial", 12), bg="#f2f2f2")
        self.names_label.pack(pady=5)

        self.load_products()

    def fetch_products(self):
        """Fetch product data from the FastAPI backend."""
        try:
            response = requests.get(f"{self.api_url}/items")
            response.raise_for_status()
            return response.json()  # List of products
        except requests.RequestException as e:
            print(f"Error fetching products: {e}")
            return []


    def load_products(self):
        """Dynamically create buttons for products."""
        for product in self.products:
            image_path = product["image"]  # Ensure the image path is valid
            
            # Check if image is a URL (remote) or a local file path
            if image_path.startswith("http://") or image_path.startswith("https://"):
                # Remote image URL
                try:
                    img_data = requests.get(image_path).content
                    product_img = Image.open(BytesIO(img_data)).resize((150, 150))
                except requests.exceptions.RequestException as e:
                    print(f"Error downloading image: {e}")
                    continue
            else:
                # Local image file
                if os.path.exists(image_path):
                    product_img = Image.open(image_path).resize((150, 150))
                else:
                    print(f"Error: Image path does not exist: {image_path}")
                    continue
            
            product_img_tk = ImageTk.PhotoImage(product_img)
            
            button = tk.Button(self.product_container, image=product_img_tk, text=product['name'], compound="top",
                               command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
                               bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
            button.image = product_img_tk
            button.pack(side="left", padx=20, pady=20)

    def on_product_click(self, product):
        """Handle product selection."""
        self.selected_product = product
        self.selected_quantity = 1  # Reset to default
        self.product_frame.pack_forget()
        self.details_label.config(text=f"Selected Product: {product['name']}")

        # Display product image
        image_path = product["image"]
        if image_path.startswith("http://") or image_path.startswith("https://"):
            try:
                img_data = requests.get(image_path).content
                product_img = Image.open(BytesIO(img_data)).resize((200, 200))
            except requests.exceptions.RequestException as e:
                print(f"Error downloading image: {e}")
                return
        else:
            if os.path.exists(image_path):
                product_img = Image.open(image_path).resize((200, 200))
            else:
                print(f"Error: Image path does not exist: {image_path}")
                return
        
        product_img_tk = ImageTk.PhotoImage(product_img)
        self.product_image_label.config(image=product_img_tk)
        self.product_image_label.image = product_img_tk
        self.product_image_label.pack(pady=10)

        # Display price and quantity
        self.price_label.config(text=f"Price: NRs {product['price']}/-")
        self.available_quantity_label.config(text=f"Available Quantity: {product['quantity']}")
        self.selected_quantity_label.config(text=f"Selected Quantity: {self.selected_quantity}")
        self.price_label.pack(pady=10)
        self.available_quantity_label.pack(pady=10)
        self.selected_quantity_label.pack(pady=10)

        # Quantity adjustment buttons
        self.quantity_frame.pack(pady=10)
        self.decrease_button.pack(side="left", padx=10)
        self.quantity_label.pack(side="left", padx=10)
        self.increase_button.pack(side="left", padx=10)
        # Display payable amount
        self.update_details()

        # Display "Buy Now" button
        self.buy_now_button.pack(pady=20)

        # Show Back button
        self.back_button.pack(side="bottom", pady=10)

    def go_back(self):
        """Handle 'Back' action to return to the product list."""
        self.product_frame.pack()
        self.details_label.config(text="Smart Vending Machine")
        self.product_image_label.pack_forget()
        self.price_label.pack_forget()
        self.available_quantity_label.pack_forget()
        self.selected_quantity_label.pack_forget()
        self.quantity_frame.pack_forget()
        self.payable_label.pack_forget()
        self.buy_now_button.pack_forget()
        self.qr_code_label.config(image="")  # Clear QR code
        self.scan_label.pack_forget()
        self.back_button.pack_forget()

    def increase_quantity(self):
        """Increase the selected quantity."""
        if self.selected_product:
            max_quantity = int(self.selected_product["quantity"])  # Ensure the quantity is an integer
        if self.selected_quantity < max_quantity:
            self.selected_quantity += 1
            self.quantity_label.config(text=str(self.selected_quantity))  # Update the displayed quantity
            self.update_details()  # Update the payable amount
             # Clear the QR code and scan label
            self.qr_code_label.pack_forget()
            self.scan_label.pack_forget()
            self.qr_code_label.config(image="")  # Clear the image

    def decrease_quantity(self):
        """Decrease the selected quantity."""
        if self.selected_product:
            if self.selected_quantity > 1:
                self.selected_quantity -= 1
                self.quantity_label.config(text=str(self.selected_quantity))  # Update the displayed quantity
                self.update_details()  # Update the payable amount
                 # Clear the QR code and scan label
            self.qr_code_label.pack_forget()
            self.scan_label.pack_forget()
            self.qr_code_label.config(image="")  # Clear the image

    def update_details(self):
        """Update the payable amount based on the selected quantity."""
        if self.selected_product:
            price = int(self.selected_product["price"])  # Ensure price is an integer
            total = price * self.selected_quantity  # Correct multiplication
            self.selected_quantity_label.config(text=f"Selected Quantity: {self.selected_quantity}")
            self.payable_label.config(text=f"Payable Amount: {price} * {self.selected_quantity} = NPR {total}/-")
            self.payable_label.pack(pady=10)

    def buy_now(self):
        """Generate a QR code for the selected product and quantity."""
        if self.selected_product:
            try:
                # Clear any existing QR code
                self.qr_code_label.pack_forget()
                self.scan_label.pack_forget()
            
                # Validate product data
                required_fields = ["name", "price", "quantity"]
                if not all(key in self.selected_product for key in required_fields):
                    raise ValueError("Product data is incomplete")
            
            # Validate quantities
                if self.selected_quantity > int(self.selected_product["quantity"]):
                    raise ValueError("Selected quantity exceeds available stock")
            
            # Calculate total price
                unit_price = float(self.selected_product["price"])
                total_price = unit_price * self.selected_quantity
            
            # Prepare data for QR code
                qr_data = {
                    "name": self.selected_product["name"],
                    "price": total_price,
                    "quantity": self.selected_quantity
                }
            
            # Generate QR code
                qr_img = generate_qr_code(qr_data)
                qr_img_tk = ImageTk.PhotoImage(qr_img)
            
            # Display QR code and label
                self.scan_label.pack(pady=10)
                self.qr_code_label.config(image=qr_img_tk)
                self.qr_code_label.image = qr_img_tk
                self.qr_code_label.pack(pady=20)
            
            # Optional: Update remaining stock (if implementing stock management)
            # self.selected_product["quantity"] -= self.selected_quantity
            # self.available_quantity_label.config(text=f"Available Quantity: {self.selected_product['quantity']}")
            
            except ValueError as ve:
                print(f"Error: {ve}")
                # You might want to show this error to the user in the GUI
                self.show_error_message(str(ve))
            except Exception as e:
                print(f"Error generating QR code: {e}")
                self.show_error_message("Failed to generate QR code")
            
    def show_error_message(self, message):
        """Display error message to user"""
        error_label = tk.Label(self.right_frame, 
                             text=message,
                             fg="red",
                             bg="#f2f2f2",
                             font=("Arial", 12))
        error_label.pack(pady=10)
        # Remove error message after 3 seconds
        self.root.after(3000, error_label.destroy)
