import cv2
import numpy as np
import streamlit as st

st.header("Decode the QR Code")

def decode_qrcode_page():
    qrcode = st.file_uploader("Upload your QR-Code",
                     type=["jpg", "png", "jpeg", "gif"])

    if qrcode:
        file_bytes = np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        st.image(opencv_image)

        detector = cv2.QRCodeDetector()
        decoded_info, point, straight_qr = detector.detectAndDecode(opencv_image)
        st.write(f"Your QRCode contained {decoded_info}")
