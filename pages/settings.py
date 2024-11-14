import streamlit as st

st.title("Settings")
st.write("Please insert OpenAI API key")

if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = None

openai_api_key = st.text_input(
    "OpenAI API Key",
    type="password"
)

if openai_api_key.startswith("sk-"):
    st.session_state.openai_api_key = openai_api_key