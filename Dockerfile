# Utilisation d' une image de base Python légère
FROM python:3.10-slim

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie du fichier requirements.txt et installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie de tous les fichiers du projet dans le conteneur
COPY . .

# Exposition des ports utilisés par FastAPI et Streamlit
EXPOSE 8000
EXPOSE 8501

# Commande pour démarrer FastAPI et Streamlit simultanément
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run app_streamlit.py --server.port=8501 --server.address=0.0.0.0"]
