import streamlit as st
from functions import col_draw, empty_col_draw

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

col_draw(col1, 0, 4)
empty_col_draw(col2)
col_draw(col3, 4, 8)
empty_col_draw(col4)
col_draw(col5, 8, None)
