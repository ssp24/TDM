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


if st.button('Bestätigen'):
     st.write('Ausgewählt:', auswahl, meta)
 else:
     st.write('Bitte wählen Sie zunächst Katalog und Metadatenformat')



#button = widgets.Button(description="Bestätigen")
#output1 = widgets.Output()

#display(button, output1)

#def on_button_clicked(b):
    
   #with output1:
       # global A
       # value = "https://services.dnb.de/sru/dnb"
       # clear_output()
       # result = auswahl.value
        #if auswahl.value == "DNB":
       #     selected_url = "https://services.dnb.de/sru/dnb"
       # elif auswahl.value == "DMA":
       #     selected_url = "https://services.dnb.de/sru/dnb.dma"
      #  elif auswahl.value == "GND":
       #     selected_url = "https://services.dnb.de/sru/authorities"
       # else:
        #    selected_url = "ERROR: Keine URL gewählt"
      #  print("Auswahl Katalog-URL für", result, ":", selected_url)
       # print("Auswahl Metadatenformat:", meta.value)
    
      #  A = selected_url
       # return A
    
#button.on_click(on_button_clicked)

