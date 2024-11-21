import requests

# URL de tu servidor Flask
url = "http://127.0.0.1:5000/predict"

# Solicitud con un ejemplo de reseña
data = {"review": "This app is amazing!"}
response = requests.post(url, json=data)

# Imprimir la respuesta
print(response.json())
