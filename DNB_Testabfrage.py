## DNB_Testabfrage für streamlit:

## Bibliotheken:
import streamlit as st
import requests
from IPython.display import display, clear_output
from bs4 import BeautifulSoup
from lxml import etree
import pandas
import unicodedata

st.title("Testabfrage DNB-Daten")

st.markdown("Hier können Sie die SRU-Schnittstelle der Deutschen Nationalbibliothek über einfache Formulareingaben "
        "abfragen. Wählen Sie dazu den Katalog, den Sie abfragen möchten und das Metadatenformat für die Ausgabe "
        "aus. Im nächsten Schritt geben Sie Ihren Suchbegriff ein. Für die Ausführung des dahinterliegenden Codes "
        "muss die Reihenfolge bei Eingaben und Buttonklicks eingehalten werden. Im Anschluss können Sie sich eine "
        "gekürzte tabellarische Darstellung Ihrer Anfrage ansehen und diese als XML- oder CSV-Datei speichern. ")
        
st.markdown("**Bitte beachten Sie**: Dieses Tutorial dient als Einstieg. Aus Performance-Gründen werden jeweils "
            "immer nur die **ersten 100 Treffer** Ihrer Anfrage ausgegeben. Die Metadatenformate enthalten "
            "unterschiedliche Informationen. Die Ausgabetabellen und -dateien variieren daher entsprechend in der "
            "Anzahl enthaltener Elemente und Informationen.")


st.subheader("Bitte wählen Sie zunächst den gewünschten Katalog:")
st.text(" DNB = Titeldaten der Deutschen Nationalbibliothek \n "
"DMA = Deutsches Musikarchiv \n "
        "GND = Gemeinsame Normdatei ")

##Erstes Dropdown:
auswahl = st.selectbox(
            'Katalog:', 
            ('DNB', 'DMA', 'GND'))
            
display(auswahl)
default = "https://services.dnb.de/sru/dnb"

#Zweites Dropdown:
st.subheader("Bitte wählen Sie das Metadatenformat für die Ausgabe:")

meta = st.selectbox(
        'Metadatenformat:',
        ('MARC21-xml', 'DNB Casual (oai_dc)', 'RDF (RDFxml)'))

display(meta)


#Übernahme der Parameter bei Click auf Bestätigen: 
if st.button('Bestätigen'):
     st.write('Katalog:', auswahl, ':', selected_url)
     st.write('Metadatenformat:', meta)
     if auswahl == "DNB":
        selected_url = "https://services.dnb.de/sru/dnb"
     elif auswahl == "DMA":
        selected_url = "https://services.dnb.de/sru/dnb.dma"
     elif auswahl == "GND":
        selected_url = "https://services.dnb.de/sru/authorities"
     else:
        selected_url = "ERROR: Keine URL gewählt"  
else:
     st.write('Bitte wählen Sie Katalog und Metadatenformat')



