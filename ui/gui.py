
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from qr_code_generator import generate_qr_code
import os
import uuid
import RPi.GPIO as GPIO
import time


# Define motor control pins (updated with new pin numbers)
MOTOR_1_PIN_1 = 23  # GPIO pin for Noodles motor direction 1
MOTOR_1_PIN_2 = 24  # GPIO pin for Noodles motor direction 2
MOTOR_2_PIN_1 = 17  # GPIO pin for Chips motor direction 1
MOTOR_2_PIN_2 = 27  # GPIO pin for Chips motor direction 2
PWM_PIN_1 = 12       # GPIO pin for Noodles motor PWM (speed control)
PWM_PIN_2 = 13       # GPIO pin for Chips motor PWM (speed control)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_1_PIN_1, GPIO.OUT)
GPIO.setup(MOTOR_1_PIN_2, GPIO.OUT)
GPIO.setup(MOTOR_2_PIN_1, GPIO.OUT)
GPIO.setup(MOTOR_2_PIN_2, GPIO.OUT)
GPIO.setup(PWM_PIN_1, GPIO.OUT)
GPIO.setup(PWM_PIN_2, GPIO.OUT)

# Setup PWM (100Hz frequency for motor control)
motor_pwm_1 = GPIO.PWM(PWM_PIN_1, 100)  # PWM for Noodles motor
motor_pwm_2 = GPIO.PWM(PWM_PIN_2, 100)  # PWM for Chips motor
motor_pwm_1.start(0)  # Start Noodles motor with 0% duty cycle (motor off)
motor_pwm_2.start(0)  # Start Chips motor with 0% duty cycle (motor off)


