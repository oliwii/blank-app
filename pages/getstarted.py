import streamlit as st

left, right = st.columns(2)
left.page_link(page="pages/signin.py", label="Sign In")
right.page_link(page="pages/register.py", label="Register")
