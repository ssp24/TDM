import pandas as pd
import plotly.express as px
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

data = pd.read_json("data/hitlist.json")

fig = px.sunburst(data, path=['Parent_no', 'Fachgebiet'], values='Results')

st.plotly_chart(fig, use_container_width=True)
