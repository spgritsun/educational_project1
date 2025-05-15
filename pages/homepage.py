import streamlit as st
import pandas as pd

data = pd.read_csv('data.csv')
st.set_page_config(layout='wide')

title1 = 'The Best Company'
st.title(title1)

content = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the \
           industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type \
and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into'
st.write(content)

title2 = 'Our Team'
st.subheader(title2)

col1, col2, col3, col4, col5 = st.columns([7, 1, 7, 1, 7])

for index, row in data[:4].iterrows():
    with col1:
        st.subheader(row['first name'].title() + " " + row['last name'].title())
        st.markdown(
            f"<span style='font-size: 17px;'>{row['role']}</span>",
            unsafe_allow_html=True
        )
        st.image("images/" + row['image'])

    with col2:
        st.write('')

for index, row in data[4:8].iterrows():
    with col3:
        st.subheader(row['first name'].title() + " " + row['last name'].title())
        st.markdown(
            f"<span style='font-size: 17px;'>{row['role']}</span>",
            unsafe_allow_html=True
        )
        st.image("images/" + row['image'])

    with col4:
        st.write('')

for index, row in data[8:].iterrows():
    with col5:
        st.subheader(row['first name'].title() + " " + row['last name'].title())
        st.markdown(
            f"<span style='font-size: 17px;'>{row['role']}</span>",
            unsafe_allow_html=True
        )
        st.image("images/" + row['image'])
