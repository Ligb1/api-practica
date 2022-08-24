from pydantic import BaseModel

# Modelo que representa al usuario y sus 3 atributos correspondientes.
class User(BaseModel):
    name: str
    last_name: str
    email: str
