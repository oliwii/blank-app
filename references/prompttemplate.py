from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", 
    '''You will recieve a news article. Read it and perform the task that follows. Respond with a JSON object of key-value pairs.

Respond only with a JSON file in the following structure. It is important that the keys remain the same; you may only edit the values according to the content of the article. 
Your task is to classify each bias according to its intensity on a scale of {intensity_scale}.

The possible biases are: {include_biases}. Do not include any biases that are not on this list. Always include all biases on this list. 
There should be one element per bias in "BiasList", so the length of "BiasList" is the same as the possible biases.

In the values for FragmentContent, there should be a text fragment from the article where you have identified the corresponding bias. The reformulations should be based specifically on that fragment, separated into three levels: from least to most modified relative to the original fragment.
Reformulations are different versions of the original fragment that correct the bias but still conserve the writer's main intention and message. The reformulations and the explanation shoud be in the same language as the original fragment.

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
        }},
        {{
            "BiasId": 2,
            "BiasType": "Sexuality",
            "BiasDegree": "Moderately biased",
            "ConfidencePercentage": 97,
            "FragmentsPresent": [
                {{
                    "FragmentId": 1,
                    "FragmentContent": "Las parejas homosexuales son divertidas",
                    "FragmentBiasDegree": "Moderately biased",
                    "Reformulations": [
                        {{
                            "ReformulationId": 1,
                            "ReformulationLevel": "Simple",
                            "AlternativeText": "xyz"
                        }},
                        {{
                            "ReformulationId": 2,
                            "ReformulationLevel": "Medium",
                            "AlternativeText": "wxy"
                        }},
                        {{
                            "ReformulationId": 3,
                            "ReformulationLevel": "Complex",
                            "AlternativeText": "vwx"
                        }}
                    ]
                }},
                {{
                    "FragmentId": 2,
                    "FragmentContent": "Los niños criados por parejas homosexuales son más abiertos de mente",
                    "FragmentBiasDegree": "Weakly biased",
                    "Reformulations": [
                        {{
                            "ReformulationId": 1,
                            "ReformulationLevel": "Simple",
                            "AlternativeText": "abc"
                        }},
                        {{
                            "ReformulationId": 2,
                            "ReformulationLevel": "Medium",
                            "AlternativeText": "bcd"
                        }},
                        {{
                            "ReformulationId": 3,
                            "ReformulationLevel": "Complex",
                            "AlternativeText": "cde"
                        }}
                    ]
                }}
            ],
            "Explanation": "El sesgo de orientación sexual es definido como ..."
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