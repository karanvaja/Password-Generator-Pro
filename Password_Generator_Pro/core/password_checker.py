"""
Password Checker - Advanced password strength analysis
"""

import re
import math
from utils.constants import COMMON_PATTERNS, SEQUENTIAL_PATTERNS

class PasswordChecker:
    """Analyze password strength and provide recommendations"""
    
    def __init__(self):
        self.common_patterns = COMMON_PATTERNS
        self.sequential_patterns = SEQUENTIAL_PATTERNS
    
    def check_strength(self, password):
        """Perform comprehensive password strength analysis"""
        if not password:
            return {
                'score': 0, 'percentage': 0, 'strength': 'NONE',
                'color': '#e74c3c', 'feedback': [], 'recommendations': [],
                'analysis': {}, 'is_strong': False
            }
        
        analysis = {
            'length': len(password),
            'uppercase': bool(re.search(r'[A-Z]', password)),
            'lowercase': bool(re.search(r'[a-z]', password)),
            'digits': bool(re.search(r'\d', password)),
            'special': bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:,.<>?]', password)),
            'common_pattern': self.check_common_patterns(password),
            'repeated_chars': bool(re.search(r'(.)\1{2,}', password)),
            'sequential': self.check_sequential(password),
            'entropy': self.calculate_entropy(password)
        }
        
        score = 0
        feedback = []
        recommendations = []
        
        # Length check
        if analysis['length'] >= 16:
            score += 3
            feedback.append("✅ Excellent length (16+ characters)")
        elif analysis['length'] >= 12:
            score += 2
            feedback.append("✅ Good length (12-15 characters)")
        elif analysis['length'] >= 8:
            score += 1
            feedback.append("✅ Minimum length (8-11 characters)")
        else:
            feedback.append("❌ Too short (< 8 characters)")
            recommendations.append("Make it at least 12 characters long")
        
        # Character types
        char_types = [
            analysis['uppercase'], analysis['lowercase'],
            analysis['digits'], analysis['special']
        ]
        score += sum(char_types)
        
        for check, msg in [
            (analysis['uppercase'], "Contains uppercase letters"),
            (analysis['lowercase'], "Contains lowercase letters"),
            (analysis['digits'], "Contains numbers"),
            (analysis['special'], "Contains special characters")
        ]:
            if check:
                feedback.append(f"✅ {msg}")
            else:
                feedback.append(f"❌ Missing {msg}")
                recommendations.append(f"Add {msg.split(' ')[-1]}")
        
        # Pattern checks
        if analysis['common_pattern']:
            score -= 1
            feedback.append("⚠️ Contains common password patterns")
            recommendations.append("Avoid common passwords")
        if analysis['repeated_chars']:
            score -= 0.5
            feedback.append("⚠️ Has repeated characters")
            recommendations.append("Avoid repeated characters")
        if analysis['sequential']:
            score -= 0.5
            feedback.append("⚠️ Contains sequential characters")
            recommendations.append("Avoid sequential characters")
        
        max_score = 8
        percentage = max(0, min(100, (score / max_score) * 100))
        
        if percentage >= 80:
            strength = "EXCELLENT"
            color = '#2ecc71'
        elif percentage >= 60:
            strength = "GOOD"
            color = '#f39c12'
        elif percentage >= 40:
            strength = "WEAK"
            color = '#e67e22'
        else:
            strength = "VERY WEAK"
            color = '#e74c3c'
        
        return {
            'score': round(score, 1),
            'percentage': round(percentage, 1),
            'strength': strength,
            'color': color,
            'feedback': feedback,
            'recommendations': recommendations,
            'analysis': analysis,
            'is_strong': percentage >= 60
        }
    
    def check_common_patterns(self, password):
        """Check if password contains common patterns"""
        password_lower = password.lower()
        for pattern in self.common_patterns:
            if pattern in password_lower:
                return True
        return False
    
    def check_sequential(self, password):
        """Check for sequential characters"""
        password_lower = password.lower()
        for pattern in self.sequential_patterns:
            if pattern in password_lower:
                return True
        return False
    
    def calculate_entropy(self, password):
        """Calculate password entropy in bits"""
        if not password:
            return 0
        charset_size = len(set(password))
        return len(password) * math.log2(charset_size)