import streamlit as st

def single_pills(dictionary):
    bias_options = []
    #Iterar en los elementos de la lista BiasList
    for bias in dictionary["BiasList"]:
        if bias["BiasDegree"] is not "Bias free":
            bias_options.append(bias["BiasType"])
    selection = st.pills(
        label="Bias",
        options=bias_options,
        selection_mode="single",
        help="Only the biases that have been identified as present are shown."
    )
    return selection
#    st.markdown(f"Your selected option: {selection}.")

def replace_fragment(text, previous_fragment, new_fragment):
    # Check if the exact fragment is in the text
    if previous_fragment in text:
        # Apply :color-background syntax for highlighting
        highlighted_new_fragment = f":green-background[{new_fragment}]"
        # Replace the exact match with the new fragment
        text = text.replace(previous_fragment,highlighted_new_fragment)
    return text

def analysis(bias, bias_analysis_result):
    #Write the item (bias) selected
    st.markdown(f"### {bias}")

    #Write the description: definition and explanation.
    #dictionary["BiasList"] returns a list with the different biases chosen to analyze.
    #Find the bias selected previously in the BiasList list, and show it's explanation.
    #item in this cycle is a dictionary because BiasList is a list of dictionaries.
    #button_dict={}

    for item in bias_analysis_result["BiasList"]:
        if item["BiasType"] == bias:
            st.markdown(item["Explanation"])
            st.markdown(f"#### Fragments where {bias} bias was detected:")
            #fragment is a dictionary of the list item["FragmentsPresent"]
            for fragment in item["FragmentsPresent"]:
                st.markdown(f" *{fragment['FragmentContent']}*.  **{fragment['FragmentBiasDegree']}**.")
                st.markdown("##### Possible reformulations")

                simple_reformulation = st.markdown(fragment["Reformulations"][0]["AlternativeText"])
                simple_button = st.button(label="Apply Simple")
                if simple_button:
                    st.markdown(replace_fragment(st.session_state.textcopy, fragment["FragmentContent"], simple_reformulation))

                meduim_reformulation = st.markdown(fragment["Reformulations"][1]["AlternativeText"])               
                medium_button = st.button(label="Apply Medium")
                if medium_button:
                    st.markdown(replace_fragment(st.session_state.textcopy, fragment["FragmentContent"], meduim_reformulation))

                complex_reformulation = st.markdown(fragment["Reformulations"][2]["AlternativeText"])
                complex_button = st.button(label="Apply Complex")
                if complex_button:
                    st.markdown(replace_fragment(st.session_state.textcopy, fragment["FragmentContent"], complex_reformulation))
