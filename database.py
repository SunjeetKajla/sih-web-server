import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

# Initialize Firebase Admin SDK
def initialize_firebase():
    if not firebase_admin._apps:
        try:
            # Try file first (simpler for Render)
            cred_path = 'firebase-config.json'
            if os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
                return True
            else:
                print("Firebase config file not found")
                return False
        except Exception as e:
            print(f"Firebase initialization error: {e}")
            return False
    return True

# Initialize Firebase when module is imported
initialize_firebase()

def get_firestore_db():
    # Initialize Firestore client only when needed
    return firestore.client()