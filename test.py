import streamlit as st

searchterm = st.text_input('Suchbegriff:', placeholder="Bitte Suchbegriff eingeben")

st.write(searchterm)

if not searchterm: 
  st.write("Kein Searchterm")
else: 
  st.write("SUCCESS")

