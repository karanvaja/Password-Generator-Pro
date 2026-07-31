Password Strength Checker

Real-time scoring (0–8 points)

Entropy calculation in bits
Pattern detection:
Common passwords (e.g., "password123")
Sequential characters (e.g., "abc", "123")
Repeated characters (e.g., "aaa")
Character type analysis (uppercase, lowercase, digits, special)
Detailed feedback and actionable recommendations
Visual strength meter with color coding

💾 Password Manager

Encrypted storage using cryptography.Fernet (AES-128-CBC)
Organize passwords by category (Work, Personal, Banking, etc.)
Search functionality (title or note)
Import/Export encrypted password files
Clipboard copy with one click
Statistics dashboard (total passwords, category breakdown)

📸 Screenshots

Add screenshots here after running the application
CUPP Profile Tab	Quantum-Secure Tab
Generate from personal info	Generate with multi-source entropy
Memorable Tab	Checker Tab
Human-friendly passwords	Strength analysis with feedback
Manager Tab	
Encrypted password storage	
🛠️ Installation
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Step 1: Clone the Repository
bash
git clone https://github.com/yourusername/password-generator-pro.git
cd password-generator-pro

Step 2: Install Dependencies
bash
pip install -r requirements.txt

Step 3: Run the Application
bash
python launcher.py
Or directly:

bash
python main.py

🎮 Usage
Quick Start Guide
Generate a Password

Go to any generation tab (CUPP, Quantum, or Memorable)
Configure options (length, word count, etc.)
Click the "Generate" button
Check Password Strength
Switch to the Checker tab
Enter or paste a password
View detailed analysis and recommendations
Save a Password
Go to the Manager tab
Fill in title, password, category, and note
Click "Save Password"

Your password is encrypted and stored locally
Manage Existing Passwords
View all saved passwords in the tree view
Search by title or note
Copy, show, or delete entries
Export/import encrypted .enc files

