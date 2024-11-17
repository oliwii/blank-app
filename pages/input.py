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
    "Religion",
]

biases = st.multiselect(
    "What biases are you worried about?",
    bias_list
)

st.write("You selected:", biases)

#Initialize input text in session state
if "textinput" not in st.session_state:
    st.session_state.textinput = None

if "textcopy" not in st.session_state:
    st.session_state.textcopy=None

original_text_area = st.text_area(
    label="Text to analyze",
    value="Los hombres manejan mejor que las mujeres",
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


    prompt_value = template.format({"intensity_scale": intensity, "include_biases": include, "article": original_text_area})
    
    if st.session_state.openai_api_key is not None:
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            max_tokens=None,
            timeout=50,
            max_retries=2,
            api_key=st.session_state.openai_api_key
            )
        result = llm.invoke(prompt_value)
        st.write(result)
    else:
        st.markdown("Please insert API key in Settings")
        st.page_link(
            page="pages/settings.py",
            label="Go to Settings :material/arrow_forward:"
        )

    st.write("See results in Output page")
    st.page_link(
        page="pages/output.py",
        label=":rainbow[Go to Output]",
        icon="🧩" 
    )
