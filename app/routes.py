from flask import Blueprint, request, jsonify
from .anomaly_detection import predict_anomaly

main_routes = Blueprint('main_routes', __name__)

# Define route for anomaly prediction
@main_routes.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get('features')
    
    if not features:
        return jsonify({'error': 'No features provided'}), 400

    # Call the anomaly detection function
    prediction = predict_anomaly(features)
    return jsonify({'prediction': int(prediction[0])})