class VendingMachineApp:
    def __init__(self, root, api_url):
        self.root = root
        self.root.geometry("1024x600")
        self.root.title("Vending Machine")
        self.root.configure(bg="#f2f2f2")
        self.api_url = api_url
        self.products = self.fetch_products()
        self.USERNAME = ""
        self.root.attributes('-fullscreen', True)
        self.root.bind ('<Escape>',self.exit_fullscreen)
        self.motor_running = False  # Flag to prevent motor interruptions
        self.transaction_id = ""
        self.dispense_quantity = 1

        #SUCCESS LABEL
   


        # Main layout frames
        self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
        self.left_frame.pack(side="left", fill="y")

        self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
        self.right_frame.pack(side="right", fill="y")

        # Top label for "Smart Vending Machine" at the top center
        self.top_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
        self.top_frame.pack(side="top", fill="x")
        self.details_label = tk.Label(self.top_frame, text="VENDme", font=("Helvetica", 18, "bold"),
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
        self.names_label = tk.Label(self.product_frame, text="Rojdeep Kharel\tACE077BEI029\nSagar Pantha\tACE077BEI030\nSuman Bhandari\tACE077BEI037",
                                    font=("Arial", 12), bg="#f2f2f2")
        self.names_label.pack(pady=5)
        self.success_label = tk.Label(self.right_frame, bg="#f2f2f2", font=("Arial", 14))

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

        # Reset quantity label in the UI
        self.quantity_label.config(text="1")

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
        """Generate a QR code and store transaction ID for consistency."""
        if self.selected_product:
            try:
                # Validate product data
                required_fields = ["name", "price", "quantity"]
                if not all(key in self.selected_product for key in required_fields):
                    raise ValueError("Product data is incomplete")

                # Validate quantities
                if self.selected_quantity > int(self.selected_product["quantity"]):
                    raise ValueError("Selected quantity exceeds available stock")

                # ✅ Generate a unique transaction ID in GUI
                self.transaction_id = str(uuid.uuid4())  
                print(f"✅ Generated Transaction ID: {self.transaction_id}")  # Debugging log

                # Calculate total price
                total_price = float(self.selected_product["price"]) * self.selected_quantity
            
                self.dispense_quantity= self.selected_quantity
                # ✅ Include transaction ID in QR data
                qr_data = {
                    "transaction_id": self.transaction_id,
                    "name": self.selected_product["name"],
                    "price": total_price,
                    "quantity": self.selected_quantity
                }

                # Generate QR code
                qr_img = generate_qr_code(qr_data)  # ✅ Now, it just creates the QR code (no new transaction ID)
                qr_img_tk = ImageTk.PhotoImage(qr_img)

                # Display QR code
                self.scan_label.pack(pady=10)
                self.qr_code_label.config(image=qr_img_tk)
                self.qr_code_label.image = qr_img_tk
                self.qr_code_label.pack(pady=20)

                # Start checking payment status

            except ValueError as ve:
                print(f"❌ Error: {ve}")
                self.show_error_message(str(ve))
            except Exception as e:
                print(f"❌ Error generating QR code: {e}")
                self.show_error_message("Failed to generate QR code")

            self.update_payment_status()
    
    
    def show_error_message(self, message):
        """Display error message to user"""
        error_label = tk.Label(self.right_frame,
                               text=message,
                               fg="red",
                               bg="#f2f2f2",
                               font=("Arial", 12))
        error_label.pack(pady=10)


    def check_payment_status(self):
        response = requests.get(f"{self.api_url}/get_username_by_transaction?transaction_id={self.transaction_id}")
        user_name = response.json()
        self.USERNAME = user_name.get("username")
        print(self.USERNAME)
        if self.transaction_id and self.USERNAME and not self.motor_running:  # Check only if motor is not running
            response = requests.get(
                f"{self.api_url}/check_payment_status?username={self.USERNAME}&transactionId={self.transaction_id}"
            )

            if response.status_code == 200:
                data = response.json()
                print(data)

                if data.get("status") == "success" and "product" in data:
                    self.display_success_message(data["product"]) 
                    
                    # Check if the motor is already running to prevent re-triggering
                    if not self.motor_running:
                        self.trigger_motor(data["product"])
                elif data.get("status") == "pending":
                    self.success_label.config(text="⌛ Payment Pending...", fg="orange")
                    self.success_label.pack(pady=20)
                elif data.get("status") == "no_transaction":
                    self.success_label.config(text="⚠ No transaction found.", fg="red")
                    self.success_label.pack(pady=20)
                else:
                    self.success_label.config(text="❌ Payment Failed!", fg="red")
                    self.success_label.pack(pady=20)
            else:
                print(f"❌ Failed to retrieve payment status. HTTP Status code: {response.status_code}")
        else:
            print("⚠ Missing transaction ID, username, or motor still running.")

    def display_success_message(self, product):
        username=self.USERNAME
        """Display the payment success message in the same window."""
        for widget in self.root.winfo_children():
            widget.destroy()
    
        success_label = tk.Label(self.root, text=f"✅ Payment Successful! for {self.USERNAME}\n Dispensing your {product}\nEnjoy your {product}!\n Do visit again", 
                             font=("Arial", 22), fg="green", bg="#f2f2f2", padx=20, pady=40)
        success_label.pack()

        self.root.after(15000, self.reset_gui)

    def trigger_motor(self, product):
        """Trigger the motor based on the product name."""
        if product.lower() == "noodles":
            self.rotate_motor("n", self.selected_quantity)
        elif product.lower() == "biscuits":
            self.rotate_motor("b", self.selected_quantity)
        else:
            print(f"Unknown product: {product}")

    
    def rotate_motor(self, motor_name, quantity, elapsed=0):
        """Simulate motor rotation for 10 seconds without blocking the GUI."""
        if elapsed == 0:  # Start motor
            if self.motor_running:
                print(f"Motor is already running. Ignoring new trigger for {motor_name}.")
                return
            self.motor_running = True  # Lock motor activation
            
            if motor_name == "n" :  # Noodles motor
                motor_pwm_1.start(100)  # Start Noodles motor with 0% duty cycle (motor off)
                motor_pwm_2.start(0) 
                if self.dispense_quantity > 0:
                    run_time = 7 * self.dispense_quantity
                    run_time = int(run_time)  # 5 seconds per quantity
                GPIO.output(MOTOR_1_PIN_1, GPIO.LOW)  # Set direction to forward
                GPIO.output(MOTOR_1_PIN_2, GPIO.HIGH)
                time.sleep(run_time)
                motor_pwm_1.start(0)  # Start Noodles motor with 0% duty cycle (motor off)
                motor_pwm_2.start(0)  
                self.motor_running = True
            elif motor_name == "b":  
                motor_pwm_1.start(0)  # Start Noodles motor with 0% duty cycle (motor off)
                motor_pwm_2.start(100) 
                if self.dispense_quantity > 0:
                    run_time = 7 * self.dispense_quantity
                    run_time = int(run_time) 
                GPIO.output(MOTOR_2_PIN_1, GPIO.HIGH)  # Set direction to forward
                GPIO.output(MOTOR_2_PIN_2, GPIO.LOW)
                time.sleep(run_time)
                motor_pwm_1.start(0)  # Start Noodles motor with 0% duty cycle (motor off)
                motor_pwm_2.start(0)  
                self.motor_running= True
        print(f"Starting {motor_name} at {speed}% speed for 10 seconds.")


    def update_payment_status(self):
        """Continuously check payment status but only trigger if motor isn't running."""
        if not self.motor_running:  # Ensure the motor is not interrupted
            self.check_payment_status()
        self.root.after(5000, self.update_payment_status)  # Check every 5 seconds
        
    def reset_gui(self):
        """Reset the GUI to its initial state after a successful transaction."""
        for widget in self.root.winfo_children():
            widget.destroy()

        self.transaction_id = None  # Clear transaction ID
        self.motor_running = False  # Ensure motor flag is reset
        
        # Reinitialize the interface
        self.__init__(self.root, self.api_url)
        
    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen',False)       
