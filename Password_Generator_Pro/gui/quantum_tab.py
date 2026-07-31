"""
Quantum Tab - Quantum-secure password generation
"""

import tkinter as tk
from tkinter import ttk, messagebox
from core.password_generator import PasswordGenerator

class QuantumTab:
    """Quantum-resistant password generation tab"""
    
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.generator = PasswordGenerator()
        
        # Create tab
        self.tab = tk.Frame(parent, bg='#1a1a2e')
        parent.add(self.tab, text='⚛️ Quantum-Secure')
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create tab widgets"""
        info_label = tk.Label(
            self.tab,
            text="🔬 Quantum-resistant passwords using entropy from multiple sources",
            font=('Arial', 12),
            bg='#1a1a2e',
            fg='#e0e0e0'
        )
        info_label.pack(pady=10)
        
        # Options frame
        options_frame = tk.LabelFrame(
            self.tab,
            text="Quantum Generation Options",
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff',
            padx=20,
            pady=20
        )
        options_frame.pack(fill='x', padx=20, pady=10)
        
        # Length
        tk.Label(
            options_frame,
            text="Password Length:",
            font=('Arial', 10),
            bg='#1a1a2e',
            fg='#e0e0e0'
        ).grid(row=0, column=0, sticky='w', pady=5)
        
        self.length_var = tk.IntVar(value=32)
        tk.Spinbox(
            options_frame,
            from_=16,
            to=128,
            textvariable=self.length_var,
            width=10,
            bg='#0f3460',
            fg='#e0e0e0',
            font=('Arial', 10)
        ).grid(row=0, column=1, sticky='w', pady=5, padx=10)
        
        # Entropy sources
        self.use_system = tk.BooleanVar(value=True)
        self.use_time = tk.BooleanVar(value=True)
        self.use_random = tk.BooleanVar(value=True)
        
        tk.Checkbutton(
            options_frame,
            text="System Entropy",
            variable=self.use_system,
            bg='#1a1a2e',
            fg='#e0e0e0',
            selectcolor='#1a1a2e',
            font=('Arial', 10)
        ).grid(row=1, column=0, sticky='w', pady=5)
        
        tk.Checkbutton(
            options_frame,
            text="Time-based Entropy",
            variable=self.use_time,
            bg='#1a1a2e',
            fg='#e0e0e0',
            selectcolor='#1a1a2e',
            font=('Arial', 10)
        ).grid(row=1, column=1, sticky='w', pady=5)
        
        tk.Checkbutton(
            options_frame,
            text="Random Entropy",
            variable=self.use_random,
            bg='#1a1a2e',
            fg='#e0e0e0',
            selectcolor='#1a1a2e',
            font=('Arial', 10)
        ).grid(row=2, column=0, sticky='w', pady=5)
        
        tk.Button(
            options_frame,
            text="🔐 Generate Quantum-Secure Password",
            command=self.generate_password,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            cursor='hand2'
        ).grid(row=3, column=0, columnspan=2, pady=20)
        
        # Display
        display_frame = tk.LabelFrame(
            self.tab,
            text="Quantum Password",
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
            fg='#e74c3c',
            relief='solid',
            bd=2,
            readonlybackground='#0f3460'
        )
        self.password_display.pack(fill='x', padx=10, pady=10)
        
        # Entropy display
        self.entropy_label = tk.Label(
            display_frame,
            text="Entropy: Not calculated",
            font=('Arial', 10),
            bg='#1a1a2e',
            fg='#e0e0e0'
        )
        self.entropy_label.pack()
        
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
        """Generate quantum-secure password"""
        length = self.length_var.get()
        
        # Get selected entropy sources
        entropy_sources = []
        if self.use_system.get():
            entropy_sources.append('system')
        if self.use_time.get():
            entropy_sources.append('time')
        if self.use_random.get():
            entropy_sources.append('random')
        
        if not entropy_sources:
            entropy_sources = ['system', 'time']
        
        # Generate password
        password = self.generator.generate_quantum_password(length, entropy_sources)
        
        # Display
        self.password_display.config(state='normal')
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)
        self.password_display.config(state='readonly')
        
        # Calculate entropy
        entropy = self.generator.calculate_entropy(password)
        self.entropy_label.config(text=f"Entropy: {entropy:.2f} bits")
        
        # Check strength in checker tab
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