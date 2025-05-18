import streamlit as st
from functions import send_email
import pandas as pd

topic_list = [row['topic'] for index, row in pd.read_csv('topics.csv').iterrows()]
st.header("Contact Us")

with st.form(key='email'):
    visitor_email = st.text_input('Your email address', placeholder='example@mail.com')
    topic = st.selectbox('What topic do you want to discuss?', topic_list)
    visitor_row_message = st.text_area('Tipe you message') + '\n' + visitor_email
    send_button = st.form_submit_button('Submit')
    subject = f"New mail from {visitor_email}"
    receiver = 'gritsun.sp@gmail.com'
    if send_button:
        message = f"From: {visitor_email}\r\nTo: {receiver}\r\nSubject: {subject}\r\n\r\n" \
                  f"Topic: {topic}\r\n{visitor_row_message} "
        send_email(receiver, message)
        st.info('The message was sent successfully')
