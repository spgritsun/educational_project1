import streamlit as st
from functions import send_email

st.header("Contact Us")

with st.form(key='email'):
    visitor_email = st.text_input('Your email address', placeholder='example@mail.com')
    visitor_row_massage = st.text_area('Tipe you massage') + '\n' + visitor_email
    send_button = st.form_submit_button('Submit')
    subject = f"New mail from {visitor_email}"
    message = f"From: {visitor_email}\r\nSubject: {subject}\r\n{visitor_row_massage}"
    if send_button:
        send_email(message)
        st.info('The email was sent successfully')
