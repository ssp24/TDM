## Bibliotheken:
import streamlit as st
import requests
from IPython.display import display, clear_output
from bs4 import BeautifulSoup
from lxml import etree
import pandas
import unicodedata
from IPython.core.display import display, HTML


st.header("Test - Informationen zu URNs") 

st.write("Hier können Sie sich Informationen zu einer URN aus dem Namensraum urn:nbn:de anzeigen lassen.") 
         
urn = st.text_input('gesuchte URN')
         
#testurn: urn:nbn:de:hebis:26-opus-37188
         
xml_url = "https://nbn-resolving.org/xml/"    
json_url = "https://nbn-resolving.org/json/"
         
xmlrequest = xml_url + urn
st.write(xmlrequest) 
         
def query(urn): 
    
    response = requests.get(xmlrequest)
         
    return response

 
test = query(urn)
         
st.code(test)
