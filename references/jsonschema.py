json_schema={
  "title": "Bye Bias",
  "description": "A list of biases detected in a text",
  "type": "object",
  "properties": {
    "BiasList": {
      "type": "array",
	  "minItems": 1,
      "uniqueItems": true,
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
			  "uniqueItems": true,
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
					  "uniqueItems": true,
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