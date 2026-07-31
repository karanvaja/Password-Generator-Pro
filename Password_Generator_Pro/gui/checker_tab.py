"""
Checker Tab - Advanced password strength checker
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from core.password_checker import PasswordChecker
from utils.helpers import mask_password

class CheckerTab:
    """Password strength checker tab"""
    
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.checker = PasswordChecker()
        
        # Create tab
        self.tab = tk.Frame(parent, bg='#1a1a2e')
        parent.add(self.tab, text='🛡️ Checker')
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create tab widgets"""
        # Input frame
        input_frame = tk.LabelFrame(
            self.tab,
            text="Enter Password to Check",
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff',
            padx=10,
            pady=10
        )
        input_frame.pack(fill='x', padx=20, pady=20)
        
        self.password_entry = tk.Entry(
            input_frame,
            font=('Courier', 14),
            show='*',
            bg='#0f3460',
            fg='#e0e0e0',
            insertbackground='#e0e0e0',
            relief='solid',
            bd=2
        )
        self.password_entry.pack(fill='x', padx=10, pady=10)
        
        # Show password
        self.show_password = tk.BooleanVar(value=False)
        tk.Checkbutton(
            input_frame,
            text="👁️ Show Password",
            variable=self.show_password,
            command=self.toggle_visibility,
            bg='#1a1a2e',
            fg='#e0e0e0',
            selectcolor='#1a1a2e',
            font=('Arial', 10)
        ).pack(pady=5)
        
        # Button frame
        btn_frame = tk.Frame(input_frame, bg='#1a1a2e')
        btn_frame.pack(pady=10)
        
        tk.Button(
            btn_frame,
            text="🔍 Analyze Password",
            command=self.check_password,
            bg='#00d4ff',
            fg='#1a1a2e',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        tk.Button(
            btn_frame,
            text="🔄 Clear",
            command=self.clear_results,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        # Results frame
        results_frame = tk.LabelFrame(
            self.tab,
            text="Analysis Results",
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff',
            padx=10,
            pady=10
        )
        results_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Strength meter
        self.strength_meter = ttk.Progressbar(
            results_frame,
            length=400,
            mode='determinate',
            style='TProgressbar'
        )
        self.strength_meter.pack(pady=10)
        
        # Strength label
        self.strength_label = tk.Label(
            results_frame,
            text="Enter a password to check its strength",
            font=('Arial', 14, 'bold'),
            bg='#1a1a2e',
            fg='#e0e0e0'
        )
        self.strength_label.pack(pady=10)
        
        # Password display (masked)
        self.password_display = tk.Label(
            results_frame,
            text="",
            font=('Courier', 10),
            bg='#1a1a2e',
            fg='#7f8c8d'
        )
        self.password_display.pack(pady=5)
        
        # Detailed analysis
        self.detailed_analysis = scrolledtext.ScrolledText(
            results_frame,
            height=8,
            font=('Courier', 10),
            bg='#0f3460',
            fg='#e0e0e0',
            relief='solid',
            bd=1
        )
        self.detailed_analysis.pack(fill='both', expand=True, padx=10, pady=10)
    
    def check_password(self):
        """Check password strength"""
        password = self.password_entry.get()
        
        if not password:
            messagebox.showwarning("Warning", "Please enter a password to check!")
            return
        
        self.check_password_strength(password)
    
    def check_password_strength(self, password):
        """Check password strength and display results"""
        if not password:
            return
        
        # Get analysis results
        results = self.checker.check_strength(password)
        
        # Update strength meter
        self.strength_meter['value'] = results['percentage']
        
        # Update strength label
        self.strength_label.config(
            text=f"Strength: {results['strength']} ({results['score']}/8)",
            fg=results['color']
        )
        
        # Show masked password
        self.password_display.config(text=f"Password: {mask_password(password)}")
        
        # Update detailed analysis
        self.detailed_analysis.delete(1.0, tk.END)
        self.detailed_analysis.insert(1.0, "📊 DETAILED ANALYSIS:\n")
        self.detailed_analysis.insert(tk.END, "-" * 40 + "\n\n")
        
        # Analysis details
        analysis = results['analysis']
        self.detailed_analysis.insert(tk.END, f"Length: {analysis['length']} characters\n")
        self.detailed_analysis.insert(tk.END, f"Entropy: {analysis['entropy']:.2f} bits\n")
        self.detailed_analysis.insert(tk.END, f"Contains Uppercase: {'✅' if analysis['uppercase'] else '❌'}\n")
        self.detailed_analysis.insert(tk.END, f"Contains Lowercase: {'✅' if analysis['lowercase'] else '❌'}\n")
        self.detailed_analysis.insert(tk.END, f"Contains Digits: {'✅' if analysis['digits'] else '❌'}\n")
        self.detailed_analysis.insert(tk.END, f"Contains Special: {'✅' if analysis['special'] else '❌'}\n")
        self.detailed_analysis.insert(tk.END, f"Common Pattern: {'⚠️' if analysis['common_pattern'] else '✅'}\n")
        self.detailed_analysis.insert(tk.END, f"Repeated Chars: {'⚠️' if analysis['repeated_chars'] else '✅'}\n")
        self.detailed_analysis.insert(tk.END, f"Sequential: {'⚠️' if analysis['sequential'] else '✅'}\n\n")
        
        # Feedback
        self.detailed_analysis.insert(tk.END, "📝 FEEDBACK:\n")
        for feedback in results['feedback']:
            self.detailed_analysis.insert(tk.END, f"  {feedback}\n")
        
        # Recommendations
        if results['recommendations']:
            self.detailed_analysis.insert(tk.END, "\n💡 RECOMMENDATIONS:\n")
            for rec in results['recommendations']:
                self.detailed_analysis.insert(tk.END, f"  • {rec}\n")
    
    def toggle_visibility(self):
        """Toggle password visibility"""
        if self.show_password.get():
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')
    
    def clear_results(self):
        """Clear all results"""
        self.password_entry.delete(0, tk.END)
        self.strength_meter['value'] = 0
        self.strength_label.config(text="Enter a password to check its strength", fg='#e0e0e0')
        self.password_display.config(text="")
        self.detailed_analysis.delete(1.0, tk.END)
        self.show_password.set(False)
        self.password_entry.config(show='*')