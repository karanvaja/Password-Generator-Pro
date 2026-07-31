"""
Password Manager - Handles password storage and management
"""

from datetime import datetime
from .encryption import EncryptionManager

class PasswordManager:
    """Manage storage, retrieval, and organization of passwords"""
    
    def __init__(self, password_file="passwords.enc"):
        self.password_file = password_file
        self.encryption = EncryptionManager()
        self.passwords = {}
        self.load_passwords()
    
    def load_passwords(self):
        """Load passwords from encrypted file"""
        self.passwords = self.encryption.decrypt_file(self.password_file)
        if not isinstance(self.passwords, dict):
            self.passwords = {}
    
    def save_passwords(self):
        """Save passwords to encrypted file"""
        self.encryption.encrypt_file(self.password_file, self.passwords)
    
    def add_password(self, title, password, category="Uncategorized", note=""):
        """Add a new password entry"""
        if title in self.passwords:
            return False, f"Password for '{title}' already exists"
        
        self.passwords[title] = {
            'password': password,
            'category': category,
            'note': note,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.save_passwords()
        return True, f"Password for '{title}' saved successfully"
    
    def get_password(self, title):
        """Retrieve password by title"""
        return self.passwords.get(title)
    
    def delete_password(self, title):
        """Delete a password entry"""
        if title not in self.passwords:
            return False, f"Password for '{title}' not found"
        del self.passwords[title]
        self.save_passwords()
        return True, f"Password for '{title}' deleted"
    
    def get_all_passwords(self):
        """Get all passwords"""
        return self.passwords
    
    def search(self, query):
        """Search passwords by title or note"""
        query_lower = query.lower()
        results = {}
        for title, data in self.passwords.items():
            if query_lower in title.lower() or query_lower in data.get('note', '').lower():
                results[title] = data
        return results
    
    def export_passwords(self, file_path):
        """Export passwords to encrypted file"""
        self.encryption.encrypt_file(file_path, self.passwords)
    
    def import_passwords(self, file_path, merge=True):
        """Import passwords from encrypted file"""
        imported = self.encryption.decrypt_file(file_path)
        if not imported:
            return False, "No data found in import file"
        if merge:
            self.passwords.update(imported)
        else:
            self.passwords = imported
        self.save_passwords()
        return True, f"Imported {len(imported)} passwords"
    
    def get_stats(self):
        """Get password statistics"""
        stats = {'total': len(self.passwords), 'categories': 0, 'by_category': {}}
        for data in self.passwords.values():
            category = data.get('category', 'Uncategorized')
            if category not in stats['by_category']:
                stats['by_category'][category] = 0
            stats['by_category'][category] += 1
        stats['categories'] = len(stats['by_category'])
        return stats