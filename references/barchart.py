import altair as alt
import pandas as pd

def barchart(dictionary, classification, hex_colour, colour_ref):
    # Obtain the biases types from the output
    # Obtain the degrees or categorization for each bias from the output
    categories = []
    degrees = []
    colors = []
    for item in dictionary["BiasList"]:
        categories.append(item["BiasType"])
        degrees.append(item["BiasDegree"])
        colors.append(colour_ref[item["BiasDegree"]])

    # Define colors for each bias level
    color_scale = alt.Scale(
        domain=classification,
        range=hex_colour
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
        x=alt.X('Bias_Index:O', axis=alt.Axis(title="Bias Degree", labels=False)),
        color=alt.Color('Degree', scale=color_scale, legend=alt.Legend(title="Bias Degree"))
    ).properties(
        title="Content Analysis",
        width=400,
        height=200
    )

    # Display the chart
    chart