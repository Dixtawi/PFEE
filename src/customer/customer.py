import requests
import pandas as pd
import numpy as np
import random
import os

# Load Test Data
test_data = pd.read_csv(os.path.join(os.path.abspath(os.getcwd()), 'dataset', 'processed', 'test_data.csv'))

# Select a random line in Test Data
random_index = random.randint(0, len(test_data) - 1)
selected_data = test_data.iloc[random_index, :-1].values

# Encryption function
def encrypt_data(data): # TODO
    return data

encrypted_data = encrypt_data(selected_data)

# Convert numpy.bool_ to bool for JSON serialization
def convert_to_native_python(data):
    if isinstance(data, np.bool_):
        return bool(data)
    elif isinstance(data, (list, np.ndarray)):
        return [convert_to_native_python(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_to_native_python(value) for key, value in data.items()}
    else:
        return data

# Convert encrypted_data to native Python types
converted_data = convert_to_native_python(encrypted_data)

# Send data to server
response = requests.post('http://127.0.0.1:5000/predict', json={'data': converted_data})
encrypted_prediction = response.json()['prediction']

# Decryption function
def decrypt_data(data): # TODO
    return data

prediction = decrypt_data(np.array(encrypted_prediction))

print('Prediction:', prediction)
