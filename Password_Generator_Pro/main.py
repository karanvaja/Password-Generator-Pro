"""
Password Generator Pro - Main Application Entry Point
A comprehensive password management system with Kali Linux-style features
"""

import sys
import os

# Add the current directory to Python path FIRST
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

def main():
    """Main application entry point"""
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║         🔐 PASSWORD GENERATOR PRO - KALI STYLE           ║
    ║                                                          ║
    ║  ⚡ Military-Grade Password Security                     ║
    ║  🔑 CUPP Profile-Based Generation                        ║
    ║  ⚛️ Quantum-Resistant Passwords                          ║
    ║  🧠 Memorable Passwords                                 ║
    ║  🛡️ Advanced Strength Checker                           ║
    ║  💾 Encrypted Password Manager                          ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    try:
        # Import the main window from GUI
        from gui.main_window import PasswordManagerApp
        app = PasswordManagerApp()
        app.run()
    except ImportError as e:
        print(f"\n❌ Import Error: {e}")
        print("\n📁 Please make sure you have the correct project structure:")
        print("""
        Password_Generator_Pro/
        
        ├── core/
        │   ├── __init__.py
        │   ├── encryption.py
        │   ├── password_checker.py
        │   ├── password_generator.py
        │   └── password_manager.py
        ├── gui/
        │   ├── __init__.py
        │   ├── checker_tab.py
        │   ├── cupp_tab.py
        │   ├── main_window.py
        │   ├── manager_tab.py
        │   ├── memorable_tab.py
        │   ├── quantum_tab.py
        │ 
        └── utils/
        │    ├── __init__.py
        │    ├── constants.py
        │    └── helpers.py
        │    ├── validators.py
        │ 
        ├── main.py



        """)
        print("\n💡 Try running: python -m main")
        sys.exit(1)
    except AttributeError as e:
        print(f"\n❌ Attribute Error: {e}")
        print("\n💡 Make sure 'self.tabs = {}' is initialized before creating widgets")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Application Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()