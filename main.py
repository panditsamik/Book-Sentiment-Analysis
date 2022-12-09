import glob
import plotly.express as px
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
positivity_scores = []
negativity_scores = []

filepaths = glob.glob("diary/*.txt")
for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity_scores.append(scores["pos"])
    negativity_scores.append(scores["neg"])

dates = [item.strip(".txt").strip("diary/") for item in filepaths]

st.title("Diary Tone")
st.subheader("Positivity")
figure1 = px.line(x=dates,
                  y=positivity_scores,
                  labels={"x": "Dates",
                          "y": "Positivity"})
st.plotly_chart(figure1)

st.subheader("Negativity")
figure2 = px.line(x=dates,
                  y=negativity_scores,
                  labels={"x": "Dates",
                          "y": "Negativity"})
st.plotly_chart(figure2)
