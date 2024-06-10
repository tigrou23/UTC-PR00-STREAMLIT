import json
import pandas as pd
import requests
import streamlit as st
import pydeck as pdk

try :
    # Requêtes à l'API
    itineraire_req = requests.get('http://hugopereira.fr:3000/itineraires')
    itineraire_req.raise_for_status()
except requests.exceptions.HTTPError:
    st.header("⚠️ Impossible de se connecter à l'API. ⚠️")
    st.write("Vérifiez votre connexion ou contactez le support.")
else :
    # Construction des Dataframes globales
    st.title("Utilisation de l'application :")
    print(itineraire_req.text)
    data_itineraire = json.loads(itineraire_req.text)
    itineraire = pd.DataFrame(data_itineraire)

    st.write("## Nombre d'utilisation de l'application :", len(itineraire))

    st.write('### Répartition des modes de transport :')
    mode_transport = itineraire['mode'].value_counts()
    mode_transport = mode_transport.reset_index()
    mode_transport.columns = ['Mode de transport', 'Nombre de participants']
    st.bar_chart(mode_transport.set_index('Mode de transport'))

    st.write('### Localisation des participants :')
    villes = []
    coordonnees = ['', '']
    for i in range(len(itineraire)):
        if itineraire['latitude_depart'][i] and itineraire['longitude_depart'][i]:
            print(itineraire['latitude_depart'][i])
            coordonnees = ['', '']
            coordonnees[0] = float(itineraire['latitude_depart'][i])
            coordonnees[1] = float(itineraire['longitude_depart'][i])
            villes.append(coordonnees)
    dfs = [pd.DataFrame({'lat': [lat], 'lon': [lon]}) for lat, lon in villes]
    df = pd.concat(dfs, ignore_index=True)

    vue = st.radio(
        "Sélectionnez la vue :",
        ('2D', '3D'),
    )
    if vue == '2D':
        st.map(df)
    else:
        st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=48.856614,
                longitude=2.3522219,
                zoom=9,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    'HexagonLayer',
                    data=df,
                    get_position='[lon, lat]',
                    radius=200,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df,
                    get_position='[lon, lat]',
                    get_color='[200, 30, 0, 160]',
                    get_radius=200,
                ),
            ],
        ))