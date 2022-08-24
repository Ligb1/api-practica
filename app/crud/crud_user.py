from typing import Any, Dict, Optional, Union

from firebase_admin import db

from app.models.User import User


class CRUDUser:

    # Metodo que optiene todos los usuarios de la base de datos.
    def get_all(self, db: db) -> User:

        users = db.collection("usuarios").stream()
        users = [user.to_dict() for user in users]
        return users

    # Metodo que optiene el usuario especifico dado su email.
    def get_by_email(self, email: str, db: db) -> User:

        users = db.collection("usuarios").document(email).get().to_dict()
        print(users)
        return users


user = CRUDUser()
