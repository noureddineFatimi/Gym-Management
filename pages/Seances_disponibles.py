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
seances_data = fetch_data('sean_ce')


# Conversion des données en DataFrame
df_seances = pd.DataFrame(seances_data['items'])

# Fonction de filtrage par nom de famille
def filtrer_par_type(df, tyype):
    if tyype:
        df = df[df['type'].str.contains(tyype, case=False)]
    return df

# Fonction de filtrage par plage de dates de naissance
# Titre de la page
st.title("Seances Disponibles")

# Widget de filtrage par nom de famille
type_de_seances = st.text_input("Filtrer par type de seances")
df_filtre_type = filtrer_par_type(df_seances, type_de_seances)

# Widget de filtrage par plage de dates de naissance
# Affichage des entraîneurs filtrés
if df_filtre_type.empty:
    st.warning("Aucun seance trouvé avec le critère de filtrage sélectionné.")
else:
    st.subheader("Seances disponibles")
    st.write(df_filtre_type)
    for _, row in df_filtre_type.iterrows():
        st.write(f"Nom de seance: {row['nom']},     Type de seance: {row['type']}")