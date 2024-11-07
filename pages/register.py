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

if "role" not in st.session_state:
    st.session_state.role = None

OPTIONS = ("Reader", "Business", "Media")

role = st.selectbox(
    label="Select user role",
    options=OPTIONS,
    index=None,
    help="Choose *Reader* if you want to evaluate other's content.\n Choose *Business* if your company hired ByeBias.\n Choose *Media* if you are a content creator.",
    placeholder="Select role...",
)

st.write("You selected:", role)

if role in OPTIONS:
    st.session_state.role = role
    st.write(st.session_state.role)

agree = st.checkbox("I agree with Terms and Conditions")

st.write("hello")


if st.session_state.role is not None:
    st.session_state.role = role
    st.session_state.role

st.page_link(
    page="pages/input.py",
    label=":violet[**Next**]",
    disabled=not(agree)
)
