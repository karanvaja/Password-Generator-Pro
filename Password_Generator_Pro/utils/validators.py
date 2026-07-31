"""
Validators - Input validation functions
"""

import re

def validate_password(password, min_length=8):
    """
    Validate password against basic requirements
    
    Args:
        password: Password to validate
        min_length: Minimum length requirement
    Returns:
        tuple: (is_valid, message)
    """
    if not password:
        return False, "Password cannot be empty"
    
    if len(password) < min_length:
        return False, f"Password must be at least {min_length} characters long"
    
    # Check for at least 3 character types
    char_types = [
        bool(re.search(r'[A-Z]', password)),
        bool(re.search(r'[a-z]', password)),
        bool(re.search(r'\d', password)),
        bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:,.<>?]', password))
    ]
    
    if sum(char_types) < 3:
        return False, "Password must contain at least 3 of the following: uppercase, lowercase, digits, special characters"
    
    return True, "Password meets minimum requirements"

def validate_title(title):
    """
    Validate password title
    
    Args:
        title: Title to validate
    Returns:
        tuple: (is_valid, message)
    """
    if not title or not title.strip():
        return False, "Title cannot be empty"
    
    if len(title) > 100:
        return False, "Title is too long (maximum 100 characters)"
    
    # Check for invalid characters
    if re.search(r'[<>:"/\\|?*]', title):
        return False, "Title contains invalid characters"
    
    return True, "Title is valid"

def validate_category(category):
    """
    Validate category name
    
    Args:
        category: Category to validate
    Returns:
        tuple: (is_valid, message)
    """
    if not category:
        return True, "Category is optional"
    
    if len(category) > 50:
        return False, "Category name is too long (maximum 50 characters)"
    
    return True, "Category is valid"

def validate_note(note):
    """
    Validate note content
    
    Args:
        note: Note to validate
    Returns:
        tuple: (is_valid, message)
    """
    if note and len(note) > 2000:
        return False, "Note is too long (maximum 2000 characters)"
    
    return True, "Note is valid"