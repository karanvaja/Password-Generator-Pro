"""
Main Window - The main application window with tabs
"""

import tkinter as tk
from tkinter import ttk

# Use absolute imports instead of relative imports
from gui.cupp_tab import CUPPTab
from gui.quantum_tab import QuantumTab
from gui.memorable_tab import MemorableTab
from gui.checker_tab import CheckerTab
from gui.manager_tab import ManagerTab

class PasswordManagerApp:
    """Main application window"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🔐 Password Generator Pro")
        self.root.geometry("1100x800")
        self.root.configure(bg='#1a1a2e')
        
        # Set minimum window size
        self.root.minsize(900, 700)
        
        # Initialize tabs dictionary FIRST
        self.tabs = {}
        
        # Setup style and GUI
        self.setup_style()
        self.create_widgets()
    
    def setup_style(self):
        """Setup dark theme style"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        bg_color = '#1a1a2e'
        fg_color = '#e0e0e0'
        accent_color = '#00d4ff'
        
        style.configure('TNotebook', 
                       background=bg_color, 
                       borderwidth=0)
        style.configure('TNotebook.Tab', 
                       background='#16213e',
                       foreground=fg_color,
                       padding=[20, 10],
                       font=('Arial', 11, 'bold'))
        style.map('TNotebook.Tab', 
                 background=[('selected', '#0f3460')],
                 foreground=[('selected', accent_color)])
        
        style.configure('TFrame', background=bg_color)
        style.configure('TLabel', background=bg_color, foreground=fg_color)
        style.configure('TLabelframe', background=bg_color, foreground=accent_color)
        style.configure('TLabelframe.Label', background=bg_color, foreground=accent_color)
        
        # Progressbar style
        style.configure('TProgressbar', 
                       thickness=20,
                       background=accent_color,
                       troughcolor='#0f3460')
    
    def create_widgets(self):
        """Create main application widgets"""
        # Main container
        main_container = tk.Frame(self.root, bg='#1a1a2e')
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title with hacker style
        title_frame = tk.Frame(main_container, bg='#1a1a2e')
        title_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(
            title_frame,
            text="⚡ V.K  PASSWORD GENERATOR PRO + ⚡",
            font=('Courier', 24, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff'
        )
        title_label.pack()
        
        subtitle = tk.Label(
            title_frame,
            text="🛡️ Military-Grade Password Security |  Develop By Vaja Karan ",
            font=('Arial', 15, 'bold'),
            bg='#1a1a2e',
            fg="#045ec5"
        )
        subtitle.pack()
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill='both', expand=True)
        
        # Create tabs and store references
        self.tabs['cupp'] = CUPPTab(self.notebook, self)
        self.tabs['quantum'] = QuantumTab(self.notebook, self)
        self.tabs['memorable'] = MemorableTab(self.notebook, self)
        self.tabs['checker'] = CheckerTab(self.notebook, self)
        self.tabs['manager'] = ManagerTab(self.notebook, self)
    
    def run(self):
        """Run the application"""
        self.root.mainloop()
    
    def switch_to_tab(self, tab_index):
        """Switch to a specific tab by index"""
        self.notebook.select(tab_index)
    
    def get_notebook(self):
        """Get the notebook widget"""
        return self.notebook