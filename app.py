from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.models import load_model
import joblib
import numpy as np

app = Flask(__name__, template_folder='assets', static_folder='assets')

# Tải mô hình và scaler
model = load_model('house_price_model.keras')
scaler = joblib.load('scaler.pkl')

features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 
            'waterfront', 'view', 'condition', 'grade', 'sqft_above', 
            'sqft_basement', 'yr_built', 'yr_renovated', 'lat', 'long', 
            'sqft_living15', 'sqft_lot15', 'month', 'year']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(request.form[feature]) for feature in features]
    input_data = np.array(input_data).reshape(1, -1)
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)[0, 0]
    return render_template('index.html', prediction=f'Predicted Price: ${prediction:,.2f}')

@app.route('/assets/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)