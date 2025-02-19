import streamlit as st
import pandas as pd
import numpy as np
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
def insert(code_e, jour, heure_debut, duree, id_s, gym_salle):
    url = 'https://apex.oracle.com/pls/apex/wksp_noureddine/horai_re/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    data = {
            "codee": code_e,
            "ids": id_s,
            "jour": jour,
            "heuredebut":  heure_debut,
            "duree": duree,
            "gymsalle": gym_salle 
    }

    response = requests.post(url, headers=headers, json=data)    #to insert


    if response.status_code == 201:
        
        st.write('Data inserted successfully')
    else:
        st.write('Failed to insert data:', response.text)




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
seances_data = fetch_data('sean_ce')
horaire_data = fetch_data('horai_re')

# Conversion des données en DataFrame
df_entraineurs = pd.DataFrame(entraineurs_data['items'])
df_seances = pd.DataFrame(seances_data['items'])
df_horaire = pd.DataFrame(horaire_data['items'])

# Titre de la page
st.title("Insertion d'une nouvelle séance hebdomadaire")

# Formulaire d'insertion de séance
with st.form(key='insert_seance_form'):
    # Champ CodeE (sélection de l'entraîneur depuis la base de données)
    code_e = st.selectbox("Sélectionnez l'entraîneur (CodeE)", options=df_entraineurs)

    # Champ Jour (sélection du jour de la semaine)
    jour = st.selectbox("Sélectionnez le jour de la semaine", options=["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"])

    # Champ Heure de début (sélection avec un curseur)
    heure_debut = st.slider("Heure de début", min_value=0, max_value=23)

    # Champ Durée (sélection avec un curseur)
    duree = st.slider("Durée (en minutes)", min_value=1, max_value=60)

    # Champ Id-S (sélection de la séance depuis la base de données)
    id_s = st.selectbox("Sélectionnez la séance (Id-S)", options=df_seances)

    # Champ GymSalle (saisie manuelle)
    gym_salle = st.text_input("GymSalle")

    # Bouton de soumission du formulaire
    submitted = st.form_submit_button("Insérer la séance")

    # Vérification des champs et insertion des données
    if submitted:
        if duree > 60:
            # Affichage du message d'erreur en cas de durée supérieure à 60 minutes
            st.error("La durée ne peut pas dépasser 60 minutes.")
        elif jour not in ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]:
            # Affichage du message d'erreur en cas de jour invalide
            st.error("Veuillez sélectionner un jour valide (du lundi au vendredi).")
        else:

            insert(code_e, jour, heure_debut, duree, id_s, gym_salle)
            st.success("Séance insérée avec succès.")