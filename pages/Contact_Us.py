import streamlit as st
from functions import send_email
import pandas as pd

topic_list = [row['topic'] for index, row in pd.read_csv('topics.csv').iterrows()]
st.header("Contact Us")

with st.form(key='email'):
    visitor_email = st.text_input('Your email address', placeholder='example@mail.com')
    topic = st.selectbox('What topic do you want to discuss?', topic_list)
    visitor_row_massage = st.text_area('Tipe you massage') + '\n' + visitor_email
    send_button = st.form_submit_button('Submit')
    subject = f"New mail from {visitor_email}"
    receiver = 'gritsun.sp@gmail.com'
    message = f"From: {visitor_email}\r\nTo: {receiver}\r\nSubject: {subject}\r\n{topic}\r\n{visitor_row_massage}"
    if send_button:
        send_email(receiver, message)
        st.info('The message was sent successfully')
