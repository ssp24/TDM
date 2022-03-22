import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

data = pd.read_json("data/hitlist.json")

fig = px.sunburst(data, path=['Parent_no', 'Fachgebiet'], values='Results', height=600)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Darstellung Sachgruppen DDC")

fig2 = px.sunburst(data, path=['Parent_title','Fachgebiet'], values='Results',
                  color='Results', hover_data=['DDC'],
                  color_continuous_scale='YlGn',
                  #color_continuous_midpoint=np.average(data['Parent_no'], weights=data['Results']),
                  height=800)

fig2.update_traces(insidetextorientation='radial')

st.plotly_chart(fig2, use_container_width=True)


st.header("Wordcloud")

ddcdata = data.set_index('DDC').to_dict()['Results']
worddata = data.set_index('Fachgebiet').to_dict()['Results']

wc = WordCloud(background_color="white").generate_from_frequencies(ddcdata)
wc2 = WordCloud(background_color="white", width=800, height=400).generate_from_frequencies(worddata)

plt.figure(figsize=(10, 10))
plt.imshow(wc2, interpolation="bilinear")
plt.axis("off")

st.pyplot(wc2)
