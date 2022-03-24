import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

data = pd.read_json("data/hitlist.json")
dnbcolor = ['#40d0c8', '#e4463e', '#124ec9', '#b6c73f', '#feca21',
                           '#3cb8f6', '#fa8e46', '#e3d98f', '#91D4D2', '#F1A39F']

st.header("Darstellung der Sammlungen der DNB")

st.write("Die Datengrundlage für die hier gezeigten Visualisieurungen sind die Titeldaten der DNB.") 
st.write("Stand der Daten: 21.03.2022")

st.subheader("Darstellung Sachgruppen DDC 1")

fig = px.sunburst(data, path=['Parent_no', 'Fachgebiet'], values='Results', height=600)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Darstellung Sachgruppen DDC 2")

fig2 = px.sunburst(data, path=['Parent_title','Fachgebiet'], values='Results',
                  color='Results', hover_data=['DDC'],
                  color_continuous_scale='YlGn',
                  color_discrete_sequence = dnbcolor,
                  #color_continuous_midpoint=np.average(data['Parent_no'], weights=data['Results']),
                  height=800)

fig2.update_traces(insidetextorientation='radial')

st.plotly_chart(fig2, use_container_width=True)


st.subheader("Wordcloud")

ddcdata = data.set_index('DDC').to_dict()['Results']
worddata = data.set_index('Fachgebiet').to_dict()['Results']

wc = WordCloud(background_color="white").generate_from_frequencies(ddcdata)
wc2 = WordCloud(background_color="white", width=800, height=400).generate_from_frequencies(worddata)


fig6, ax = plt.subplots()
ax.imshow(wc2, interpolation="bilinear")
ax.axis("off")

st.pyplot(fig6)
