import streamlit as st

st.title("Results")

st.write("Was this answer helpful?")
selected = st.feedback("thumbs")
if selected is not None:
    st.caption("Thank you for the feedback!")