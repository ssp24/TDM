import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#data = pd.read_json("data/DDCall.json")
#data = pd.read_excel("data/DDCall.xlsx")
dnbcolor = ['#40d0c8', '#124ec9', '#e4463e', '#b6c73f', '#feca21',
            '#3cb8f6', '#f9852e', '#e3d98f', '#8102ff', '#01be00']

alldata = data['found'].sum(axis=0) 
allofit = alldata.to_string()


st.header("Darstellung der Sammlungen der DNB")

st.write("Informationen zu Datengrundlage: Die die erstellten Visualisieurungen basieren auf den Titeldaten der DNB. Hierfür wurde für jede DDC-Sachgruppe "
         "eine Suchanfrage über die SRU-Schnittstelle gestellt und die erhaltene Treffermenge übernommen.") 
st.write("Abgebildete Titeldaten:", allofit) 
st.write("Stand der Daten: 21.03.2022")

st.subheader("Unsere Sammlungen:")

fig = px.sunburst(data, path=['Parent_title', 'DDCsecond-title', 'Sachgebiet'], values='found', height=800, color_discrete_sequence = dnbcolor)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Darstellung Sachgruppen DDC 2")

fig2 = px.sunburst(data, path=['Parent_title','Fachgebiet'], values='Results',
                  color='Results', hover_data=['DDC'],
                  color_continuous_scale='YlGn',
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
