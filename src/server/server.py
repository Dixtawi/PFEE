from flask import Flask, request, jsonify
from concrete.ml.deployment import FHEModelServer
import os

app = Flask(__name__)

# Load FHE model
fhe_directory = os.path.join(os.path.abspath(os.getcwd()), 'models', 'fhe_files')
server = FHEModelServer(path_dir=fhe_directory)
server.load()

evaluation_keys = None

@app.route('/predict', methods=['POST'])
def predict():
    global evaluation_keys
    data = request.json['data']
    encrypted_data = bytes.fromhex(data)
    encrypted_result = server.run(encrypted_data, serialized_evaluation_keys=evaluation_keys)
    return jsonify({'prediction': encrypted_result.hex()})

@app.route('/evaluation_keys', methods=['POST'])
def receive_evaluation_keys():
    global evaluation_keys
    keys = request.json['keys']
    evaluation_keys = bytes.fromhex(keys)
    with open(os.path.join(fhe_directory, 'serialized_evaluation_keys.ekl'), 'wb') as f:
        f.write(evaluation_keys)
    return jsonify({'status': 'keys received'})

if __name__ == '__main__':
    app.run(debug=True)

