## DNB_Testabfrage für streamlit:

## Bibliotheken:
import streamlit as st
import requests
from IPython.display import display, clear_output
from bs4 import BeautifulSoup
from lxml import etree
import pandas
import unicodedata

if "button1_clicked" not in st.session_state:
    st.session_state.button1_clicked = False
    st.session_state.button2_clicked = False

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

confirm = st.button('Los!', key='push')
#Suche ausführen: 
if confirm:
     parameter = {'version' : '1.1' , 'operation' : 'searchRetrieve' , 'query' : searchterm, 'recordSchema' : meta, 
                  'maximumRecords': '100'} 

     r1 = requests.get(selected_url, params = parameter)  

     response = BeautifulSoup(r1.content)
     records = response.find_all('record')
     records_marc = response.find_all('record', {'type':'Bibliographic'})
     gndm = response.find_all('record', {'type':'Authority'})
     results = response.find('numberofrecords')  
     numberofrecords = results.text
     numberofrecords = int(numberofrecords)
     st.write("Gefundene Treffer:", numberofrecords)
        
     if numberofrecords >= 1: 
        vorschau = records[0]
        st.write("Vorschau des ersten Treffers der SRU-Antwort:")
        st.code(vorschau)
     else: 
        st.write("Keine Treffer vorhanden")
else:
     st.write('Bitte wählen Sie Katalog und Metadatenformat und geben Sie einen Suchbegriff ein')



## TEIL 2 -------------------------------------------------------------------------------------------


#Funktion für Titeldaten in OAI-DC
def parse_record_dc(record):
    
    ns = {"dc": "http://purl.org/dc/elements/1.1/", 
          "xsi": "http://www.w3.org/2001/XMLSchema-instance"}
    xml = etree.fromstring(unicodedata.normalize("NFC", str(record)))
    
    #idn
    idn = xml.xpath(".//dc:identifier[@xsi:type='dnb:IDN']", namespaces=ns) #--> Adressiert das Element direkt   
    try:
        idn = idn[0].text
    except:
        idn = 'fail'
    
    #creator:
    creator = xml.xpath('.//dc:creator', namespaces=ns)
    try:
        creator = creator[0].text
    except:
        creator = "N/A"
    
    #titel
    titel = xml.xpath('.//dc:title', namespaces=ns)
    try:
        titel = titel[0].text
    except:
        titel = "N/A"
        
    #date
    date = xml.xpath('.//dc:date', namespaces=ns)
    try:
        date = date[0].text
    except:
        date = "N/A"
    
    #publisher
    publ = xml.xpath('.//dc:publisher', namespaces=ns)
    try:
        publ = publ[0].text
    except:
        publ = "N/A"
     
    #identifier
    ids = xml.xpath('.//dc:identifier[@xsi:type="tel:ISBN"]', namespaces=ns)
    try:
        ids = ids[0].text
    except:
        ids = "N/A"
        
    #urn
    urn = xml.xpath('.//dc:identifier[@xsi:type="tel:URN"]', namespaces=ns)
    try:
        urn = urn[0].text
    except:
        urn = "N/A"
         
    meta_dict = {"IDN":idn, "CREATOR":creator, "TITLE":titel, "DATE":date, "PUBLISHER":publ, "URN":urn, "ISBN":ids}
    return meta_dict
  
    
                 
