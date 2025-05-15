import streamlit as st

st.set_page_config(
    page_title="My App",
    layout="wide"
)

# Явно перечислите страницы (опционально)
st.sidebar.markdown("""
- [Page 1](?page=page1)
- [Page 2](?page=page2)
""")