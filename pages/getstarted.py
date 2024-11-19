import streamlit as st

left, right = st.columns(2)
left.page_link(page="pages/signin.py", label="Sign In")
right.page_link(page="pages/register.py", label="Register")

st.markdown("# Plans")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

st.markdown(
    ":material/check_small: Basic analysis\n"
    ":material/check_small: Dashboard\n" 
    ":material/check_small: Limited words\n"
    ":material/check_small: Simple-level reformulation\n"
    ":material/close_small: No image analysis"
)

with col1:
    container = st.container(border=True)
    container.markdown("Free")
    container.markdown("### $0 p/month")
    container.markdown("Ideal for users who want an introduction to :violet[Bye Bias]")
    container.markdown(
    ":material/check_small: Basic analysis\n"
    ":material/check_small: Dashboard\n" 
    ":material/check_small: Limited words\n"
    ":material/check_small: Simple-level reformulation\n"
    ":material/close_small: No image analysis"
)
    #container.markdown(":material/check_small: Basic analysis"+"\n"+":material/check_small: Dashboard"+"\n"+":material/check_small: Limited words"+"\n"+":material/check_small: Simple-level reformulation"+"\n"+":material/close_small: No image analysis")
    container.button(
        label="Start for free",
        icon="🌱"
    )

with col2:
    container = st.container(border=True)
    container.markdown("Pro")
    container.markdown("### $10 p/month")
    container.caption("*:blue[Best deal :material/bolt:]*")
    container.markdown("Free features +")
    container.markdown("""
                    - Complete analysis
                    - Advanced insights
                    - Illimited words
                    - Three reformulation levels
                    - Image analysis
                    - AI text detection
                       """)
    #container.markdown(":material/check_small: Complete analysis"+"\n"+":material/check_small: Advanced insights"+"\n"+":material/check_small: Illimited words"+"\n"+":material/check_small: Three reformulation levels"+"\n"+":material/check_small: Image analysis"+"\n"+":material/check_small: AI text detection")
    container.button(
        label="Get Pro",
        icon=":material/arrow_forward:",
        disabled = True
    )

with col3:
    container = st.container(border=True)
    container.markdown("Basic")
    container.markdown("### $25 p/month")
    container.markdown("For small businesses seeking an introduction to bias analysis in their communication.")
    container.markdown(":material/check_small: Complete analysis"+"\n"+":material/check_small: Advanced insights"+"\n"+":material/check_small: 100 queries a month"+"\n"+":material/check_small: Two reformulation levels: simple and complex"+"\n"+":material/check_small: Up to 5 users"+"\n"+":material/close_small: No image analysis")
    container.button(
        label="Get Basic",
        icon=":material/arrow_forward:",
        disabled = True
    )

with col4:
    container = st.container(border=True)
    container.markdown("Business")
    container.markdown("### $100 p/month")
    container.caption("*:gray[Recommended :material/bolt:]*")
    container.markdown("Basic plan fratures +")
    container.markdown("""
                       :material/check_small: Advanced insights
                       :material/check_small: Illimited words
                       :material/check_small: Three reformulation levels
                       :material/check_small: Image analysis
                       :material/check_small: AI text detection
    """)
    container.button(
        label="Get Business",
        icon=":material/arrow_forward:",
        disabled = True
    )