#Function für Titeldaten in MARC21
def parse_record_marc(item):

    ns = {"marc":"http://www.loc.gov/MARC21/slim"}
    xml = etree.fromstring(unicodedata.normalize("NFC", str(item)))
    
    #idn
    idn = xml.findall("marc:controlfield[@tag = '001']", namespaces=ns)
    try:
        idn = idn[0].text
    except:
        idn = 'N/A' 
        
    #creator
    creator1 = xml.findall("marc:datafield[@tag = '100']/marc:subfield[@code = 'a']", namespaces=ns)
    creator2 = xml.findall("marc:datafield[@tag = '110']/marc:subfield[@code = 'a']", namespaces=ns)
    subfield = xml.findall("marc:datafield[@tag = '110']/marc:subfield[@code = 'e']", namespaces=ns)
    
    if creator1:
        creator = creator1[0].text
    elif creator2:
        creator = creator2[0].text
        if subfield:
            creator = creator + " [" + subfield[0].text + "]"
    else:
        creator = "N/A"
    
    #Titel $a
    title = xml.findall("marc:datafield[@tag = '245']/marc:subfield[@code = 'a']", namespaces=ns)
    title2 = xml.findall("marc:datafield[@tag = '245']/marc:subfield[@code = 'b']", namespaces=ns)
    
    if title and not title2:
        titletext = title[0].text
    elif title and title2:     
        titletext = title[0].text + ": " + title2[0].text
    else:
        titletext = "N/A"
    
    #date
    date = xml.findall("marc:datafield[@tag = '264']/marc:subfield[@code = 'c']", namespaces=ns)
    try:
        date = date[0].text
    except:    
        date = 'N/A'
    
    #publisher
    publ = xml.findall("marc:datafield[@tag = '264']/marc:subfield[@code = 'b']", namespaces=ns)
    try:
        publ = publ[0].text
    except:    
        publ = 'N/A'
        
    #URN
    testurn = xml.findall("marc:datafield[@tag = '856']/marc:subfield[@code = 'x']", namespaces=ns)
    urn = xml.findall("marc:datafield[@tag = '856']/marc:subfield[@code = 'u']", namespaces=ns)
    
    if testurn:
        urn = urn[0].text
    else:    
        urn = 'N/A'
          
    #ISBN
    isbn_new = xml.findall("marc:datafield[@tag = '020']/marc:subfield[@code = 'a']", namespaces=ns)
    isbn_old = xml.findall("marc:datafield[@tag = '024']/marc:subfield[@code = 'a']", namespaces=ns)
    if isbn_new:
        isbn = isbn_new[0].text
    elif isbn_old: 
        isbn = isbn_old[0].text
    else:    
        isbn = 'N/A'
      
    meta_dict = {"IDN":idn, "CREATOR":creator, "TITLE": titletext, "DATE":date, 
                 "PUBLISHER":publ, "URN":urn, "ISBN":isbn}
    return meta_dict

                 
                 
             
#Funktion für Titeldaten in RDF:

