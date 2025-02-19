import streamlit as st
import pandas as pd
import datetime
import requests
page_bg_img = """
<style>
[data-testid="stApp"]{ 
    background-color: #c0d4ec;
    color: #000000;
}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)
def fetch_data(table_name):
    url = f'https://apex.oracle.com/pls/apex/wksp_noureddine/{table_name}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')


# Données des entraîneurs (exemple)
entraineurs_data = fetch_data('entrain_eur')


# Conversion des données en DataFrame
df_entraineurs = pd.DataFrame(entraineurs_data['items'])

# Fonction de filtrage par nom de famille
def filtrer_par_nom(df, nom):
    if nom:
        df = df[df['nom'].str.contains(nom, case=False)]
    return df

# Fonction de filtrage par plage de dates de naissance
def filtrer_par_date_naissance(df, date):
    if date:
        date = date.strftime('20%y-%m-%dT00:00:00Z')
        df = df[
            (df['datenaissance'] == date)
        ]
    return df

# Titre de la page
st.title("Entraîneurs Disponibles")

# Widget de filtrage par nom de famille
nom_entraineur = st.text_input("Filtrer par nom de famille de l'entraîneur")
df_filtre_nom = filtrer_par_nom(df_entraineurs, nom_entraineur)

# Widget de filtrage par plage de dates de naissance
date_nais = st.date_input("Date de naissance minimale")

df_filtre_date = filtrer_par_date_naissance(df_filtre_nom, date_nais)

# Affichage des entraîneurs filtrés
if df_filtre_date.empty:
    st.warning("Aucun entraîneur trouvé avec les critères de filtrage sélectionnés.")
else:
    st.subheader("Entraîneurs disponibles")
    st.write(df_filtre_date)
    for _, row in df_filtre_date.iterrows():
        st.write(f"Nom: {row['nom']},      Prénom: {row['prenom']}")
