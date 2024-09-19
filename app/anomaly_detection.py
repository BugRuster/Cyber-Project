import pickle
import numpy as np

# Load the trained model (ensure the path to the model is correct)
with open('models/rf_model.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)

def predict_anomaly(features):
    features = np.array(features).reshape(1, -1)  # Reshape to match input format
    prediction = rf_model.predict(features)
    return prediction