def parse_record_rdf(record):
    
    ns = {"xlmns":"http://www.loc.gov/zing/srw/", 
          "agrelon":"https://d-nb.info/standards/elementset/agrelon#",
          "bflc":"http://id.loc.gov/ontologies/bflc/",
          "rdau":"http://rdaregistry.info/Elements/u/",
          "dc":"http://purl.org/dc/elements/1.1/",
          "rdau":"http://rdaregistry.info/Elements/u",
          "bibo":"http://purl.org/ontology/bibo/",
          "dbp":"http://dbpedia.org/property/",  
          "dcmitype":"http://purl.org/dc/dcmitype/", 
          "dcterms":"http://purl.org/dc/terms/", 
          "dnb_intern":"http://dnb.de/", 
          "dnbt":"https://d-nb.info/standards/elementset/dnb#", 
          "ebu":"http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#", 
          "editeur":"https://ns.editeur.org/thema/", 
          "foaf":"http://xmlns.com/foaf/0.1/", 
          "gbv":"http://purl.org/ontology/gbv/", 
          "geo":"http://www.opengis.net/ont/geosparql#", 
          "gndo":"https://d-nb.info/standards/elementset/gnd#", 
          "isbd":"http://iflastandards.info/ns/isbd/elements/", 
          "lib":"http://purl.org/library/", 
          "madsrdf":"http://www.loc.gov/mads/rdf/v1#", 
          "marcrole":"http://id.loc.gov/vocabulary/relators/",
          "mo":"http://purl.org/ontology/mo/", 
          "owl":"http://www.w3.org/2002/07/owl#", 
          "rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#", 
          "rdfs":"http://www.w3.org/2000/01/rdf-schema#", 
          "schema":"http://schema.org/", 
          "sf":"http://www.opengis.net/ont/sf#", 
          "skos":"http://www.w3.org/2004/02/skos/core#", 
          "umbel":"http://umbel.org/umbel#", 
          "v":"http://www.w3.org/2006/vcard/ns#", 
          "vivo":"http://vivoweb.org/ontology/core#", 
          "wdrs":"http://www.w3.org/2007/05/powder-s#", 
          "xsd":"http://www.w3.org/2001/XMLSchema#"}
    
    xml = etree.fromstring(unicodedata.normalize("NFC", str(record)))
   
    #idn
    idn = xml.findall(".//dc:identifier", namespaces=ns)
    try:
        idn = idn[0].text
    except:
        idn = 'N/A' 
        
    #creator
    creator = record.find_all('rdau:p60327')
    
    try:
        creator = creator[0].text
    except:
        creator = "N/A"
        
    #title
    test = record.find_all('dc:title')
    
    try:
        test = test[0].text
    except:
        test = "N/A"
        
    #date
    date = record.find_all('dcterms:issued')
    try:
        date = date[0].text
    except:
        date = "N/A"    
      
    #publisher
    publ = record.find_all('dc:publisher')
    try:
        publ = publ[0].text
    except:
        publ = "N/A"    
    
    #urn
    urn = record.find_all('umbel:islike')
    try:
        urn = urn[0]
        urn = urn.get('rdf:resource')
    except:
        urn = "N/A"
    
    #isbn
    isbn = xml.findall(".//bibo:isbn13", namespaces=ns)
    isbn10 = xml.findall(".//bibo:isbn10", namespaces=ns)
    
    if isbn:
        isbn = isbn[0].text
    elif isbn10: 
        isbn = isbn10[0].text
    else:
        isbn = "N/A"
     
    meta_dict = {"IDN":idn, "CREATOR":creator, "TITLE":test, "DATE":date, "PUBLISHER":publ, "URN":urn, "ISBN":isbn}
    return meta_dict
                 
                 
                 
                 
                 
## -----------------------------------------------------------------------------
                 
                 
                 
#Ausgaben: 
                 
st.subheader("Ausgeben und Speichern der Daten:")
                 
st.subheader("Darstellung der Daten in tabellarischer Form:")


##für Titeldaten:
if confirm:

    if auswahl == "DNB" and meta == "oai_dc":
        result = [parse_record_dc(record) for record in records]
        df = pandas.DataFrame(result)
                #df1 = (df.style
                             #.format({'URN': make_clickable})
                             #.set_properties(**{'text-align': 'left'})
                             #.set_table_styles([dict(selector = 'th', props=[('text-align', 'left')])]) )    
        st.dataframe(df)
    elif auswahl == "DNB" and meta == "MARC21-xml":
        result2 = [parse_record_marc(item) for item in records_marc]
        df = pandas.DataFrame(result2)
                #df1 = (df.style
                             #.format({'URN': make_clickable})
                            # .set_properties(**{'text-align': 'left'})
                             #.set_table_styles([dict(selector = 'th', props=[('text-align', 'left')])]) )       
        st.dataframe(df)
    elif auswahl == "DNB" and meta == "RDFxml":
        result3 = [parse_record_rdf(item) for item in records]
        df = pandas.DataFrame(result3)
                #df1 = (df.style
                            # .format({'URN': make_clickable})
                            # .set_properties(**{'text-align': 'left'})
                            # .set_table_styles([dict(selector = 'th', props=[('text-align', 'left')])]) )       
        st.dataframe(df)
else:
    st.write("Es wurde noch keine Suchanfrage gestellt.")
        

        
