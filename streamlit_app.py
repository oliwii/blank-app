import streamlit as st


# --- PAGE SETUP ---

home_page = st.Page(
    page = "pages/home.py",
    title = "Home",
    icon = ":material/home:",
    default = True
)

get_started_page = st.Page(
    page = "pages/getstarted.py",
    title = "Get started",
    icon = ":material/cheer:",
)

sign_in_page = st.Page(
    page = "pages/signin.py",
    title = "Sign in",
    icon = ":material/account_circle:"
)

register_page = st.Page(
    page = "pages/register.py",
    title = "Register",
    icon = ":material/person_add:"
)

input_page = st.Page(
    page = "pages/input.py",
    title = "Insert content",
    icon = ":material/arrow_insert:",
)

output_page = st.Page(
    page = "pages/output.py",
    title = "Results",
    icon = ":material/output_circle:",
)

# --- NAVIGATION SETUP ---
pg = st.navigation(
    pages = [
        home_page,
        get_started_page,
        sign_in_page,
        register_page,
        input_page,
        output_page
    ]
)

# --- ON ALL PAGES --
st.logo("assets/byebias.png", size="large")
st.sidebar.subheader(":violet[Be aware, don't beware]")

# --- RUN NAVIGATION ---
pg.run()

