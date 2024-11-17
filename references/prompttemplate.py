from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", 
    '''You will recieve a news article. Read it and perform the task that follows. Respond with a JSON object of key-value pairs.

Respond only with a JSON file in the following structure. It is important that the keys remain the same; you may only edit the values according to the content of the article. 
Your task is to classify each bias according to its intensity on a scale of {intensity_scale}.

The possible biases are: {include_biases}. Do not include any biases that are not on this list. Include all biases on this list.

In the values for FragmentContent, there should be a text fragment from the article where you have identified the corresponding bias. The reformulations should be based specifically on that fragment, separated into three levels: from least to most modified relative to the original fragment.
Reformulations shoud be in the same language as the original fragment.

Leave the category, topic, and subtopic keys blank.
For the Turing test, respond true if you believe the article was written by a human, false otherwise.

The JSON you should return is as follows:

{{
    "BiasList": [
        {{
            "BiasId": 1,
            "BiasType": "Gender",
            "BiasDegree": "Highly biased",
            "ConfidencePercentage": 80,
            "FragmentsPresent": [
                {{
                    "FragmentId": 1,
                    "FragmentContent": "Los hombres manejan mejor que las mujeres",
                    "FragmentBiasDegree": "Highly biased",
                    "Reformulations": [
                        {{
                            "ReformulationId": 1,
                            "ReformulationLevel": "Simple",
                            "AlternativeText": "bla bla bla"
                        }},
                        {{
                            "ReformulationId": 2,
                            "ReformulationLevel": "Medium",
                            "AlternativeText": "lab lab lab"
                        }},
                        {{
                            "ReformulationId": 3,
                            "ReformulationLevel": "Complex",
                            "AlternativeText": "alb alb alb"
                        }}
                    ]
                }}
            ],
            "Explanation": "El sesgo de género es un sesgo definido como ..."
        }}
    ],
    "TuringTest": true,
    "Category": "Politics",
    "Topic": "Democracy",
    "Subtopic": "Election Security"
}}

It is important that you ONLY return the JSON.'''),
    ("human", "{article}")
])