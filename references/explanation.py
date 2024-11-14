import streamlit as st

st.markdown(st.session_state.textinput)

bias_shown = st.selectbox(
    label="Select bias",
    options=bias_selected,
    index=None,
    placeholder="Select bias...",
)

st.title(bias_shown)

def get_fragments(dictionary):
    #For each fragment, I want the quote, 
    # a suggestion and a button to allow a replace.
    for items in dictionary["FragmentsPresent"]:
        



def explanation(dictionary):
    # Create a markdown string for the list
    markdown_text = ""

    for item in dictionary["BiasList"]:
        markdown_text += f"- {item["BiasType"]}\n"
        for subitem in item:
            



    for item, subitems in dictionary:
        markdown_text += f"- {BiasType}\n"  # BiasType
        for subitem in subitems:
            markdown_text += f"    - {subitem}\n"  # Indented subitems

    # Display the list in Streamlit
    st.markdown(markdown_text)

    exp = ""
    for bias in dictionary["BiasList"]:
        exp += "- "+bias["BiasType"] + "/n" + bias["Explanation"]

    st.write(exp)




'''
import streamlit as st

st.markdown(
- Main item 1
    - Subitem 1.1
    - Subitem 1.2
        - Sub-subitem 1.2.1
- Main item 2
    - Subitem 2.1
""")
'''


'''
import streamlit as st

st.markdown(
- Main item 1
    - Subitem 1.1
    - Subitem 1.2
        - Sub-subitem 1.2.1
- Main item 2
    - Subitem 2.1
""")
'''