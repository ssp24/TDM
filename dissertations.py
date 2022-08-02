import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


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
st.write("Klicken Sie auf die Anzahl der Dissertationen eines bestimmten Jahres, um diese im Katalog der DNB zu betrachten.")


dissyears2 = pd.read_json("data/dissyears.json")
dissyears2["url"] = "https://portal.dnb.de/opac.htm?method=simpleSearch&cqlMode=true&query=catalog=dnb.hss+location=onlinefree+jhr="+dissyears2["years"].astype(str)

fig2 = px.bar(dissyears2, x="years", y = "count", labels={'years':'Jahr', 'count':'Anzahl'}, color='count', height=500)
update = (len(dissyears2["years"]))

for i in range (0,update):     
    fig2.add_annotation(      
                x = dissyears2["years"].values[i],
                y = dissyears2["count"].values[i],
                textangle = 90,
                text = f"""<a href="{dissyears2["url"].values[i]}" target="_blank">{dissyears2["count"].values[i]}</a>""",
                showarrow=True,
                arrowhead=1,                        
            )
fig2.update_traces(showlegend=False)
st.plotly_chart(fig2, use_container_width=True)

st.info("INFO: Es werden die Daten für die Jahre 1990 bis 2022 (laufend) dargestellt. " ) 
