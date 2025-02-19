import streamlit as st

page_bg_img = """
<style>
[data-testid="stApp"]{ 
    background-color: #c0d4ec;
    color: #000000;
[data-testid="stImage"]{
margin-left: 8vw;
width: 30vw;
}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)
# Fonction pour la page d'accueil
def home_page():
    st.title("Bienvenue à la page officielle de GYMFITNESS")
    st.image("photo/img1.jpg")

# Appel de la fonction pour afficher la page d'accueil
home_page()

description = """
Chez GymFitness, nous sommes fiers de vous offrir bien plus qu'un simple club de fitness. Nous sommes une communauté passionnée dédiée à votre santé, à votre forme physique et à votre bien-être général.

**Ce que nous offrons :**

1. **Installations de Pointe :** GymFitness dispose d'équipements de fitness de dernière génération pour vous offrir une expérience d'entraînement optimale. Des machines cardiovasculaires aux poids libres, nous avons tout ce dont vous avez besoin pour atteindre vos objectifs.

2. **Entraînement Personnalisé :** Nos entraîneurs qualifiés sont là pour vous guider à chaque étape de votre parcours. Ils créeront un programme personnalisé en fonction de vos besoins spécifiques, que vous souhaitiez perdre du poids, développer votre force musculaire ou simplement adopter un mode de vie plus sain.

3. **Variété de Cours :** De la musculation aux cours de groupe stimulants, nous proposons une variété de cours adaptés à tous les goûts. Rejoignez nos cours de yoga pour la flexibilité, nos sessions d'entraînement en groupe pour la motivation, ou travaillez en solo à votre propre rythme.

4. **Espace Détente :** Après une séance d'entraînement intense, détendez-vous dans notre espace spa ou sauna. La récupération est tout aussi importante que l'effort physique, et nous nous assurons que vous puissiez prendre soin de votre corps de manière holistique.

5. **Événements Communautaires :** Chez GymFitness, nous sommes plus qu'un club, nous sommes une famille. Participez à nos événements communautaires, des compétitions amicales aux ateliers sur la nutrition, pour rencontrer d'autres membres partageant les mêmes idées.

Rejoignez-nous chez GymFitness et faites partie d'une communauté qui valorise votre santé et votre bonheur. Que vous soyez débutant ou athlète confirmé, nous avons ce qu'il vous faut pour vous aider à atteindre vos objectifs. Votre aventure vers une vie plus saine commence ici. Bienvenue à GymFitness, où votre bien-être est notre priorité.
"""

st.markdown(description)
    