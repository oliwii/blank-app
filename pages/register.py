import streamlit as st

st.title("Create your account")

st.text_input(
    label="Email",
    placeholder="example@byebias.com"
    )

st.text_input(
    label="Create password",
    placeholder="*******",
    type="password"
)

st.text_input(
    label="Confirm password",
    placeholder="*******",
    type="password"
)

option = st.selectbox(
    label="Select user role",
    options=("Reader", "Business", "Media"),
    index=None,
    help="Choose *Reader* if you want to evaluate other's content.\n Choose *Business* if your company hired ByeBias.\n Choose *Media* if you are a content creator.",
    placeholder="Select role...",
)

st.write("You selected:", option)

st.page_link(
    page="pages/input.py",
    label=":violet[**Next**]"
)