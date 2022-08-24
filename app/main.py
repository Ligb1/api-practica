from typing import Union

from fastapi import FastAPI

from app.models.User import User

from app.db.conection import db

from app.crud.crud_user import user

app = FastAPI()

# Enpoint que trae todos los usuarios de la base de datos.
@app.get("/users")
def read_all():
    users = user.get_all(db)
    return users


# Enpoint que trae un usuario especifico de la base de datos dado su email.
@app.get("/users/{email}")
def read_user(email: str):

    users = user.get_by_email(email, db)
    return users
