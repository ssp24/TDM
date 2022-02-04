import streamlit as st

searchterm = st.text_input('Suchbegriff:', placeholder="Bitte Suchbegriff eingeben", default_value="test")

st.write(searchterm)
