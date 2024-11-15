import streamlit as st
from references.barchart import barchart
from references.explanation import single_pills
from references.explanation import analysis
from references.explanation import replace_fragment
from references.turingtest import turing_test


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

col1, col2 = st.columns(2)

with col1:
    #Show chart
    st.altair_chart(barchart(example_bias_dict, st.session_state.bias_level, colour_hex, colour_reference))

    # Write analysis
    selected_bias = single_pills(example_bias_dict)
    st.write(f"Your selected option: {selected_bias}.")
    if selected_bias is not None:
        analysis(selected_bias, example_bias_dict)

    # Show Turing test results
    turing_test(example_bias_dict)

with col2:
    with st.container(border=True):
        st.markdown(st.session_state.textcopy + "Lorem Ipsum"*100)

st.divider()
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
st.markdown("##### Was this answer helpful?")
selected = st.feedback("thumbs")
if selected is not None:
    st.caption(":violet[Thank you for the feedback!]")
    if selected == 1:
        st.balloons()