import streamlit as st

st.title("Results")

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
st.write("Was this answer helpful?")
selected = st.feedback("thumbs")
if selected is not None:
    st.caption(":violet[Thank you for the feedback!]")
    if selected == 1:
        st.balloons()