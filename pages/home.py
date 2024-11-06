import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact Us")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
st.image(
    "./assets/byebias.png", 
    width=400
    )
st.write("\n")
st.subheader(":violet[Be aware, don't beware]")
st.write("\n")
st.page_link(page="pages/getstarted.py",
                label=":rainbow[**Get Started**]",
                icon="🚀"
                )
st.write("\n")
col1, col2, col3 = st.columns(3,
                                 gap="small",
                                 )
with col1:
    st.markdown("**What is :violet[ByeBias]?**")
    st.markdown(
        body=":violet[ByeBias] :gray[is a revolutionary tool that uncovers hidden biases, enabling users to express their ideas in a more inclusive and fair way.]"
    )
with col2:
    st.markdown("**How does :violet[ByeBias] improve my way of communicating?**")
    st.markdown(
        body=":violet[ByeBias] :gray[improves the way you communicate by identifying biases and offering alternatives, ensuring that your message is clear, inclusive, and free from unwanted stereotypes.]"
    )
with col3:
    st.markdown("**Can I customize the level of change that :violet[ByeBias] offers?**")
    st.markdown(":gray[Yes!] :violet[ByeBias] :gray[provides various levels of suggestions, from subtle adjustments to more significant changes, allowing you to choose how much you want to modify your content while maintaining your original tone and message.]")

if st.button(":material/mail: Contact Us"):
    show_contact_form()