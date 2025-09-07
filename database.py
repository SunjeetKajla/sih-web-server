import firebase_admin
from firebase_admin import credentials, firestore
import os

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    # Option 1: Use service account key file
    cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH', 'firebase-config.json')
    if os.path.exists(cred_path):
        cred = credentials.Certificate(cred_path)
    else:
        # Option 2: Use project config (same as React Native app)
        firebase_config = {
            "type": "service_account",
            "project_id": "test-project-5e082",
            # Add your service account details here
        }
        cred = credentials.Certificate(firebase_config)
    
    firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

def get_firestore_db():
    return db