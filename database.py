import firebase_admin
from firebase_admin import credentials, firestore
import os

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    # Option 1: Use service account key file
    cred_path = os.path.join(os.path.dirname(__file__), os.getenv('FIREBASE_CREDENTIALS_PATH', 'firebase-config.json'))
    if os.path.exists(cred_path):
        cred = credentials.Certificate(cred_path)
    else:
        # Option 2: Use project config (same as React Native app)
        firebase_config = {
            "type": "service_account",
            "project_id": "test-project-5e082",
            "private_key_id": "ad4a898fb4a2fa74cbf30549a2f8f9a5bc3e7b81",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC1T8OxTgcDk6a4\ncgXDL2+vhhAiC2/gGuXhgSMrrgxm23a08Ze7IYMIyDeXRoKaX8nuYOAKW6NVj9fC\nCEqLpOFvyWz36x5wwCoEVCFDkxkTVv3mzxyouKXdazq0dqFpYFuGSfZfjeDL3YBI\npRkDWUePMU/FPK01Vk1xrmBuld+zK/t4cXu7XKk4TGIg8nov8CYlUkxp3Gm8U5Sc\nVMC3gO2zK8HmpqY/Ocni2Slrssi1qm5ZZAXqO+G2DVkZXf0O+di+JS1bYboeJMHC\nbL35ZoluJWs+pR5GGbjqcR8A6K+T+UsK69cS4lVDAKjzizXfGVfNVjok8ThRUFvi\n5Rq7tNyTAgMBAAECggEABXNYlIfIzIc6Sljcf9HOajjosD/8GivE1bgjnghf8BGl\n6mpJikMcz31GtTdV7XJ2vWylH4/srkGiQKouJNo35WaT7jS1GA+hfmV8Zdh8tv5K\nU2TOMuubdOITLuH9bTphK1LQOMQo9LKmd3NFzWTNiBT5QG/YBylJL7iIcUVJJyIy\nOuwFKtNrzsV0YczZhQfHZ+vFJxm76tFPgaie0IguXI9eHYhIGFe54G7NUDT4KaCd\nu1YdfJGNW1qjWf32Kq/7WygRMI4rzlpqfMbwzGn6y0sWie9tHQTzLsNMCmk5rfHY\nZJDJkSzIoSsdJ1kpi7UvRAFClNnweoooTzSDEoFOzQKBgQDbmACEWXQ1UMlD7dnt\ngcwCi4oUqlL1IA9GKP8GBJ74W3ELmQ9T31vHefCtVSmOO62qj8Q17/lZcNmgRmPn\nWMx1M58sWwf1c2TXcnFbLiwYXNCB/RM/Ru/q5x8RTb7XiOMfc8nTwd/pkWwJg8VP\nclLF0ceYJlBUYnJWGZTsr5dszQKBgQDTXv2BLijR3jWL68Xjjz32NGK/gdS7EtPY\nmbyfSJ2JvoCbYCRwlzNqUW5apkEbpZxCuMYaK4t1gaVIbqrNRfpcWtiZguRHXCxT\nfndFr1eQaY2sNCtHTQgJsSMgxhQGMU6QG/McExdz6Fx4Ip0Xcz4d7FRSloB+LCil\n/xZobkFu3wKBgHotDQSV/Kj5RLGtsVWKpOY5mt66kSNe7gCcKJ/BjG0j+zZ3t2Zz\n3E2U08qsmk1PeOVvzbwwwyv3NK4O2+DIsCD5UrNMBpaS2GVigB06CECZy0y3cLEB\nF9U7ODbZabfjqnJCauWNdbYvOcvla68zLUhw2jsV/hWlHHY5D3nMjFR1AoGASVXB\nupobS4U/Ksaop+VA6DUQtcUD28wSeCoOyWzWS74uvLnEqtOq4Q5TrVvVZxQ0fOnC\nwb2t6x0KDXFoDURkMrrKP6isLx4JuwY7t4+4X8BfiQmoolpVmZc9ytcuh1+AFHu+\nA1WUY4CQ5JWNz18KhDNEpkrVVfFYQQ+Z5K2sQh0CgYEAhHtF2DbEXWD8GrXXtE9B\nmCKbncmDPJ0Ps26Aj2f+TsoX7nrF/nClleGkqst9+b20DJdGniTH6/GUUrrtE9FP\nC8krm+z3yGNOrYr4rolBRDYwhkqEco0nM5BokXeN+Ytj3wlNBUDmHxdV7t+3vxhI\nuu8iG2v6Btz54Toz6w5XkK4=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-fbsvc@test-project-5e082.iam.gserviceaccount.com",
            "client_id": "100521982521779310338",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40test-project-5e082.iam.gserviceaccount.com",
            "universe_domain": "googleapis.com"
        }
        cred = credentials.Certificate(firebase_config)
    
    firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

def get_firestore_db():
    return db