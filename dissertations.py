import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

logo = "https://files.dnb.de/DFG-Viewer/DNB-Logo-Viewer.jpg"
#st.image(logo)
st.set_page_config(page_title='DNB - DissVIS', page_icon = logo) # , layout = 'wide')

stats = pd.read_json("data/stats.json")
dissyears2 = pd.read_json("data/dissyears.json")


# ---- SIDEBAR ----- 

with st.sidebar:
    st.subheader("Auswahlmenü")
    visual = st.selectbox(
     'Bitte wählen Sie die Anzeige: ',
     ('Übersicht', 'Publikationsjahre', 'Verteilung nach Fächern', 'Sprachen', 'Publikationsorte')
    )
    st.write('Momentan ausgewählt:',
             visual)
    
    st.write("Stand der Daten: 23.06.2022")
    

# ----- color codes ---------

dnbcolor = ['#FEFEFE', '#2499ff', '#f33930', '#b6c73f', '#ffd44d',
            '#3cb8f6', '#f9852e', '#e3d98f', '#000000', '#01be00']
testcolor = ['#ff6900', '#fcb900', '#7bdcb5', '#00d084', '#8ed1fc',
            '#0693e3', '#abb8c3', '#eb144c', '#f78da7', '#9900ef']

st.header('"Freie Online-Hochschulschriften" in der DNB')


# ------- MAIN BOX ----------

