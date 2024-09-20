import streamlit as st
import plotly.express as px
from dairy_backend import get_scores

st.title("Dairy Tone")

scores, dates = get_scores()

st.subheader("Positivity")
positives = [i["pos"] for i in scores]
figure = px.line(x=dates, y=positives, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")
negatives = [i["neg"] for i in scores]
figure = px.line(x=dates, y=negatives, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure)