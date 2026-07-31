"""
Constants - Word lists and patterns used throughout the application
"""

# Word lists for memorable password generation
WORD_LISTS = {
    'common': [
        'apple', 'tiger', 'ocean', 'mountain', 'forest', 'river', 'cloud',
        'star', 'moon', 'sun', 'fire', 'water', 'wind', 'earth', 'sky',
        'dream', 'hope', 'love', 'peace', 'joy', 'light', 'shadow',
        'crystal', 'thunder', 'silver', 'golden', 'emerald', 'ruby',
        'dragon', 'phoenix', 'wolf', 'eagle', 'lion', 'tiger',
        'garden', 'valley', 'desert', 'island', 'canyon', 'glacier'
    ],
    'random': [
        'xylophone', 'quantum', 'nebula', 'serendipity', 'ephemeral',
        'luminescence', 'ethereal', 'cascade', 'resonance', 'synergy',
        'vortex', 'zenith', 'aurora', 'cosmos', 'infinity', 'paradox',
        'nostalgia', 'serenade', 'melody', 'harmony', 'eclipse'
    ],
    'tech': [
        'python', 'java', 'ruby', 'rust', 'go', 'swift', 'kotlin',
        'docker', 'kubernetes', 'aws', 'azure', 'linux', 'unix',
        'binary', 'hex', 'byte', 'cache', 'array', 'stack', 'queue',
        'algorithm', 'database', 'network', 'security', 'crypto'
    ],
    'nature': [
        'forest', 'ocean', 'mountain', 'river', 'cloud', 'star',
        'flower', 'tree', 'stone', 'wave', 'flame', 'frost',
        'thunder', 'lightning', 'rainbow', 'sunset', 'dawn', 'dusk',
        'crystal', 'mineral', 'opal', 'sapphire', 'topaz'
    ]
}

# Common weak password patterns
COMMON_PATTERNS = [
    'password', '123456', 'qwerty', 'admin', 'letmein', 'welcome',
    'monkey', 'dragon', 'master', 'hello', 'freedom', 'whatever',
    'abc123', '123abc', 'qwerty123', 'password123', 'admin123'
]

# Sequential patterns
SEQUENTIAL_PATTERNS = [
    '012', '123', '234', '345', '456', '567', '678', '789', '890',
    'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk',
    'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst',
    'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz'
]

# Categories for password organization
CATEGORIES = [
    'Work', 'Personal', 'Social', 'Banking', 'Email',
    'Gaming', 'Shopping', 'Entertainment', 'Education', 'Other'
]

# Password strength colors
STRENGTH_COLORS = {
    'EXCELLENT': '#2ecc71',
    'GOOD': '#f39c12',
    'WEAK': '#e67e22',
    'VERY WEAK': '#e74c3c'
}

# Default settings
DEFAULT_SETTINGS = {
    'password_length': 16,
    'word_count': 4,
    'separator': '-',
    'include_numbers': True,
    'include_special': True,
    'word_source': 'common'
}