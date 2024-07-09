from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
from concrete.ml.sklearn.rf import RandomForestClassifier
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load model
model_params = joblib.load(os.path.join(os.path.abspath(os.getcwd()), 'models', 'fhe_model.pkl'))
model = RandomForestClassifier(**model_params)

# Loas Train Data
train_data = pd.read_csv(os.path.join(os.path.abspath(os.getcwd()), 'dataset', 'processed', 'train_data.csv'))

X_train = train_data.drop(columns=['prediction'])
y_train = train_data['prediction']
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Training model
model.fit(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    encrypted_data = np.array(data)

    # Prediction
    encrypted_prediction = model.predict(encrypted_data)

    return jsonify({'prediction': encrypted_prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)

