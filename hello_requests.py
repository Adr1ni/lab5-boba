import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print("Ejecutando Hola Mundo desde Requests! Respuesta:", response.json())
