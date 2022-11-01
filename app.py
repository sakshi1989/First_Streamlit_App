from turtle import color
import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data


@st.cache()
def get_data(n):
    return np.random.rand(n)


st.header('Homework 1')

st.markdown(
    "**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
    "Create a datframe where the x axis limit is 100 and the y values are random values.\n"
    "Print the dataframe you create and use the following code block to help get you started"
)

x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0, x_limit, 1)

# Create a random array of data that we will use for our y values
y_data = get_data(100)

df = pd.DataFrame({'x': x_axis,
                   'y': y_data})
st.write(df)


st.markdown(
    "**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
    "Use the following code block to help get you started."
)

scatter = alt.Chart(df).mark_point().encode(x='x', y='y')

st.altair_chart(scatter, use_container_width=True)


st.markdown(
    "**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
    "https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
    "Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
    "To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
    "https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("""
The 5 changes I made were:
- _Connecting the points of the y-axis through line ordered by the x-axis_
- _Added the color column [c] in the dataframe which will have 4 distinct colors, and added that column in the color option to show lines with color_
- _Created a tooltip to show x, y & c value_
- _Created a radiobutton options which will allow to either see only the particular color data points or all color points together_
- _Made the graph interactive which will allow to zoom-out/zoom-in the graph. Additionally, also added the custom legend_
""")

# I do not want data to change so have added the color column into the function and hav added the cache for the function


@st.cache()
def with_colors(df):
    # Generate colors
    color = ['red', 'blue', 'green', 'pink'] * 25
    # Shuffle the generated list
    random.shuffle(color)
    df['c'] = color
    return df


df = with_colors(df)
# st.write(df)

# Create the radiobuttons for the color
color_radio = st.radio(
    "What's your favorite color?",
    ('blue', 'green', 'pink', 'red', 'All of the above'))

if color_radio == 'All of the above':
    scatter = alt.Chart(df).mark_line(point=True)\
        .encode(x='x', y='y', order='x', color=alt.Color('c:N', scale=alt.Scale(range=['blue', 'green', 'pink', 'red'])), tooltip=['x', 'y', 'c'])\
        .interactive()

elif color_radio == 'blue':
    scatter = alt.Chart(df[df['c'] == color_radio]).mark_line(point=True)\
        .encode(x='x', y='y', color=alt.value(color_radio), tooltip=['x', 'y', 'c'])\
        .interactive()

elif color_radio == 'green':
    scatter = alt.Chart(df[df['c'] == color_radio]).mark_line(point=True)\
        .encode(x='x', y='y', color=alt.value(color_radio), tooltip=['x', 'y', 'c'])\
        .interactive()

elif color_radio == 'pink':
    scatter = alt.Chart(df[df['c'] == color_radio]).mark_line(point=True)\
        .encode(x='x', y='y', color=alt.value(color_radio), tooltip=['x', 'y', 'c'])\
        .interactive()

elif color_radio == 'red':
    scatter = alt.Chart(df[df['c'] == color_radio]).mark_line(point=True)\
        .encode(x='x', y='y', color=alt.value(color_radio), tooltip=['x', 'y', 'c'])\
        .interactive()

# Display the chart
st.altair_chart(scatter, use_container_width=True)

st.markdown(
    "**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
    "Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
    "You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("""
The 2 changes I made were:
- Change the axis font size to 20 pt
- Changed the graph background to Light Gray
"""
            )

source = data.barley()
st.write(source)

# Bar chart between the year and the mean of the yield
bars = alt.Chart(source).mark_bar().encode(
    x='year:O',
    y=alt.Y('mean(yield):Q', title='Mean Yield'),
    color='year:N',
)

error_bars = alt.Chart(source).mark_errorbar(extent='stdev').encode(
    x='year:O',
    y='yield:Q'
)

# Layer chart
final_chart = (bars + error_bars).facet(column='site:N')
# Background color for the final chart
final_chart = final_chart.configure(background='#EEE')
# Font size 
final_chart = final_chart.configure_axis(
    labelFontSize=20,
    titleFontSize=20
)
# Display the final chart
st.altair_chart(final_chart, use_container_width=True)

