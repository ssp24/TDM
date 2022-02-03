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
if auswahl == "DNB":
        selected_url = "https://services.dnb.de/sru/dnb"
elif auswahl == "DMA":
        selected_url = "https://services.dnb.de/sru/dnb.dma"
elif auswahl == "GND":
        selected_url = "https://services.dnb.de/sru/authorities"
else:
        selected_url = "ERROR: Keine URL gewählt"  
st.write('Katalog:', auswahl, ':', selected_url)
st.write('Metadatenformat:', meta)


#Eingabe Suchbegriff: 
st.subheader("Bitte geben Sie nun Ihren Suchbegriff ein:")
searchterm = st.text_input('Suchbegriff:', 'Faust')

#Suche ausführen: 
if st.button('Los!', key='push2'):
     parameter = {'version' : '1.1' , 'operation' : 'searchRetrieve' , 'query' : searchterm, 'recordSchema' : meta, 
                  'maximumRecords': '100'} 

     r1 = requests.get(selected_url, params = parameter)  

     response = BeautifulSoup(r1.content)
     records = response.find_all('record')
     records_marc = response.find_all('record', {'type':'Bibliographic'})
     gndm = response.find_all('record', {'type':'Authority'})
     numberofrecords = response.find_all('numberofrecords')
     st.write(numberofrecords[0])

else:
     st.write('Bitte wählen Sie Katalog und Metadatenformat und geben Sie einen Suchbegriff ein')


#test = numberofrecords[0].text
#test2 = test.text
#st.write(test)
#st.write(test2)
     #vorschau = records[0]
     #st.write("Gefundene Treffer:", numberofrecords)
     #st.write(" ")
     #st.write("Vorschau des ersten Treffers der SRU-Antwort:")
     #st.write(vorschau.prettify())
     #st.write("")
     #st.write(" - Ende der Vorschau - ")  

