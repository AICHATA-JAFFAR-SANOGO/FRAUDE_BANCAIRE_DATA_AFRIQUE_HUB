import streamlit as st
import requests

# URL de l'API FastAPI
api_url = "http://localhost:8000/predict/"

# Chargement des noms des colonnes (incluant les V1 à V28 et Amount)
X_columns = [
    'Amount', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
    'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',
    'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28'
]

# Définition de la mise en page de la page Streamlit
st.set_page_config(page_title="Détection des Fraudes Bancaires", layout="wide")
st.title("Détection des Fraudes Bancaires 🏦💳")

# Application  de style à la page
st.markdown(
    """
    <style>
    .main {
        background-color: #121212; /* Couleur de fond sombre */
        color: #E0E0E0; /* Couleur du texte claire pour contraste */
    }
    .stButton>button {
        background-color: #1F1F1F;
        color: #E0E0E0;
        font-size: 18px;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
    }
    .stNumberInput>div>label>span,
    .stTextInput>div>label>span {
        font-size: 16px;
        color: #E0E0E0;
    }
    .stMarkdown>p {
        color: #E0E0E0;
        font-size: 18px;
        font-weight: bold;
    }
    footer {
        font-size: 14px;
        color: #B0BEC5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Création d'une colonne pour la disposition
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="color: #E0E0E0;">Entrez les détails de la transaction</h2>
        <p style="color: #B0BEC5;">Veuillez remplir les champs suivants pour analyser la transaction.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Entrées utilisateur pour le montant et les caractéristiques
col1, col2 = st.columns([2, 1])

with col1:
    amount = st.number_input('Montant de la Transaction (€)', min_value=0.0, format="%.2f")
    features = [st.number_input(f'Feature {col}', value=0.0, format="%.2f") for col in X_columns[1:]]

with col2:
    st.write("### Instructions")
    st.write("1. Entrez le montant de la transaction.")
    st.write("2. Entrez les valeurs pour chaque caractéristique.")
    st.write("3. Cliquez sur le bouton **Analyser** pour détecter la fraude.")

if st.button('Analyser'):
    # Préparation des données d'entrée pour l'API
    input_data = {col: features[i] for i, col in enumerate(X_columns[1:])}
    input_data['Amount'] = amount
    
    # Appel à l'API
    response = requests.post(api_url, json=input_data)
    prediction = response.json().get("prediction", "Erreur de prédiction")

    # Affichage de  la prédiction avec des messages personnalisés et des icônes
    if prediction == "fraudulent":
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://img.icons8.com/ios-filled/50/ff6f6f/sad.png" style="width: 150px; height: 150px;" />
                <h2 style="color: #FF5252;">Cette transaction est frauduleuse ! 😭</h2>
                <p style="color: #E0E0E0;">Cette transaction est suspecte. Veuillez vérifier les détails.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.balloons()
    else:
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://img.icons8.com/ios-filled/50/7acaa7/happy.png" style="width: 150px; height: 150px;" />
                <h2 style="color: #66BB6A;">Cette transaction est normale ! 😊</h2>
                <p style="color: #E0E0E0;">Tout semble en ordre avec cette transaction.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.snow()

st.markdown(
    """
    <footer>
        <p style="text-align: center; color: #B0BEC5;">Développé par AICHATA JAFFAR SANOGO | © 2024</p>
    </footer>
    """,
    unsafe_allow_html=True
)
