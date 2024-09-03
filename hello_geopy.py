from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="hola_mundo_app")
location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
print(f"Ejecutando Hola Mundo desde Geopy! Ubicación: {location.address}")
