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

st.write("Hier können Sie sich Informationen zu einer URN aus dem Namensraum urn:nbn:de anzeigen lassen". 
         
urn = st.text_input('gesuchte URN')
         
#testurn: urn:nbn:de:hebis:26-opus-37188
         
def request(): 
         
    xml_url = "https://nbn-resolving.org/xml/"    
    json_url = "https://nbn-resolving.org/json/"
         
    xmlrequest = xml_url + urn
    st.write(xmlrequest) 
         
    
 
 content = request(urn)
         
 st.code(content)
