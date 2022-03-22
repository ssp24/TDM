import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

data = pd.read_json("data/hitlist.json")

fig = px.sunburst(data, path=['Parent_no', 'Fachgebiet'], values='Results')

st.plotly_chart(fig, use_container_width=True)

st.subheading("Darstellung Sachgruppen DDC")

fig2 = px.sunburst(data, path=['Parent_title','Fachgebiet'], values='Results',
                  color='Results', hover_data=['DDC'],
                  color_continuous_scale='YlGn',
                  #color_continuous_midpoint=np.average(data['Parent_no'], weights=data['Results']),
                  height=800)

fig2.update_traces(insidetextorientation='radial')

st.plotly_chart(fig2, use_container_width=True)
