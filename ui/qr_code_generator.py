# # import qrcode
# # from PIL import Image

# # def generate_qr_code(product):
# #     data = f"Product: {product['name']}\nPrice: {product['price'] * product['quantity']}\nQuantity: {product['quantity']}"
# #     qr = qrcode.QRCode(version=1, box_size=10, border=4)
# #     qr.add_data(data)
# #     qr.make(fit=True)
# #     img = qr.make_image(fill="black", back_color="white").resize((300, 300))
# #     return img

# # qr_code_generator.py
# import qrcode
# import json

# def generate_qr_code(product_data):
#     """
#     Generate a QR code containing product purchase details.
    
#     Args:
#         product_data (dict): Dictionary containing:
#             - name: Product name
#             - price: Total price (unit price * quantity)
#             - quantity: Number of items being purchased
            
#     Returns:
#         PIL.Image: QR code image
#     """
#     try:
#         # Format the data as a JSON string
#         qr_data = {
#             "name": product_data["name"],
#             "total_price": product_data["price"],
#             "quantity": product_data["quantity"],
#             "timestamp": "YYYY-MM-DD HH:MM:SS"  # You can add actual timestamp here
#         }
        
#         json_data = json.dumps(qr_data, ensure_ascii=False)
        
#         # Create QR code instance
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
        
#         # Add the data
#         qr.add_data(json_data)
#         qr.make(fit=True)
        
#         # Create the QR code image
#         qr_image = qr.make_image(fill_color="black", back_color="white")
#         qr_image = qr.make_image(fill="black", back_color="white").resize((300, 300))
#         return qr_image
    
#     except Exception as e:
#         print(f"Error generating QR code: {e}")
#         raise


# qr_code_generator.py
import qrcode
import json
from PIL import Image
from datetime import datetime

def generate_qr_code(product_data):
    """
    Generate a QR code with automatic timestamp.
    
    Args:
        product_data (dict): Dictionary containing product details
            
    Returns:
        PIL.Image: QR code image
    """
    try:
        # Get current timestamp in a readable format
        current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format the data as a JSON string
        qr_data = {
            "name": product_data["name"],
            "total_price": product_data["price"],
            "quantity": product_data["quantity"],
            "timestamp": current_timestamp  # Add automatic timestamp
        }
        
        json_data = json.dumps(qr_data, ensure_ascii=False)
        
        # Create QR code with smaller parameters
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=2,
        )
        
        qr.add_data(json_data)
        qr.make(fit=True)
        
        # Create and resize the QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image = qr_image.resize((300, 300))
        
        return qr_image
    
    except Exception as e:
        print(f"Error generating QR code: {e}")
        raise