if visual == "Übersicht":

    st.write("Informationen zur Datengrundlage: "
         " Die die erstellten Visualisieurungen basieren auf den Titeldaten der DNB. Hierfür wurde das Datenset "
         ' "Freie Online-Hochschulschriften" der DNB genutzt, welches die Metadaten von mehr als 282.000 freien Online-Dissertationen '
         " ohne Zugriffsbeschränkung aus Deutschland enthält. ")
    st.write(" Das Datenset wird alle 3 Monate aktualisiert."  ) 
    st.write("")


    all_ofd = 288128
    conv_ofd = f'{all_ofd:,}'
    #test2 = float(test.replace(',', '.'))
    conv1_ofd = conv_ofd.replace(',', '.')
    ofd_last = 282864
    growth = all_ofd-ofd_last
    conv_growth = f'{growth:,}'
    conv1_growth = conv_growth.replace(',', '.')
    update = conv1_growth + ' (seit März 2022)'
       
  
    st.metric(label="Anzahl freie online Dissertationen", value=conv1_ofd, delta=update)
    #st.caption("Seit der letzten Aktualisierung des Datensets im März 2022.")
  
     # --- Data ---- 
    
    df = pd.read_json("data/diss_06-2022_cleaned.json")
    dissddc = pd.read_json("data/diss_ddc.json")
    
    zero = dissddc[dissddc["Parent_no"].astype(str).str.startswith('0')]
    first = dissddc[dissddc["Parent_no"].astype(str).str.startswith('1')]
    second = dissddc[dissddc["Parent_no"].astype(str).str.startswith('2')]
    third = dissddc[dissddc["Parent_no"].astype(str).str.startswith('3')]
    fourth = dissddc[dissddc["Parent_no"].astype(str).str.startswith('4')]
    fifth = dissddc[dissddc["Parent_no"].astype(str).str.startswith('5')]
    sixth = dissddc[dissddc["Parent_no"].astype(str).str.startswith('6')]
    seventh = dissddc[dissddc["Parent_no"].astype(str).str.startswith('7')]
    eigth = dissddc[dissddc["Parent_no"].astype(str).str.startswith('8')]
    ninth = dissddc[dissddc["Parent_no"].astype(str).str.startswith('9')]
    
    
    pub_000 = zero['count'].sum()
    conv_pub_000 = f'{pub_000:,}'
    conv1_pub_000 = conv_pub_000.replace(',', '.')
    pub_100 = first['count'].sum()
    conv_pub_100 = f'{pub_100:,}'
    conv1_pub_100 = conv_pub_100.replace(',', '.')
    pub_200 = second['count'].sum()
    conv_pub_200 = f'{pub_200:,}'
    conv1_pub_200 = conv_pub_200.replace(',', '.')
    pub_300 = third['count'].sum()
    conv_pub_300 = f'{pub_300:,}'
    conv1_pub_300 = conv_pub_300.replace(',', '.')
    pub_400 = fourth['count'].sum()
    conv_pub_400 = f'{pub_400:,}'
    conv1_pub_400 = conv_pub_400.replace(',', '.')
    pub_500 = fifth['count'].sum()
    conv_pub_500 = f'{pub_500:,}'
    conv1_pub_500 = conv_pub_500.replace(',', '.')
    pub_600 = sixth['count'].sum()
    conv_pub_600 = f'{pub_600:,}'
    conv1_pub_600 = conv_pub_600.replace(',', '.')
    pub_700 = seventh['count'].sum()
    conv_pub_700 = f'{pub_700:,}'
    conv1_pub_700 = conv_pub_700.replace(',', '.')
    pub_800 = eigth['count'].sum()
    conv_pub_800 = f'{pub_800:,}'
    conv1_pub_800 = conv_pub_800.replace(',', '.')
    pub_900 = ninth['count'].sum()
    conv_pub_900 = f'{pub_900:,}'
    conv1_pub_900 = conv_pub_900.replace(',', '.')
    
    # --- boxes
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        wch_colour_box = (0,504,102)
        wch_colour_font = (0,0,0)
        fontsize = 18
        #valign = "left"
        iconname = "fas fa-asterisk"
        sline = "Informatik, Information & Wissen, allgemeine Werke"
        #lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = conv1_pub_000
        
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height: 20px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><br><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(htmlstr, unsafe_allow_html=True)
    
    
    with col2: 
        wch_colour_box = (200,504,102)
        wch_colour_font = (0,0,0)
        fontsize = 18
        iconname = "fas fa-asterisk"
        sline = "Philosophie & Psychologie"
        i = conv1_pub_100

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, {wch_colour_box[1]}, {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, {wch_colour_font[1]}, {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(htmlstr, unsafe_allow_html=True)
        
    with col3:
        wch_colour_box = (000,204,602)
        #wch_colour_font = (0,0,0)
        fontsize = 18
        #iconname = "fas fa-asterisk"
        sline = "Religion"
        i = conv1_pub_200

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, {wch_colour_box[1]}, {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, {wch_colour_font[1]}, {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(htmlstr, unsafe_allow_html=True)

   
    twocol1, twocol2, twocol3 = st.columns(3)
      
    with twocol1: 
        wch_colour_box = (100,204,302)
        fontsize = 18
        sline = "Sozialwissenschaften"
        i = conv1_pub_300
        
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, {wch_colour_box[1]}, {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, {wch_colour_font[1]}, {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
    with twocol2: 
        wch_colour_box = (800,204,102)
        fontsize = 18
        sline = "Sprache"
        i = conv1_pub_400
        
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, {wch_colour_box[1]}, {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, {wch_colour_font[1]}, {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
        
    with twocol3: 
        wch_colour_box = (400,204,402)
        fontsize = 18
        sline = "Naturwissenschaften"
        i = conv1_pub_500
        
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, {wch_colour_box[1]}, {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, {wch_colour_font[1]}, {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
        
    threecol1, threecol2, threecol3 = st.columns(3)
      
    with threecol1: 
        wch_colour_box = (255,200,31)
        fontsize = 18
        sline = "Technik"
        i = conv1_pub_600
        
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, {wch_colour_box[1]}, {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, {wch_colour_font[1]}, {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
        
    with threecol2: 
        wch_colour_box = (230,45,45)
        fontsize = 18
        sline = "Künste & Freizeit und Erholung"
        i = conv1_pub_700
        
        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+diss*+location%3Donlinefree+hsg%3D7*&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({wch_colour_box[0]}, {wch_colour_box[1]}, {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, {wch_colour_font[1]}, {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p></a>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
    with threecol3: 
        wch_colour_box = (0,70,196)
        fontsize = 18
        sline = "Literatur"
        i = conv1_pub_800
        
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, {wch_colour_box[1]}, {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, {wch_colour_font[1]}, {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
    fourcol1, fourcol2, fourcol3 = st.columns(3)
      
    with fourcol1: 
        wch_colour_box = (77,170,1)
        fontsize = 18
        sline = "Geschichte & Geografie"
        i = conv1_pub_900
        
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, {wch_colour_box[1]}, {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, {wch_colour_font[1]}, {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
        
        

#------ PUBLIKATIONSJAHRE --------------

elif visual == "Publikationsjahre":  

    st.subheader("Anzahl der Online-Hochschulschriften im Bestand nach Jahren: ")

    dissyears2["url"] = "https://portal.dnb.de/opac.htm?method=simpleSearch&cqlMode=true&query=catalog=dnb.hss+location=onlinefree+jhr="+dissyears2["years"].astype(str)

    fig2 = px.bar(dissyears2, x="years", y = "count", labels={'years':'Jahr', 'count':'Anzahl'}, color='count', height=500)
    update = (len(dissyears2["years"]))

    for i in range (0,update):     
        fig2.add_annotation(      
                x = dissyears2["years"].values[i],
                y = dissyears2["count"].values[i],
                textangle = 90,
                text = f"""<a href="{dissyears2["url"].values[i]}" target="_blank">{dissyears2["count"].values[i]}</a>""",
                showarrow=True,
                arrowhead=1,                        
            )
    fig2.update_traces(showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

    st.write("Klicken Sie auf die Anzahl der Dissertationen eines bestimmten Jahres, um diese im Katalog der DNB zu betrachten.")
    st.info("INFO: Es werden die Daten für die Jahre 1990 bis 2022 (laufend) dargestellt. " )     
 

# --------- DDC -----------------

elif visual == "Verteilung nach Fächern":
    
    dissddc = pd.read_json("data/diss_ddc.json")
    
    #Erste Darstellung: 
    fig = px.sunburst(dissddc, path=['Parent_title', 'DDCsecond-title', 'Sachgebiet'], values='count', 
                  custom_data=['Parent_title', 'count', 'Parent_no'],
                  height = 750, color_discrete_sequence = testcolor)
    fig.update_traces(insidetextorientation='radial', texttemplate="%{label}<br>%{percentEntry:.2%}",
                 hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Hauptklasse: %{customdata[2]} - %{customdata[0]}"]),
                        sort=False,
                        rotation=180,
                        textfont_size=12
                 )

    st.plotly_chart(fig, use_container_width=True)
    
    st.info("INFO: Klicken Sie auf die einzelnen Elemente, um eine detailliertere Darstellung der Teilmengen sehen zu können. "
        "Bewegen Sie Ihren Cursor auf die Elemente, um Zusatzinformationen zu erhalten." ) 
       
    col1, col2 = st.columns([1, 6])
    
     
    
    with col1:
        st.write("")
        st.write("")
        st.markdown("[![Foo](https://i.creativecommons.org/l/by-nc-nd/3.0/88x31.png)](http://creativecommons.org/licenses/by-nc-nd/3.0/)") 
        
        
    with col2:     
        st.caption("This work is licensed under a Creative Commons Attribution-Noncommercial-No Derivative Works 3.0 Unported License "
            "by OCLC Online Computer Library Center, Inc. All copyright rights in the Dewey Decimal Classification system are "
            "owned by OCLC. Dewey, Dewey Decimal Classification, DDC, OCLC and WebDewey are registered trademarks of OCLC. ")
    

elif visual == "Sprachen":
    
    #stats = pd.read_json("data/stats.json") 
    stats.drop(stats.loc[stats['DDC']== "N/A"].index, inplace=True)
    stats.drop(stats.loc[stats['DDC']=="NaN"].index, inplace=True)
    
    lang_ger = stats.lang.value_counts()["ger"]
    lang_eng = stats.lang.value_counts()["eng"]
    lang_fre = stats.lang.value_counts()["fre"]
    lang_ita = stats.lang.value_counts()["ita"]
    lang_spa = stats.lang.value_counts()["spa"]
    lang_por = stats.lang.value_counts()["por"]
    lang_dut = stats.lang.value_counts()["dut"]
    lang_gre = stats.lang.value_counts()["gre"]
    lang_grc = stats.lang.value_counts()["grc"]
    lang_rus = stats.lang.value_counts()["rus"]
    lang_mul = stats.lang.value_counts()["mul"]
    

    
    df_stats = pd.DataFrame({'lang':[lang_ger, lang_eng, lang_fre, lang_ita, lang_spa, lang_por, lang_dut, lang_gre, lang_grc, lang_rus, lang_mul],
                            'Sprache':["Deutsch", "Englisch", "Französisch", "Italienisch", "Spanisch", "Portugiesisch", "Niederländlisch", "GRE", "GRC", "Russisch", "Mehrere Sprachen"]})
    
    fig_s = px.pie(df_stats, values='lang', names='Sprache', height=600, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_s, use_container_width=True)
    

elif visual=="Publikationsorte": 
    df = pd.read_json("geoplacecount.json", encoding="utf-8")
    #places = pd.read_json("data/geoplaces.json", encoding="utf-8") 
    #st.dataframe(places)
    
    #dfmerge = pd.merge(df, places, on='Place', how='left')
        
    #dfshort = dfmerge.head(10000)
    #st.dataframe(dfshort)
       
    #dfvis = dfshort.dropna(subset = ['gcode'])
    
    
    fig3 = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="Place",
                        size="count", color="count", color_continuous_scale=px.colors.cyclical.IceFire, zoom=5, height=500)
    fig3.update_layout(mapbox_style="open-street-map", 
                      mapbox=dict(
                            #accesstoken=mapbox_access_token,
                            bearing=0,
                            center=dict(
                                    lat=51.10,
                                    lon=10.27
                                            ))
                        )  
    fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig3.update_traces(marker_sizemin = 5, marker_sizeref = 10)
    st.plotly_chart(fig3, use_container_width=True)
    
        
       
    
else: 
    
    st.warning("Noch nicht verfügbar - bitte schauen Sie später noch einmal vorbei.") 
