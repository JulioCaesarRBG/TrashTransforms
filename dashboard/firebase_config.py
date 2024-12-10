import firebase_admin
from firebase_admin import credentials, db
from decouple import config

cred = credentials.Certificate(config("FIREBASE_CREDENTIALS"))

if not firebase_admin._apps:
    firebase_admin.initialize_app(
        cred, {"databaseURL": config("FIREBASE_DATABASE_URL")}
    )

def get_database():
    return db.reference("/")

