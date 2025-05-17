import streamlit as st

st.header("Contact Us")

with st.form(key='email'):
    user_email = st.text_input('Your email address', placeholder='example@mail.com')
    user_massage = st.text_area('Tipe you massage')
    send_button = st.form_submit_button('Submit')
    if send_button:
        print('Button was pressed')