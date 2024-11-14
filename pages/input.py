import streamlit as st
#from references.prompttemplate import format_prompt
from references.barchart import barchart
from references.explanation import single_pills
from references.turingtest import turing_test
#from langchain.llms import OpenAI
#from langchain_core.prompts import PromptTemplate
#from langchain_openai.chat_models import ChatOpenAI
#from langchain.chat_models import ChatOpenAI

st.title("Insert content")

bias_level = [
    "Bias free",
    "Weakly biased",
    "Moderately biased",
    "Highly biased",
    "Extremely biased"
]

bias_list = [
    "Gender",
    "Racism",
    "Ageism",
    "Body type",
    "Sexuality",
    "Ideology",
    "Religion",
]

biases = st.multiselect(
    "What biases are you worried about?",
    bias_list
)

st.write("You selected:", biases)

if "textinput" not in st.session_state:
    st.session_state.textinput = None

original_text = st.text_area(
    label="Text to analyze",
    value=None,
    placeholder="Enter text"
)

st.write(
    f"You wrote {len(original_text)} characters.",
    "\n"
)

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

if st.button(":material/send: Submit"):
    st.session_state.textinput = original_text
    #format_prompt(original_text, biases, bias_level)
    #llamar a openai funcion(prompt_template.invoke({"article": txt}))
    #barchart()
    #selected_bias=single_pills(diccionario)
    #st.write(f"Your selected option: {selected_bias}.")
    #analysis(selected_bias, diccionario)
    turing_test()
    st.switch_page("pages/output.py")

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
							"AlternativeText": "alb alb alb"
						}
                	]
            	}
            ],
			"Explanation": "Gender bias is a bias defined as ..."
		}
	],
	"TuringTest": True/False,
	"Category": "Politics",
	"Topic": "Democracy",
	"Subtopic": "Election Security"
}


sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
st.markdown("#### Was this answer helpful?")
selected = st.feedback("thumbs")
if selected is not None:
    st.caption(":violet[Thank you for the feedback!]")
    if selected == 1:
        st.balloons()