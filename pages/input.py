import streamlit as st

st.title("Insert content")

biases = st.multiselect(
    "What biases are you worried about?",
    ["Genre","Racism","Ageism", "Body type", "Sexuality", "Ideology", "Religion"],
)

st.write("You selected:", biases)

txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)

st.write(f"You wrote {len(txt)} characters.",
         "\n"
         )

if st.button(":material/send: Submit"):
    st.switch_page("pages/output.py")

