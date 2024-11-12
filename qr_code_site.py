import streamlit as st
st.set_page_config(page_title='QR Code generator', page_icon='👾')
from decode_qrcode_page import decode_qrcode_page
from qrcode_generator_app import qrcode_generator_app

menu_options = ['Generate QR-Code', 'Decode QR code', 'About me']

with st.sidebar:
    page_selection = st.selectbox('Menu', menu_options)

if page_selection == 'Generate QR-Code':
    qrcode_generator_app()
elif page_selection == 'Decode QR code':
    decode_qrcode_page()
elif page_selection == 'About me':
    st.title('Hello there.')