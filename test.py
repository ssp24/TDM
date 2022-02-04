import streamlit as st

searchterm = st.text_input('Suchbegriff:', placeholder="Bitte Suchbegriff eingeben")

st.write(searchterm)
