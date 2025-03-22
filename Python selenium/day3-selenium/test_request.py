import requests

#Petición a jsone
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# Miramos el estado de la respuesta 
assert response.status_code == 200, f"Error: Código de estado inesperado {response.status_code}"

# La respuesta anterior a json 
data = response.json()

# Validamos los datos 
assert "id" in data and data["id"] == 1, "Error: ID incorrecto en la respuesta"
assert "title" in data, "Error: No se encontró el campo 'title' en la respuesta"
assert "body" in data, "Error: No se encontró el campo 'body' en la respuesta"

# 
print(" Test succesfully : La API devolvió los datos esperados.")
print(data)
