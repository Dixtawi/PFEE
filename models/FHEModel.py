from concrete.ml.sklearn import RandomForestClassifier
from concrete.ml.deployment import FHEModelDev
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os
import joblib

# Load training data
train_data = pd.read_csv(os.path.join(os.path.abspath(os.getcwd()), 'dataset', 'processed', 'train_data.csv'))
X_train = train_data.drop(columns=['prediction'])
y_train = train_data['prediction']
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Initialize and train the model
model_params = joblib.load(os.path.join(os.path.abspath(os.getcwd()), 'models', 'fhe_model.pkl'))
model = RandomForestClassifier(**model_params)
model.fit(X_train, y_train)

# Compile the model for homomorphic encryption
model.compile(X_train)

# Save model and specifications for client and server
fhe_directory = os.path.join(os.path.abspath(os.getcwd()), 'models', 'fhe_files')
dev = FHEModelDev(path_dir=fhe_directory, model=model)
dev.save()

print("Model trained, compiled, and saved.")
