"""
Launcher Script - Run this to start the application
Fixes import issues by setting up the Python path correctly
"""

import sys
import os

# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

print(f"📁 Project Directory: {current_dir}")
print(f"🐍 Python Path: {sys.path[0]}")
print("\n🚀 Starting Password Generator Pro...\n")

if __name__ == "__main__":
    try:
        # Try importing and running the application
        from gui.main_window import PasswordManagerApp
        app = PasswordManagerApp()
        app.run()
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("\n📁 Please make sure you have the correct project structure:")
        print("""
        Password_Generator_Pro/
        ├── launcher.py      ← You are here
        ├── main.py
        ├── core/
        │   ├── __init__.py
        │   ├── encryption.py
        │   ├── password_generator.py
        │   ├── password_checker.py
        │   └── password_manager.py
        ├── gui/
        │   ├── __init__.py
        │   ├── main_window.py
        │   ├── cupp_tab.py
        │   ├── quantum_tab.py
        │   ├── memorable_tab.py
        │   ├── checker_tab.py
        │   └── manager_tab.py
        └── utils/
            ├── __init__.py
            ├── constants.py
            ├── validators.py
            └── helpers.py
        """)
        input("\nPress Enter to exit...")
    except Exception as e:
        print(f"❌ Application Error: {e}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")