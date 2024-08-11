import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données prétraitées
df = pd.read_csv('X_preprocessed.csv')
y = pd.read_csv('y_preprocessed.csv')

# Ajout de la colonne de classes à df
df['Class'] = y

# Configuration des graphiques
sns.set(style="whitegrid")

# 1. Distribution des classes
plt.figure(figsize=(8, 6))
sns.countplot(x='Class', data=df)
plt.title('Distribution des Classes')
plt.xlabel('Class')
plt.ylabel('Nombre de Transactions')
plt.savefig('distribution_classes.png')  # Sauvegarde du graphique
plt.close() 

# 2. Répartition des montants de transaction par classe
plt.figure(figsize=(10, 6))
sns.histplot(df[df['Class'] == 0]['Amount'], bins=50, label='Normales', color='blue', kde=True)
sns.histplot(df[df['Class'] == 1]['Amount'], bins=50, label='Frauduleuses', color='red', kde=True)
plt.title('Répartition des Montants de Transaction par Classe')
plt.xlabel('Montant')
plt.ylabel('Fréquence')
plt.legend()
plt.savefig('repartition_montants.png')  
plt.close()  

# 3. Heatmap des caractéristiques (corrélations)
plt.figure(figsize=(12, 10))
corr = df.corr()
sns.heatmap(corr, cmap='coolwarm', annot=False, fmt=".1f", linewidths=0.5)
plt.title('Heatmap des Corrélations entre les Caractéristiques')
plt.savefig('heatmap_correlations.png')  
plt.close()  

# 4. Pairplot des premières caractéristiques (exemple)
sns.pairplot(df[['Amount', 'V1', 'V2', 'Class']], hue='Class')
plt.title('Pairplot des Caractéristiques')
plt.savefig('pairplot_caracteristiques.png')  
plt.close()  

print("Les graphiques ont été sauvegardés en tant que fichiers image.")
