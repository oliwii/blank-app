import streamlit as st

st.title("Results")

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

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
st.write("Was this answer helpful?")
selected = st.feedback("thumbs")
if selected is not None:
    st.caption(":violet[Thank you for the feedback!]")
    if selected == 1:
        st.balloons()