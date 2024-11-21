import streamlit as st
from references.prompttemplate import template
#from references.jsonschema import json_schema
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

length_text_area = len(original_text_area) if original_text_area else 0
st.write(
    f"You wrote {length_text_area} characters.",
    "\n"
)

#st.markdown("Alternatively, upload a text file")
#st.file_uploader("Browse .txt a file")

json_schema={
  "title": "Bye Bias",
  "description": "A list of biases detected in a text",
  "type": "object",
  "properties": {
    "BiasList": {
      "type": "array",
	  "minItems": 1,
      "uniqueItems": True,
      "items": [
        {
          "type": "object",
          "properties": {
            "BiasId": {
              "type": "integer",
			  "minimum": 1,
			  "description": "The unique identifier for a bias"
            },
            "BiasType": {
              "type": "string",
			  "description": "Name of the bias",
			  "enum": ["Gender", "Racism", "Ageism", "Body type", "Sexuality", "Ideology", "Religion"]
            },
            "BiasDegree": {
              "type": "string",
			  "description": "Score of how strong is the presence of the bias in a intensity scale",
			  "enum": ["Bias free", "Weakly biased", "Moderately biased", "Highly biased", "Extremely biased"]
            },
            "ConfidencePercentage": {
              "type": "integer",
			  "description": "Percentage of how confident the response is",
			  "minimum": 0
            },
            "FragmentsPresent": {
              "type": "array",
			  "minItems": 1,
			  "uniqueItems": True,
			  "description": "List of fragments where the specified bias is detected",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "FragmentId": {
                      "type": "integer",
					  "description": "The unique identifier for a fragment",
					  "minimum": 1
                    },
                    "FragmentContent": {
                      "type": "string",
					  "description": "Quote the fragment where the specified bias was detected from the text"
                    },
                    "FragmentBiasDegree": {
                      "type": "string",
					  "description": "Score of how strong is the presence of the bias in a intensity scale",
					  "enum": ["Bias free", "Weakly biased", "Moderately biased", "Highly biased", "Extremely biased"]
                    },
                    "Reformulations": {
                      "type": "array",
					  "description": "Reformulations based specifically on the specified fragment",
					  "minItems": 3,
					  "maxItems": 3,
					  "uniqueItems": True,
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "ReformulationId": {
                              "type": "integer",
							  "description": "The unique identifier for a reformulation",
							  "minimum": 1
                            },
                            "ReformulationLevel": {
                              "type": "string",
							  "description": "Scale from least to most modified relative to the original fragment",
							  "enum": ["Simple", "Medium", "Complex"]
                            },
                            "AlternativeText": {
                              "type": "string",
							  "description": "The reformulaton or unbiased phrasing of the biased fragment"
                            }
                          },
                          "required": [
                            "ReformulationId",
                            "ReformulationLevel",
                            "AlternativeText"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "FragmentId",
                    "FragmentContent",
                    "FragmentBiasDegree",
                    "Reformulations"
                  ]
                }
              ]
            },
            "Explanation": {
              "type": "string",
			  "description": "Brief explanation of the specified bias"
            }
          },
          "required": [
            "BiasId",
            "BiasType",
            "BiasDegree",
            "ConfidencePercentage",
            "Explanation"
          ]
        }
      ]
    },
    "TuringTest": {
      "type": "boolean",
	  "description": "Wether the text was written by a human or not"
    },
    "Category": {
      "type": "string"
    },
    "Topic": {
      "type": "string"
    },
    "Subtopic": {
      "type": "string"
    }
  },
  "required": [
    "BiasList",
    "TuringTest",
    "Category",
    "Topic",
    "Subtopic"
  ]
}

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
        structured_llm = llm.with_structured_output(json_schema)
        st.session_state.result = structured_llm.invoke(prompt_value)
        st.write(st.session_state.result)
        st.write("See results in Output page:")
        st.page_link(
            page="pages/output.py",
            label=":rainbow[Go to Output]",
            icon="🧩" 
        )
    else:
        st.markdown("Please insert OpenAI API key in Settings :material/settings:")
        st.page_link(
            page="pages/settings.py",
            label="Go to Settings :material/arrow_forward:"
        )
