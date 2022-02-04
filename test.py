import streamlit as st

searchterm = st.text_input('Suchbegriff:', placeholder="Bitte Suchbegriff eingeben")

st.write(searchterm)

if searchterm == None: 
  st.write("Kein Searchterm")
else: 
  st.write("SUCCESS")

if not searchterm: 
  st.write("Existiert, ist aber leer")
else:
  st.write("Auch nicht der Weg")
