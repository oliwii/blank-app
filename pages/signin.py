import streamlit as st

st.title("Sign In")

st.text_input(
    label="Email",
    placeholder="example@byebias.com"
    )

st.text_input(
    label="Password",
    placeholder="*******",
    type="password"
    )

st.page_link(
    page="pages/register.py",
    label=":violet[**Next**]"
    )