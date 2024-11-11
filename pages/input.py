import streamlit as st
import altair as alt
import pandas as pd

st.title("Insert content")

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

st.write(f"You wrote {len(txt)} characters.",
         "\n"
         )

if st.button(":material/send: Submit"):
    st.switch_page("pages/output.py")

bias_level = [
    "Bias free",
    "Weakly biased",
    "Moderately biased",
    "Highly biased",
    "Extremely biased"
]

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
                            "FragmentBiasDegree": "Red",
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

colour_reference = {
     "Bias free": 0,
     "Weakly biased": 1,
     "Moderately biased": 2,
     "Highly biased": 3,
     "Extremely biased": 4
}

colour_rgb = [
    "#6ABD45",
    "#FFC107",
    "#FF9800",
    "#F44336",
    "#D32F2F"
]

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
    range=colour_rgb
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
    x=alt.X('Bias_Index:O', axis=alt.Axis(title="Nivel de Sesgo", labels=False)),
    color=alt.Color('Degree', scale=color_scale, legend=alt.Legend(title="Nivel de Sesgo"))
).properties(
    title="Análisis de Contenido",
    width=400,
    height=200
)

# Display the chart
chart
   

