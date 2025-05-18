import streamlit as st
import pandas as pd
import smtplib
import ssl

data = pd.read_csv('data.csv')


def col_draw(col, beg, end, table=data):
    for index, row in table[beg:end].iterrows():
        with col:
            st.subheader(row['first name'].title() + " " + row['last name'].title())
            st.markdown(
                f"<span style='font-size: 17px;'>{row['role']}</span>",
                unsafe_allow_html=True
            )
            st.image("images/" + row['image'])


def empty_col_draw(col):
    with col:
        st.write('')


def send_email(receiver, message):
    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()

    gmail_user = 'gsp672021@gmail.com'
    app_password = 'gbiylefkztnirvyh'

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(gmail_user, app_password)
        server.sendmail(gmail_user, receiver, message)
