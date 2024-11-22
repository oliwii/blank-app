import streamlit as st
from references.barchart import barchart
from references.explanation import single_pills
from references.explanation import analysis
from references.explanation import replace_fragment
from references.turingtest import turing_test

"""
StreamlitDuplicateElementId: There are multiple `button` elements with the same 

auto-generated ID. When this element is created, it is assigned an internal ID 

based on the element type and provided parameters. Multiple elements with the 

same type and parameters will cause this error.


To fix this error, please pass a unique `key` argument to the `button` element."""


example_bias_dict = {
	"BiasList": [
		{
			"BiasId": 1,
			"BiasType": "Gender",
			"BiasDegree": "Highly biased",
			"ConfidencePercentage": 80,
			"FragmentsPresent": [
				{
					"FragmentId": 1,
					"FragmentContent": "Los hombres manejan mejor que las mujeres",
					"FragmentBiasDegree": "Highly biased",
					"Reformulations": [
						{
							"ReformulationId": 1,
							"ReformulationLevel": "Simple",
							"AlternativeText": "bla bla bla"
						},
						{
							"ReformulationId": 2,
							"ReformulationLevel": "Medium",
							"AlternativeText": "lab lab lab"
						},
						{
							"ReformulationId": 3,
							"ReformulationLevel": "Complex",
							"AlternativeText": "abl abl abl"
						}
                	]
            	}
            ],
			"Explanation": "Gender bias is a bias defined as ..."
		}
	],
	"TuringTest": True,
	"Category": "Politics",
	"Topic": "Democracy",
	"Subtopic": "Election Security"
}

###########


st.title("Results")


colour_reference = {
     "Bias free": 0,
     "Weakly biased": 1,
     "Moderately biased": 2,
     "Highly biased": 3,
     "Extremely biased": 4
}

colour_hex = [
    "#6ABD45",
    "#FFC107",
    "#FF9800",
    "#F44336",
    "#D32F2F"
]

#Show chart
st.altair_chart(barchart(st.session_state.parsed_result, st.session_state.bias_level, colour_hex, colour_reference))

# Write analysis
selected_bias = single_pills(st.session_state.parsed_result)
st.write(f"Your selected option: {selected_bias}.")
if selected_bias is not None:
    analysis(selected_bias, st.session_state.parsed_result)
    undo_button = st.button(
        label = "Undo changes",
        icon = ":material/undo:"
	)
    if undo_button:
          st.session_state.textcopy = st.session_state.textinput

# Show Turing test results
turing_test(st.session_state.parsed_result)

with st.container(border=True):
    st.markdown(st.session_state.textcopy)

st.divider()

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
st.markdown("##### Was this answer helpful?")
selected = st.feedback("thumbs")
if selected is not None:
    st.caption(":violet[Thank you for the feedback!]")
    if selected == 1:
        st.balloons()
        
holidays = st.button(
    label="Happy holidays!",
    icon="❄️"
)
if holidays:
    st.snow()