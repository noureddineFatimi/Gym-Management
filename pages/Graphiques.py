import requests
import streamlit as st
import pandas as pd
import plotly.express as px

page_bg_img = """
<style>
[data-testid="stApp"]{ 
    background-color: #c0d4ec;
    color: #000000;
}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)
# URL pour les données d'entraîneurs
url_entraineur = 'https://apex.oracle.com/pls/apex/wksp_noureddine/entrain_eur//?limit=10000'

# URL pour les données d'horaire
url_horaire = 'https://apex.oracle.com/pls/apex/wksp_noureddine/horai_re/?limit=10000'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Récupération des données depuis les URLs
response_entraineur = requests.get(url_entraineur, headers=headers)
response_horaire = requests.get(url_horaire, headers=headers)

# Assurez-vous que la requête a réussi avant de continuer
if response_entraineur.status_code == 200 and response_horaire.status_code == 200:
    # Convertissez les données JSON en DataFrames pandas
    df_entraineur_new = pd.DataFrame(response_entraineur.json()["items"])
    df_horaire_new = pd.DataFrame(response_horaire.json()["items"])

    # Définissez les DataFrames si elles ne sont pas déjà définies
    if 'df_entraineur' not in globals():
        df_entraineur = pd.DataFrame(columns=['codee', 'nom', 'prenom'])
    if 'df_horaire' not in globals():
        df_horaire = pd.DataFrame(columns=['codee', 'jour', 'heuredebut', 'duree'])

    # Ajoutez les nouvelles données à vos DataFrames existants df_eeentraineur et df_hhhoraire
    df_entraineur = pd.concat([df_entraineur, df_entraineur_new[['codee', 'nom', 'prenom']]], ignore_index=True)
    df_horaire = pd.concat([df_horaire, df_horaire_new[['codee', 'jour', 'heuredebut', 'duree']]], ignore_index=True)

    # Triez le DataFrame par la colonne 'jour' et 'heure_de_debut'
    df_horaire = df_horaire.sort_values(by=["jour", "heuredebut"])

    # Créez l'ordre des jours de la semaine
    jours_ordre = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI"]

    # Graphique à barres pour le nombre de séances par plage horaire
    fig_bar = px.bar(df_horaire, x="heuredebut", title="Nombre de séances par plage horaire")
    df_horaire['jour']= pd.Categorical(df_horaire['jour'],categories=jours_ordre, ordered=True)
    # Graphique à courbes pour le nombre de séances par jour de la semaine
    fig_line = px.line(
        df_horaire.groupby("jour").size().reset_index(name="nombre_seances"),
        x="jour",
        y="nombre_seances",
        title="Nombre de séances par jour de la semaine"
    )

    # Ordonner les jours de la semaine
    fig_line.update_xaxes(categoryorder='array', categoryarray=jours_ordre)

    # Affichage des graphiques sur la page
    st.title("Graphiques sur les séances programmées")

    # Graphique à barres
    st.plotly_chart(fig_bar)

    # Graphique à courbes
    st.plotly_chart(fig_line)

    st.success("Les données ont été mises à jour avec succès.")
else:
    st.error("Échec de la récupération des données depuis les URLs.")