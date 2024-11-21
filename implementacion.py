from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

# Configurar la aplicación Flask
app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir solicitudes desde cualquier origen

# Cargar el modelo y el vectorizador
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener la reseña desde la solicitud
    data = request.json
    review = data.get('review', '')
     if len(review) > 200:
        return jsonify({'error': 'Reseña demasiado larga. El máximo permitido es 200 caracteres.'}), 400

    if not review:
        return jsonify({'error': 'No review provided'}), 400

    # Transformar la reseña en vector TF-IDF
    review_vect = vectorizer.transform([review])

    # Hacer la predicción
    prediction = model.predict(review_vect)[0]

    # Retornar la predicción como respuesta JSON
    return jsonify({'review': review, 'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
