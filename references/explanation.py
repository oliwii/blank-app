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

def analysis(bias, bias_analysis_result):
    #Write the item (bias) selected
    st.markdown(f"# {bias}")
    #Write the description: definition and explanation.
    #dictionary["BiasList"] returns a list with the different biases chosen to analyze.
    #Find the bias selected previously in the BiasList list, and show it's explanation.
    #item in this cycle is a dictionary because BiasList is a list of dictionaries.
    button_dict={}
    for item in bias_analysis_result["BiasList"]:
        if item["BiasType"] == bias:
            st.markdown(item["Explanation"])
            st.markdown(f"## Fragments where {bias} bias was detected:")
            #fragment is a dictionary of the list item["FragmentsPresent"]
            for fragment in item["FragmentsPresent"]:
                st.markdown(f" {fragment['FragmentContent']}.  **{fragment['FragmentBiasDegree']}**.")
                st.markdown("### Possible reformulations")
                st.markdown(fragment["Reformulations"][0]["AlternativeText"])
                st.button(label="Apply Simple")
#                button_dict[f"{fragment["FragmentId"]},1"]=st.button(label="Apply Simple")
                st.markdown(fragment["Reformulations"][1]["AlternativeText"])               
                st.button(label="Apply Medium")
#                button_dict[f"{fragment["FragmentId"]},2"]=st.button(label="Apply Medium")
                st.markdown(fragment["Reformulations"][2]["AlternativeText"])
                st.button(label="Apply Complex")
#                button_dict[f"{fragment["FragmentId"]},3"]=st.button(label="Apply Complex")


#def apply(level,bias_analysis_result):
#    st.button()

                

#def get_fragments(dictionary):
    #For each fragment, I want the quote, 
    # a suggestion and a button to allow a replace.