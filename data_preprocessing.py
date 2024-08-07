import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.utils import resample

# Chargement du dataset
df = pd.read_csv('creditcard.csv')  

# Affichage des premières lignes et des informations du dataset
print(df.head())
print(df.info())

# Normalisation des données
scaler = StandardScaler()
features = df.drop('Class', axis=1)
scaled_features = scaler.fit_transform(features)

# Remplacement des caractéristiques normalisées dans le dataframe
df_scaled = pd.DataFrame(scaled_features, columns=features.columns)
df_scaled['Class'] = df['Class'].values

# Gestion des classes déséquilibrées
df_majority = df_scaled[df_scaled['Class'] == 0]
df_minority = df_scaled[df_scaled['Class'] == 1]

# Rééchantillonnage des classes minoritaires
df_minority_upsampled = resample(df_minority, 
                                 replace=True, 
                                 n_samples=len(df_majority), 
                                 random_state=123)

df_balanced = pd.concat([df_majority, df_minority_upsampled])

# Séparation des caractéristiques et les étiquettes
X = df_balanced.drop('Class', axis=1)
y = df_balanced['Class']

# Sauvegarde des données prétraitées pour l'entraînement du modèle
X.to_csv('X_preprocessed.csv', index=False)
y.to_csv('y_preprocessed.csv', index=False)

print("Prétraitement terminé et fichiers sauvegardés.")
