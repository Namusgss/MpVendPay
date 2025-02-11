import qrcode
import json
from PIL import Image
from datetime import datetime

def generate_qr_code(product_data):
    """
    Generate a QR code with automatic timestamp.
    
    Args:
        product_data (dict): Dictionary containing product details with transaction_id
            
    Returns:
        PIL.Image: QR code image
    """
    try:
        # Get current timestamp
        current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Ensure transaction ID exists (must be passed from GUI)
        if "transaction_id" not in product_data:
            raise ValueError("Missing transaction ID in QR data")

        # Format the data as a JSON string
        qr_data = {
            "transaction_id": product_data["transaction_id"],  # ✅ Use the transaction ID from GUI
            "identifier": "VENDING_MACHINE",
            "productname": product_data["name"],
            "total_price": product_data["price"],
            "quantity": product_data["quantity"],
            "timestamp": current_timestamp
        }

        json_data = json.dumps(qr_data, ensure_ascii=False)

        # Create QR code
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

        return qr_image  # ✅ No longer returns transaction ID

    except Exception as e:
        print(f"❌ Error generating QR code: {e}")
        raise
