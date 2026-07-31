"""
CUPP Tab - Profile-based password generation
Inspired by Kali Linux CUPP (Common User Password Profiler)
"""

import tkinter as tk
from tkinter import ttk, messagebox
from core.password_generator import PasswordGenerator

class CUPPTab:
    """CUPP-style password generation tab"""
    
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.generator = PasswordGenerator()
        
        # Create tab
        self.tab = tk.Frame(parent, bg='#1a1a2e')
        parent.add(self.tab, text='👤 CUPP Profile')
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create tab widgets"""
        # Instructions
        info_label = tk.Label(
            self.tab,
            text="📋 Enter personal information to generate personalized secure passwords",
            font=('Arial', 12),
            bg='#1a1a2e',
            fg='#e0e0e0'
        )
        info_label.pack(pady=10)
        
        # Profile input frame
        profile_frame = tk.LabelFrame(
            self.tab,
            text="Personal Information",
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff',
            padx=20,
            pady=20
        )
        profile_frame.pack(fill='x', padx=20, pady=10)
        
        # Input fields
        fields = [
            ('First Name:', 'first_name'),
            ('Last Name:', 'last_name'),
            ('Nickname:', 'nickname'),
            ('Birth Year:', 'birth_year'),
            ('Pet Name:', 'pet_name'),
            ('Favorite Color:', 'favorite_color'),
            ('Favorite Food:', 'favorite_food'),
            ('Phone Number:', 'phone'),
            ('Email:', 'email')
        ]
        
        self.profile_vars = {}
        for i, (label, key) in enumerate(fields):
            tk.Label(
                profile_frame,
                text=label,
                font=('Arial', 10),
                bg='#1a1a2e',
                fg='#e0e0e0'
            ).grid(row=i, column=0, sticky='e', padx=5, pady=5)
            
            var = tk.StringVar()
            entry = tk.Entry(
                profile_frame,
                textvariable=var,
                font=('Arial', 10),
                bg='#0f3460',
                fg='#e0e0e0',
                insertbackground='#e0e0e0',
                relief='solid',
                bd=1,
                width=35
            )
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.profile_vars[key] = var
        
        # Generate button
        btn_frame = tk.Frame(profile_frame, bg='#1a1a2e')
        btn_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)
        
        tk.Button(
            btn_frame,
            text="🎯 Generate Profile-Based Password",
            command=self.generate_password,
            bg='#00d4ff',
            fg='#1a1a2e',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            cursor='hand2'
        ).pack()
        
        # Result frame
        result_frame = tk.LabelFrame(
            self.tab,
            text="Generated Password",
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff',
            padx=10,
            pady=10
        )
        result_frame.pack(fill='x', padx=20, pady=10)
        
        self.password_display = tk.Entry(
            result_frame,
            font=('Courier', 16, 'bold'),
            bg='#0f3460',
            fg='#00d4ff',
            relief='solid',
            bd=2,
            readonlybackground='#0f3460'
        )
        self.password_display.pack(fill='x', padx=10, pady=10)
        
        # Action buttons
        action_frame = tk.Frame(result_frame, bg='#1a1a2e')
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
        """Generate password from profile data"""
        # Collect profile data
        profile_data = {}
        for key, var in self.profile_vars.items():
            value = var.get().strip()
            if value:
                profile_data[key] = value
        
        if not profile_data:
            messagebox.showwarning("Warning", "Please fill at least one field!")
            return
        
        # Generate password
        password = self.generator.generate_cupp_password(profile_data)
        
        # Display password
        self.password_display.config(state='normal')
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)
        self.password_display.config(state='readonly')
        
        # Check strength in checker tab
        self.app.tabs['checker'].check_password_strength(password)
    
    def save_password(self):
        """Save generated password"""
        password = self.password_display.get()
        if not password:
            messagebox.showwarning("Warning", "Generate a password first!")
            return
        
        # Switch to manager tab
        self.app.switch_to_tab(4)
        
        # Fill password field
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