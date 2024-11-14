import streamlit as st

def turing_test(a_dictionary):
    st.subheader("Turing test:")
    if a_dictionary["TuringTest"]:
        st.success("This text was likely written by a human", icon="✅")
    else:
        st.error('This text was likely written by an artificial intelligence', icon="❌")