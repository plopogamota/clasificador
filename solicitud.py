import requests

# URL de tu servidor Flask
url = "http://127.0.0.1:5000/predict"

# Solicitud con un ejemplo de reseña
data = {"review": "This app is amazing!"}
# Verifica si la reseña excede el límite de 500 caracteres
if len(data['review']) > 200:
    print("La reseña es demasiado larga. El máximo permitido es 200 caracteres.")
else:
    response = requests.post(url, json=data)
    # Imprimir la respuesta
    print(response.json())


