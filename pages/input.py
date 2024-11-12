import streamlit as st
import altair as alt
import pandas as pd
from langchain.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain.chat_models import ChatOpenAI

st.title("Insert content")

openai_api_key = st.text_input(
    "OpenAI API Key",
    type="password"
)

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

txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)

st.write(
    f"You wrote {len(txt)} characters.",
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

prompt_template = PromptTemplate.from_template(
    '''
The following is a news article. Read it and perform the task that follows. Respond with a JSON object of key-value pairs.

####################

{article}

####################

Respond only with a JSON file in the following structure. It is important that the keys remain the same; you may only edit the values according to the content of the article. Your task is to classify each bias according to its intensity on a scale of ["Bias free", "Weakly biased", "Moderately biased", "Highly biased", "Extremely biased"].

The possible biases are: ["Gender", "Racism", "Ageism", "Body type", "Sexuality", "Ideology", "Religion"]. Do not include any biases that are not on this list.

In the values for FragmentContent, there should be a text fragment from the article where you have identified the corresponding bias. The reformulations should be based specifically on that fragment, separated into three levels: from least to most modified relative to the original fragment.

Leave the category, topic, and subtopic keys blank.
For the Turing test, respond True if you believe the article was written by a human, False otherwise.

The JSON you should return is as follows:

{
	"BiasList": [
		{
			"BiasId": 1,
			"BiasType": "Gender",
			"BiasDegree": "Highly biased",
			"ConfidencePercentage": 80,
			"FragmentsPresent": {
				"items": [
					{
						"FragmentId": 1,
						"FragmentContent": "Los hombre manejan mejor que las mujeres",
						"FragmentBiasDegree": "Highly biased",
						"Reformulations": {
							"items": [
								{
									"ReformulationId": 1,
									"ReformulationLevel": "Simple",
									"AlternativeText": "bla bla bla"
								},
								{
									"ReformulationId": 2,
									"ReformulationLevel": "Medium",
									"AlternativeText": "bla bla bla"
								},
								{
									"ReformulationId": 3,
									"ReformulationLevel": "Complex",
									"AlternativeText": "bla bla bla"
								}
							],
						}
					}
				]
			},
			"Explanation": "Gender bias is a bias defined as ..."
		}
	],
	"TuringTest": True/False,
	"Category": "Politics",
	"Topic": "Democracy",
	"Subtopic": "Election Security"
}

It is important that you ONLY return the JSON.

'''
)
prompt_template.format(article=txt)

def bias_barChart(response):
    # Obtain the biases types from the output
    # Obtain the degrees or categorization for each bias from the output
    categories = []
    degrees = []
    colors = []
    for item in response["BiasList"]:
        categories.append(item["BiasType"])
        degrees.append(item["BiasDegree"])
        colors.append(colour_reference[item["BiasDegree"]])

    # Define colors for each bias level
    color_scale = alt.Scale(
        domain=bias_level,
        range=colour_hex
    )

    # Define the data in tabular format
    data = pd.DataFrame({
        'Category': categories,
        'Degree': degrees,
        'Bias_Index': colors  # These indices map to the colors
    })

    # Create the Altair chart
    chart = alt.Chart(data).mark_bar().encode(
        y=alt.Y('Category', sort='-x', title=""),
        x=alt.X('Bias_Index:O', axis=alt.Axis(title="Bias Degree", labels=False)),
        color=alt.Color('Degree', scale=color_scale, legend=alt.Legend(title="Bias Degree"))
    ).properties(
        title="Content Analysis",
        width=400,
        height=200
    )

    # Display the chart
    chart

def explanation(response):
    exp = []
    for bias in response["BiasList"]:
        exp.append(bias["Explanation"])
    st.write(exp)

def turing_test(response):
    st.subheader("Turing test:")
    if response["TuringTest"] == True:
        st.success("This text was likely written by a human", icon="✅")
    else:
        st.error('This text was likely written by an artificial intelligence', icon="❌")

if st.button(":material/send: Submit"):
    #bias_barChart()
    #explanation()
    #turing_test()
    st.switch_page("pages/output.py")

input_dict = {
    "BiasList": [
            {
                "BiasId": 1,
                "BiasType": "Gender",
                "BiasDegree": "Highly biased",
                "ConfidencePercentage": 80,
                "FragmentsPresent": {
                    "items": [
                        {
                            "FragmentId": 1,
                            "FragmentContent": "Los hombres manejan mejor que las mujeres",
                            "FragmentBiasDegree": "Highly biased",
                            "Reformulations": {
                                "items": [
                                    {
                                        "ReformulationId": 1,
                                        "ReformulationLevel": "Weak",
                                        "AlternativeText": "bla bla bla"
                                    },
                                    {
                                        "ReformulationId": 2,
                                        "ReformulationLevel": "Medium",
                                        "AlternativeText": "Bla Bla Bla"
                                    },
                                    {
                                        "ReformulationId": 3,
                                        "ReformulationLevel": "Strong",
                                        "AlternativeText": "BLA BLA BLA"
                                    }
                                ],
                            }
                        }
                    ]
                },
                "Explanation": "Gender bias is a bias defined as ..."
            }
        ],
        "TurningTest": True,
        "Category": "Politics",
        "Topic": "Democracy",
        "Subtopic": "Election Security"
}

# Obtain the biases types from the output
# Obtain the degrees or categorization for each bias from the output
categories = []
degrees = []
colors = []
for item in input_dict["BiasList"]:
    categories.append(item["BiasType"])
    degrees.append(item["BiasDegree"])
    colors.append(colour_reference[item["BiasDegree"]])

# Define colors for each bias level
color_scale = alt.Scale(
    domain=bias_level,
    range=colour_hex
)

# Define the data in tabular format
data = pd.DataFrame({
    'Category': categories,
    'Degree': degrees,
    'Bias_Index': colors  # These indices map to the colors
})

# Create the Altair chart
chart = alt.Chart(data).mark_bar().encode(
    y=alt.Y('Category', sort='-x', title=""),
    x=alt.X('Bias_Index:O', axis=alt.Axis(title="Bias Degree", labels=False)),
    color=alt.Color('Degree', scale=color_scale, legend=alt.Legend(title="Bias Degree"))
).properties(
    title="Content Analysis",
    width=400,
    height=200
)

# Display the chart
chart