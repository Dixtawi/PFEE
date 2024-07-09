import requests
import pandas as pd
import numpy as np
import random
import os
from concrete.ml.deployment import FHEModelClient

# Load test data
test_data = pd.read_csv(os.path.join(os.path.abspath(os.getcwd()), 'dataset', 'processed', 'test_data.csv'))

# Select a random row of test data
random_index = random.randint(0, len(test_data) - 1)
selected_data = test_data.iloc[random_index, :-1].values.reshape(1, -1).astype(np.float32)

# Initialize the FHE client
fhe_directory = os.path.join(os.path.abspath(os.getcwd()), 'models', 'fhe_files')
client = FHEModelClient(path_dir=fhe_directory, key_dir=fhe_directory)
serialized_evaluation_keys = client.get_serialized_evaluation_keys()

# Send evaluation keys to server (one time only)
response = requests.post('http://127.0.0.1:5000/evaluation_keys', json={'keys': serialized_evaluation_keys.hex()})

# Pre-process and encrypt data
encrypted_data = client.quantize_encrypt_serialize(selected_data)

# Send encrypted data to server for prediction
response = requests.post('http://127.0.0.1:5000/predict', json={'data': encrypted_data.hex()})
encrypted_prediction = bytes.fromhex(response.json()['prediction'])

# Decrypt the result
prediction = client.deserialize_decrypt_dequantize(encrypted_prediction)

# Convert prediction to 0 or 1
binary_prediction = np.argmax(prediction, axis=1)
print('Prediction:', binary_prediction)
