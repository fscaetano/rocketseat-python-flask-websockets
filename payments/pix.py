import uuid
import qrcode

class Pix:
    def __init__(self) -> None:
        pass
    
    def create_payment(self):
        bank_payment_id = str(uuid.uuid4())
        hash_payment = f"hash_payment_{bank_payment_id}"
        
        # qr code
        img = qrcode.make(hash_payment)
        img.save(f"static/img/qrcode_payment_{bank_payment_id}.png")
        
        return {
            "bank_payment_id":bank_payment_id,
            "qr_code_path":f"qrcode_payment_{bank_payment_id}"
            }