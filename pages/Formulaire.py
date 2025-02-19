import streamlit as st
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
# Fonction pour insérer une nouvelle séance dans la base de données
def inserer_seance(id_s, nom, tyype, niveau):
    url = 'https://apex.oracle.com/pls/apex/wksp_noureddine/sean_ce/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Content-Type': 'application/json',  # Ajout de l'en-tête Content-Type
    }

    data = {
        "IDS": id_s,
        "NOM": nom,
        "TYPE": tyype,
        "NIVEAU": niveau
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        seance_data = response.json()

        if "ids" in seance_data:
            st.success("Séance insérée avec succès!")
        else:
            st.error("Erreur lors de l'insertion de la séance.")
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de requête : {e}")

# Page principale de l'application Streamlit
def main():
    st.title("Formulaire d'Insertion de Séance")

    # Formulaire de saisie pour la nouvelle séance
    id_s = st.number_input("ID de la séance", min_value=1)
    nom = st.text_input("Nom de la séance")
    tyype = st.text_input("Type de la séance")
    niveau = st.number_input("Niveau de la séance", min_value=1, max_value=4)
    

    # Bouton pour l'insertion de la séance
    if st.button("Insérer la Séance"):
        # Vérification des champs
        if id_s and nom and tyype and niveau:
            # Appel de la fonction d'insertion
            inserer_seance(id_s, nom, tyype, niveau)
        else:
            st.warning("Veuillez remplir tous les champs du formulaire.")

# Exécution de l'application principale
if __name__== "__main__":
    main()


