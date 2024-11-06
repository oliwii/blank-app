import streamlit as st

def contact_form():
    with st.form("contact_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email Adress")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.success("🎉 Message successfully sent!")