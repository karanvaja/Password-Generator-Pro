"""
Memorable Tab - Generate memorable but secure passwords
"""

import tkinter as tk
from tkinter import ttk, messagebox
from core.password_generator import PasswordGenerator
from utils.constants import WORD_LISTS

class MemorableTab:
    """Memorable password generation tab"""
    
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.generator = PasswordGenerator()
        
        # Create tab
        self.tab = tk.Frame(parent, bg='#1a1a2e')
        parent.add(self.tab, text='🧠 Memorable')
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create tab widgets"""
        info_label = tk.Label(
            self.tab,
            text="🎯 Create passwords that are easy to remember but hard to crack",
            font=('Arial', 12),
            bg='#1a1a2e',
            fg='#e0e0e0'
        )
        info_label.pack(pady=10)
        
        # Options
        options_frame = tk.LabelFrame(
            self.tab,
            text="Memorable Password Options",
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff',
            padx=20,
            pady=20
        )
        options_frame.pack(fill='x', padx=20, pady=10)
        
        # Number of words
        tk.Label(
            options_frame,
            text="Number of Words:",
            font=('Arial', 10),
            bg='#1a1a2e',
            fg='#e0e0e0'
        ).grid(row=0, column=0, sticky='w', pady=5)
        
        self.word_count = tk.IntVar(value=4)
        tk.Spinbox(
            options_frame,
            from_=3,
            to=8,
            textvariable=self.word_count,
            width=10,
            bg='#0f3460',
            fg='#e0e0e0',
            font=('Arial', 10)
        ).grid(row=0, column=1, sticky='w', pady=5, padx=10)
        
        # Separator
        tk.Label(
            options_frame,
            text="Separator:",
            font=('Arial', 10),
            bg='#1a1a2e',
            fg='#e0e0e0'
        ).grid(row=1, column=0, sticky='w', pady=5)
        
        self.separator_var = tk.StringVar(value='-')
        separators = ['-', '_', '.', '!', '?', '*', '+', '=']
        sep_menu = ttk.Combobox(
            options_frame,
            textvariable=self.separator_var,
            values=separators,
            width=10,
            state='readonly'
        )
        sep_menu.grid(row=1, column=1, sticky='w', pady=5, padx=10)
        
        # Word source
        tk.Label(
            options_frame,
            text="Word Source:",
            font=('Arial', 10),
            bg='#1a1a2e',
            fg='#e0e0e0'
        ).grid(row=2, column=0, sticky='w', pady=5)
        
        self.word_source = tk.StringVar(value='common')
        source_menu = ttk.Combobox(
            options_frame,
            textvariable=self.word_source,
            values=list(WORD_LISTS.keys()),
            width=15,
            state='readonly'
        )
        source_menu.grid(row=2, column=1, sticky='w', pady=5, padx=10)
        
        # Options
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)
        
        tk.Checkbutton(
            options_frame,
            text="Include Numbers",
            variable=self.include_numbers,
            bg='#1a1a2e',
            fg='#e0e0e0',
            selectcolor='#1a1a2e',
            font=('Arial', 10)
        ).grid(row=3, column=0, sticky='w', pady=5)
        
        tk.Checkbutton(
            options_frame,
            text="Include Special Chars",
            variable=self.include_special,
            bg='#1a1a2e',
            fg='#e0e0e0',
            selectcolor='#1a1a2e',
            font=('Arial', 10)
        ).grid(row=3, column=1, sticky='w', pady=5)
        
        # Generate button
        tk.Button(
            options_frame,
            text="🧠 Generate Memorable Password",
            command=self.generate_password,
            bg='#9b59b6',
            fg='white',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            cursor='hand2'
        ).grid(row=4, column=0, columnspan=2, pady=20)
        
        # Display
        display_frame = tk.LabelFrame(
            self.tab,
            text="Memorable Password",
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff',
            padx=10,
            pady=10
        )
        display_frame.pack(fill='x', padx=20, pady=10)
        
        self.password_display = tk.Entry(
            display_frame,
            font=('Courier', 16, 'bold'),
            bg='#0f3460',
            fg='#9b59b6',
            relief='solid',
            bd=2,
            readonlybackground='#0f3460'
        )
        self.password_display.pack(fill='x', padx=10, pady=10)
        
        # Action buttons
        action_frame = tk.Frame(display_frame, bg='#1a1a2e')
        action_frame.pack(pady=10)
        
        tk.Button(
            action_frame,
            text="📋 Copy",
            command=self.copy_to_clipboard,
            bg='#2ecc71',
            fg='#1a1a2e',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        tk.Button(
            action_frame,
            text="💾 Save",
            command=self.save_password,
            bg='#f39c12',
            fg='#1a1a2e',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
    
    def generate_password(self):
        """Generate memorable password"""
        password = self.generator.generate_memorable_password(
            word_count=self.word_count.get(),
            separator=self.separator_var.get(),
            include_numbers=self.include_numbers.get(),
            include_special=self.include_special.get(),
            word_source=self.word_source.get()
        )
        
        self.password_display.config(state='normal')
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)
        self.password_display.config(state='readonly')
        
        # Check strength
        self.app.tabs['checker'].check_password_strength(password)
    
    def save_password(self):
        """Save generated password"""
        password = self.password_display.get()
        if not password:
            messagebox.showwarning("Warning", "Generate a password first!")
            return
        
        self.app.switch_to_tab(4)
        self.app.tabs['manager'].save_password_entry.delete(0, tk.END)
        self.app.tabs['manager'].save_password_entry.insert(0, password)
        self.app.tabs['manager'].save_title_entry.focus()
    
    def copy_to_clipboard(self):
        """Copy password to clipboard"""
        password = self.password_display.get()
        if password:
            self.app.root.clipboard_clear()
            self.app.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")