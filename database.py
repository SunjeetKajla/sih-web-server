import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    try:
        # Try environment variable first (for production)
        firebase_creds = os.getenv('FIREBASE_CREDENTIALS')
        if firebase_creds:
            cred_dict = json.loads(firebase_creds)
            cred = credentials.Certificate(cred_dict)
        else:
            # Fallback to file (for local development)
            cred_path = 'firebase-config.json'
            if os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
            else:
                raise Exception("No Firebase credentials found")
        
        firebase_admin.initialize_app(cred)
    except Exception as e:
        print(f"Firebase initialization error: {e}")
        # Initialize with minimal config to prevent crashes
        firebase_admin.initialize_app()

# Get Firestore client
db = firestore.client()

def get_firestore_db():
    return db