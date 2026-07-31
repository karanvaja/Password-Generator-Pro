"""
Encryption Manager - Handles all encryption/decryption operations
"""

import os
import json
from cryptography.fernet import Fernet

class EncryptionManager:
    """Manage encryption and decryption of sensitive data"""
    
    def __init__(self, key_file="master.key"):
        self.key_file = key_file
        self.cipher = None
        self.setup_encryption()
    
    def setup_encryption(self):
        """Setup encryption key and cipher"""
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
        self.cipher = Fernet(key)
    
    def encrypt_data(self, data):
        """Encrypt data dictionary"""
        json_data = json.dumps(data).encode()
        return self.cipher.encrypt(json_data)
    
    def decrypt_data(self, encrypted_data):
        """Decrypt encrypted data"""
        try:
            decrypted = self.cipher.decrypt(encrypted_data)
            return json.loads(decrypted.decode())
        except Exception:
            return {}
    
    def encrypt_file(self, file_path, data):
        """Encrypt and save data to file"""
        with open(file_path, 'wb') as f:
            f.write(self.encrypt_data(data))
    
    def decrypt_file(self, file_path):
        """Decrypt data from file"""
        if os.path.exists(file_path):
            try:
                with open(file_path, 'rb') as f:
                    return self.decrypt_data(f.read())
            except Exception:
                return {}
        return {}