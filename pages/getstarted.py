import streamlit as st

left, right = st.columns(2)
left.page_link(page="pages/signin.py", label="Sign In")
right.page_link(page="pages/register.py", label="Register")

st.markdown("# Plans")
col1, col2, col3, col4 = st.columns(4)

#"✓"
#"✗"

#st.markdown("# Hello 1")
#st.markdown("## Hello 2")
#st.markdown("### Hello 3")
#st.markdown("#### Hello 4")
#st.markdown("##### Hello 5")
#st.markdown("###### Hello 6")
#st.write("Hello write")
#st.text("Hello text")
#st.markdown("####### Hello 7")
#st.markdown("######## Hello 8")
#st.markdown("######### Hello 9")


with col1:
    container = st.container(border=True)
    container.markdown("Free")
    container.markdown("## $0")
    container.markdown("###### p/month")
    container.markdown("Ideal for users who want an introduction to :violet[Bye Bias]")
    texto1 = """
    <p>✓ Basic bias analysis</p>
    <p>✓ Dashboard</p>
    <p>✓ Limited words</p>
    <p>✓ Simple-level reformulation</p>
    <p>✗ No image analysis</p>
    """
    container.markdown(texto1, unsafe_allow_html=True)
    container.button(
        label="Start for free",
        icon="🌱"
    )
    

with col2:
    container = st.container(border=True)
    container.markdown("Pro")
    container.markdown("## $10") 
    container.markdown("###### p/month")
    container.caption("*:blue-background[Best deal :material/bolt:]*")
    container.markdown("Free features +")
    texto2 = """
    <p>✓ Complete bias analysis</p>
    <p>✓ Advanced insights</p>
    <p>✓ Illimited words</p>
    <p>✓ Three reformulation levels</p>
    <p>✓ Image analysis</p>
    <p>✓ AI text detection</p>
    """
    container.markdown(texto2, unsafe_allow_html=True)
    container.button(
        label="Get Pro",
        icon=":material/arrow_forward:",
        disabled = True
    )

with col3:
    container = st.container(border=True)
    container.markdown("Basic")
    container.markdown("## $25")
    container.markdown("###### p/month")
    container.markdown("For small businesses seeking an introduction to bias analysis in their communication.")
    texto3="""
    <p>✓ Complete bias analysis</p>
    <p>✓ Dashboard</p>
    <p>✓ 100 queries a month</p>
    <p>✓ Two reformulation levels: simple and complex</p>
    <p>✓ Up to 5 users</p>
    <p>✗ No image analysis</p>
    """
    container.markdown(texto3, unsafe_allow_html=True)
    container.button(
        label="Get Basic",
        icon=":material/arrow_forward:",
        disabled = True
    )

with col4:
    container = st.container(border=True)
    container.markdown("Business")
    container.markdown("## $100")
    container.markdown("###### p/month")
    container.caption("*:violet-background[Recommended :material/bolt:]*")
    container.markdown("Basic plan fratures +")
    texto4="""
    <p>✓ Advanced insights</p>
    <p>✓ Illimited use</p>
    <p>✓ Three reformulation levels</p>
    <p>✓ Image analysis</p>
    <p>✓ AI text detection</p>
    """
    container.markdown(texto4, unsafe_allow_html=True)
    container.button(
        label="Get Business",
        icon=":material/arrow_forward:",
        disabled = True
    )