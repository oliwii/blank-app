import streamlit as st

st.title("Insert content")

bias_list = [
    "Gender",
    "Racism",
    "Ageism",
    "Body type",
    "Sexuality",
    "Ideology",
    "Religion",
    "aaa"
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

input_dict = {
    "BiasList": [
            {
                "BiasId": 1,
                "BiasType": "Gender",
                "BiasDegree": "Red",
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


