import streamlit as st
from references.prompttemplate import template
#from langchain.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


st.title("Insert content")


bias_level = [
    "Bias free",
    "Weakly biased",
    "Moderately biased",
    "Highly biased",
    "Extremely biased"
]

if "bias_level" not in st.session_state:
    st.session_state.bias_level = None

bias_list = [
    "Gender",
    "Racism",
    "Ageism",
    "Body type",
    "Sexuality",
    "Ideology",
    "Religion"
]

biases = st.multiselect(
    "What biases are you worried about?",
    bias_list
)

st.write("You selected:", biases)

#Initialize input text, it's copy, and result in session state
if "textinput" not in st.session_state:
    st.session_state.textinput=None

if "textcopy" not in st.session_state:
    st.session_state.textcopy=None

if "result" not in st.session_state:
    st.session_state.result=None


original_text_area = st.text_area(
    label="Text to analyze",
    value=None,
    max_chars=5000,
    help="Please consider the quantity of characters is limited.",
    placeholder="Enter text"
)

st.write(
    f"You wrote {len(original_text_area)} characters.",
    "\n"
)

#st.markdown("Alternatively, upload a text file")
#st.file_uploader("Browse .txt a file")


if st.button(":material/send: Submit"):
    #Set original text and copy in session state
    st.session_state.textinput = original_text_area
    st.session_state.textcopy = original_text_area

    #Set bias classifications in session state
    st.session_state.bias_level = bias_level

    # Turn list arguments into string
    intensity = ", ".join(bias_level)
    include = ", ".join(biases)


    prompt_value = template.format(intensity_scale=intensity, include_biases=include, article=original_text_area)
    
    if st.session_state.openai_api_key is not None:
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            max_tokens=None,
            timeout=50,
            max_retries=2,
            api_key=st.session_state.openai_api_key
            )
        st.session_state.result = llm.invoke(prompt_value)
        #st.write(result)
        st.write("See results in Output page:")
        st.page_link(
            page="pages/output.py",
            label=":rainbow[Go to Output]",
            icon="🧩" 
        )
    else:
        st.markdown("Please insert API key in Settings :material/settings:")
        st.page_link(
            page="pages/settings.py",
            label="Go to Settings :material/arrow_forward:"
        )


"""
{"content":"{\n    \"BiasList\": [\n        {\n            \"BiasId\": 1,\n            \"BiasType\": \"Gender\",\n            \"BiasDegree\": \"Highly biased\",\n            \"ConfidencePercentage\": 80,\n            \"FragmentsPresent\": [\n                {\n                    \"FragmentId\": 1,\n                    \"FragmentContent\": \"Los hombres manejan mejor que las mujeres.\",\n                    \"FragmentBiasDegree\": \"Highly biased\",\n                    \"Reformulations\": [\n                        {\n                            \"ReformulationId\": 1,\n                            \"ReformulationLevel\": \"Simple\",\n                            \"AlternativeText\": \"Los hombres son mejores conductores que las mujeres.\"\n                        },\n                        {\n                            \"ReformulationId\": 2,\n                            \"ReformulationLevel\": \"Medium\",\n                            \"AlternativeText\": \"Se dice que los hombres tienen más habilidades al volante que las mujeres.\"\n                        },\n                        {\n                            \"ReformulationId\": 3,\n                            \"ReformulationLevel\": \"Complex\",\n                            \"AlternativeText\": \"Existen afirmaciones que sugieren que los hombres poseen una mayor destreza en la conducción en comparación con las mujeres.\"\n                        }\n                    ]\n                }\n            ],\n            \"Explanation\": \"El sesgo de género es un sesgo definido como la creencia de que un género es superior o inferior a otro en ciertas habilidades o características.\"\n        }\n    ],\n    \"TuringTest\": true,\n    \"Category\": \"\",\n    \"Topic\": \"\",\n    \"Subtopic\": \"\"\n}","additional_kwargs":{"refusal":null},"response_metadata":{"token_usage":{"completion_tokens":298,"prompt_tokens":522,"total_tokens":820,"completion_tokens_details":{"accepted_prediction_tokens":0,"audio_tokens":0,"reasoning_tokens":0,"rejected_prediction_tokens":0},"prompt_tokens_details":{"audio_tokens":0,"cached_tokens":0}},"model_name":"gpt-4o-mini-2024-07-18","system_fingerprint":"fp_3de1288069","finish_reason":"stop","logprobs":null},"type":"ai","name":null,"id":"run-600cd61f-fba2-41d6-bee8-25638ac3e2e7-0","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":{"input_tokens":522,"output_tokens":298,"total_tokens":820,"input_token_details":{"audio":0,"cache_read":0},"output_token_details":{"audio":0,"reasoning":0}}}
"""