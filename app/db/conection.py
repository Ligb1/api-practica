import firebase_admin
from firebase_admin import firestore, credentials


# Se certifica la conexcion con Firebase mediante el archivo Json.
cred = credentials.Certificate("pruebafb.json")
# Se inicializa la aplicacion de Firebase.
firebase_admin.initialize_app(cred)

# Se inicia el cliente de Firestore.
db = firestore.client()
