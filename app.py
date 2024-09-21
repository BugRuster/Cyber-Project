from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model (rf_model.pkl)
with open('models/rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

# Define the root route ('/')
@app.route('/')
def index():
    return render_template('dashboard.html')

# Define a route for anomaly detection API
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)

    # Convert the data into the format the model expects
    input_features = np.array([data['features']])

    # Make a prediction
    prediction = rf_model.predict(input_features)


    output = {'prediction': int(prediction[0])}
    return jsonify(output)

if __name__ == '__main__':

    app.run(host='172.168.1.1', port=8080, ssl_context=('certs/cert.pem', 'certs/key.pem'))
