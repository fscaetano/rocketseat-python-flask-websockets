import pytest
import os

import sys
base_dir = "../"
sys.path.append("../")

from payments.pix import Pix

def test_pix_create_payment():
    pix = Pix()
    
    payment_info = pix.create_payment(base_dir)
    
    assert "bank_payment_id" in payment_info
    assert "qr_code_path" in payment_info
    
    qr_code_path = payment_info["qr_code_path"]
    assert os.path.isfile(f"{base_dir}static/img/{qr_code_path}.png")