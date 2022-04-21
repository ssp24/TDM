import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import h5py

test = h5py.File("data/testdf.h5")

#data = pd.read_hdf("data/online_diss_cleaned.h5")
test2 = h5py.File("data/online_diss_cleaned.h5")
data = pd.DataFrame(test2, key="df")
#data['Results'] = data['Results'].astype(int)
st.dataframe(data)


dnbcolor = ['#FEFEFE', '#2499ff', '#f33930', '#b6c73f', '#ffd44d',
            '#3cb8f6', '#f9852e', '#e3d98f', '#000000', '#01be00']
testcolor = ['#ff6900', '#fcb900', '#7bdcb5', '#00d084', '#8ed1fc',
            '#0693e3', '#abb8c3', '#eb144c', '#f78da7', '#9900ef']


st.header('Übersicht "Freie Online-Hochschulschriften" in der DNB')

st.write("Informationen zu Datengrundlage: Die die erstellten Visualisieurungen basieren auf den Titeldaten der DNB. Hierfür wurde das Datenset "
         '"Freie Online-Hochschulschriften" der DNB genutzt, welches die Metadaten von mehr als 282.000 Online-Dissertationen '
         "ohne Zugriffsbeschränkung aus Deutschland enthält. ") 

st.write("Stand der Daten: 22.03.2022")

st.subheader("Anzahl der Online-Hochschulschriften im Bestand nach Jahren: ")

st.info("INFO: Es werden die Daten für die Jahre 1990 bis 2022 (laufend) dargestellt." ) 

#Jahre: 
#data = data[data['Year'].notna()]
#data = data.astype({'Year':'int'})
#data = data[(data['Year'] >= 1900) & (data['Year'] <= 2100)]

#s = data['Year'].value_counts()[:33].sort_index()
#fig = px.bar(s, labels={'index':'Jahr', 'value':'Anzahl'}, color='value', height=500)
#st.plotly_chart(fig, use_container_width=True)


