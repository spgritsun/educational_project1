import streamlit as st
import pandas as pd

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
