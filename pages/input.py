import streamlit as st
#from references.prompttemplate import format_prompt
from references.barchart import barchart
from references.explanation import single_pills
from references.explanation import analysis
from references.turingtest import turing_test
#from langchain.llms import OpenAI
from langchain_core.prompts import PromptTemplate
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

st.markdown("Alternatively, upload a text file")
st.file_uploader("Browse .txt a file")


if st.button(":material/send: Submit"):
    #Set original text and copy in session state
    st.session_state.textinput = original_text_area
    st.session_state.textcopy = original_text_area

    #Set bias classifications in session state
    st.session_state.bias_level = bias_level

    #format_prompt(original_text, biases, bias_level)
    #llamar a openai funcion(prompt_template.invoke({"article": txt}))

    st.write("See results in Output page")
    st.page_link(
        page="pages/output.py",
        label=":rainbow[Go to Output]",
        icon="🧩" #":material/arrow_forward:"
    )
