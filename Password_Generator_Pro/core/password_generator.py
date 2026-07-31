"""
Password Generator - Core password generation logic
"""

import random
import secrets
import string
import re
import hashlib
import base64
import math
from datetime import datetime
from utils.constants import WORD_LISTS

class PasswordGenerator:
    """Generate secure passwords using multiple strategies"""
    
    def __init__(self):
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.digits = "0123456789"
        self.letters = string.ascii_letters
    
    def generate_cupp_password(self, profile_data):
        """Generate password based on personal information (CUPP style)"""
        info = []
        for key, value in profile_data.items():
            if value and value.strip():
                info.append(value.strip().lower())
        
        if not info:
            return self.generate_quantum_password(length=16)
        
        variations = []
        for i in range(len(info)):
            for j in range(len(info)):
                if i != j:
                    variations.append(f"{info[i]}{info[j]}")
                    variations.append(f"{info[i]}{random.randint(0, 99)}{info[j]}")
                    variations.append(f"{info[i]}{random.choice(self.special_chars)}{info[j]}")
        
        if variations:
            base = random.choice(variations)
            while len(base) < 12:
                base += random.choice(self.letters)
            return self.add_complexity(base)
        return self.generate_quantum_password(length=16)
    
    def generate_quantum_password(self, length=32, entropy_sources=None):
        """Generate quantum-resistant password"""
        if entropy_sources is None:
            entropy_sources = ['system', 'time']
        
        entropy_data = b''
        if 'system' in entropy_sources:
            entropy_data += secrets.token_bytes(32)
        if 'time' in entropy_sources:
            entropy_data += str(datetime.now().timestamp()).encode()
        if 'random' in entropy_sources:
            entropy_data += str(random.random()).encode()
        
        hash_obj = hashlib.sha512(entropy_data)
        hash_bytes = hash_obj.digest()
        
        password = base64.b64encode(hash_bytes).decode()
        password = re.sub(r'[^a-zA-Z0-9!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', '', password)
        
        while len(password) < length:
            password += random.choice(self.letters + self.digits + self.special_chars)
        password = password[:length]
        
        return self.add_complexity(password)
    
    def generate_memorable_password(self, word_count=4, separator='-', 
                                   include_numbers=True, include_special=True,
                                   word_source='common'):
        """Generate memorable but secure password"""
        words = WORD_LISTS.get(word_source, WORD_LISTS['common'])
        num_words = min(word_count, len(words))
        selected = random.sample(words, num_words)
        
        for i in range(len(selected)):
            if random.random() > 0.5:
                selected[i] = selected[i].capitalize()
        
        password = separator.join(selected)
        
        if include_numbers:
            password += str(random.randint(10, 99))
        if include_special:
            for _ in range(2):
                pos = random.randint(0, len(password))
                password = password[:pos] + random.choice(self.special_chars) + password[pos:]
        
        return self.add_complexity(password)
    
    def add_complexity(self, password):
        """Ensure password contains all required character types"""
        if not re.search(r'[A-Z]', password):
            pos = random.randint(0, len(password))
            password = password[:pos] + random.choice(string.ascii_uppercase) + password[pos:]
        if not re.search(r'[a-z]', password):
            pos = random.randint(0, len(password))
            password = password[:pos] + random.choice(string.ascii_lowercase) + password[pos:]
        if not re.search(r'\d', password):
            pos = random.randint(0, len(password))
            password = password[:pos] + random.choice(self.digits) + password[pos:]
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:,.<>?]', password):
            pos = random.randint(0, len(password))
            password = password[:pos] + random.choice(self.special_chars) + password[pos:]
        return password
    
    def calculate_entropy(self, password):
        """Calculate entropy of a password"""
        if not password:
            return 0
        charset_size = len(set(password))
        return len(password) * math.log2(charset_size)