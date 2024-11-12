import qrcode
from datetime import datetime
from PIL import Image
import streamlit as st
from qrcode.image.styledpil import StyledPilImage


def qrcode_generator_app():

    st.header('Genewtor')

    def generate_qrcode(url):
        qr = qrcode.QRCode(
                            version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=10,
                            border=2
                            )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(image_factory=StyledPilImage)

        img.save("qrcode.png")

    main_image = Image.open('static/rick.png')

    st.image(main_image,use_column_width='auto')
    st.title("✨ QR Code Generator 🚀")
    url = st.text_input("Enter your URL please 👇")
    if url is not None and url != "":
        with st.spinner(f"Generating QR Code... 💫"):
            qrcode_path = generate_qrcode(str(url))

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(' ')
        with col2:
            image = Image.open("qrcode.png")
            st.image(image, caption='Here\'s the Generated QR Code ✅')
        with col3:
            st.write(' ')

    else:
        st.warning('⚠ Please enter your URL! 😯')

