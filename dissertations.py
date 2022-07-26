import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


#data = pd.read_json("data/diss_06-2022_cleaned.json")
data = pd.read_json("https://www.bygenius.eu/data/diss_06-2022_cleaned.json")
#st.dataframe(data)


dnbcolor = ['#FEFEFE', '#2499ff', '#f33930', '#b6c73f', '#ffd44d',
            '#3cb8f6', '#f9852e', '#e3d98f', '#000000', '#01be00']
testcolor = ['#ff6900', '#fcb900', '#7bdcb5', '#00d084', '#8ed1fc',
            '#0693e3', '#abb8c3', '#eb144c', '#f78da7', '#9900ef']


st.header('Übersicht "Freie Online-Hochschulschriften" in der DNB')

st.write("Informationen zu Datengrundlage: Die die erstellten Visualisieurungen basieren auf den Titeldaten der DNB. Hierfür wurde das Datenset "
         '"Freie Online-Hochschulschriften" der DNB genutzt, welches die Metadaten von mehr als 282.000 Online-Dissertationen '
         "ohne Zugriffsbeschränkung aus Deutschland enthält. ") 

st.write("Stand der Daten: 23.06.2022")

st.subheader("Anzahl der Online-Hochschulschriften im Bestand nach Jahren: ")

#Jahre: 
data1 = data[data['Year'].notna()]
data1 = data1.astype({'Year':'int'})
data1 = data1[(data1['Year'] >= 1900) & (data1['Year'] <= 2100)]

s = data1['Year'].value_counts()[:33].sort_index()
fig = px.bar(s, x="Jahr", labels={'index':'Jahr', 'value':'Anzahl'}, color='value', height=500)
st.plotly_chart(fig, use_container_width=True)

st.info("INFO: Es werden die Daten für die Jahre 1990 bis 2022 (laufend) dargestellt. " ) 


st.subheader("Hochschulschriften nach Sachgruppen:")

st.info("INFO: Klicken Sie auf die einzelnen Elemente, um eine detailliertere Darstellung der Teilmengen sehen zu können. "
        "Bewegen Sie Ihren Cursor auf die Elemente, um Zusatzinformationen zu erhalten." ) 

#Erster Darstellung: 
fig = px.sunburst(data, path=['DDC', 'DDC2'], values='found', 
                  custom_data=['DDC', 'found', 'Parent_no'],
                  height=1000, color_discrete_sequence = testcolor)
fig.update_traces(insidetextorientation='radial', texttemplate="%{label}<br>%{percentEntry:.2%}",
                 hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Hauptklasse: %{customdata[2]} - %{customdata[0]}"]),
                        sort=False,
                        rotation=180,
                        textfont_size=12
                 )

st.plotly_chart(fig, use_container_width=True)


