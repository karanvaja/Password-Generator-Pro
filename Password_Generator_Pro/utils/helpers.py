"""
Helpers - Utility functions
"""

import tkinter as tk
from datetime import datetime

def copy_to_clipboard(text):
    """
    Copy text to clipboard
    
    Args:
        text: Text to copy
    Returns:
        bool: True if successful, False otherwise
    """
    if not text:
        return False
    
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        root.clipboard_clear()
        root.clipboard_append(text)
        root.destroy()
        return True
    except Exception:
        return False

def mask_password(password):
    """
    Mask password for display
    
    Args:
        password: Password to mask
    Returns:
        str: Masked password
    """
    if not password:
        return ""
    
    if len(password) <= 8:
        return "*" * len(password)
    
    return "*" * min(len(password), 10)

def truncate_text(text, max_length=50):
    """
    Truncate text to maximum length
    
    Args:
        text: Text to truncate
        max_length: Maximum length
    Returns:
        str: Truncated text
    """
    if not text:
        return ""
    
    if len(text) <= max_length:
        return text
    
    return text[:max_length - 3] + "..."

def format_date(date_str):
    """
    Format date string for display
    
    Args:
        date_str: Date string to format
    Returns:
        str: Formatted date
    """
    if not date_str:
        return "N/A"
    
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return dt.strftime('%b %d, %Y at %I:%M %p')
    except:
        return date_str