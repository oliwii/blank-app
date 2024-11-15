import streamlit as st

def turing_test(a_dictionary):
    st.markdown("### Turing test:")
    if a_dictionary["TuringTest"]:
        st.success("This text was likely written by a human :material/psychology:", icon="✅")
    else:
        st.error('This text was likely written by an artificial intelligence :material/robot_2', icon="❌")