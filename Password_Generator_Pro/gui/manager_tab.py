"""
Manager Tab - Password management with encryption
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Use absolute imports
from core.password_manager import PasswordManager
from core.password_generator import PasswordGenerator
from utils.helpers import mask_password
from utils.constants import CATEGORIES

class ManagerTab:
    """Password management tab"""
    
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.manager = PasswordManager()
        self.generator = PasswordGenerator()
        
        # Create tab
        self.tab = tk.Frame(parent, bg='#1a1a2e')
        parent.add(self.tab, text='💾 Manager')
        
        self.create_widgets()
        self.display_passwords()
    
    def create_widgets(self):
        """Create tab widgets"""
        # Add password frame
        add_frame = tk.LabelFrame(
            self.tab,
            text="Add New Password",
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff',
            padx=10,
            pady=10
        )
        add_frame.pack(fill='x', padx=20, pady=10)
        
        # Title
        tk.Label(
            add_frame,
            text="Title:",
            font=('Arial', 10),
            bg='#1a1a2e',
            fg='#e0e0e0'
        ).grid(row=0, column=0, sticky='e', padx=5, pady=5)
        
        self.save_title_entry = tk.Entry(
            add_frame,
            font=('Arial', 10),
            bg='#0f3460',
            fg='#e0e0e0',
            insertbackground='#e0e0e0',
            width=40
        )
        self.save_title_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Password
        tk.Label(
            add_frame,
            text="Password:",
            font=('Arial', 10),
            bg='#1a1a2e',
            fg='#e0e0e0'
        ).grid(row=1, column=0, sticky='e', padx=5, pady=5)
        
        self.save_password_entry = tk.Entry(
            add_frame,
            font=('Arial', 10),
            bg='#0f3460',
            fg='#e0e0e0',
            insertbackground='#e0e0e0',
            width=40,
            show='*'
        )
        self.save_password_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Category
        tk.Label(
            add_frame,
            text="Category:",
            font=('Arial', 10),
            bg='#1a1a2e',
            fg='#e0e0e0'
        ).grid(row=2, column=0, sticky='e', padx=5, pady=5)
        
        self.save_category_var = tk.StringVar(value='Uncategorized')
        category_combo = ttk.Combobox(
            add_frame,
            textvariable=self.save_category_var,
            values=['Uncategorized'] + CATEGORIES,
            width=37,
            state='readonly'
        )
        category_combo.grid(row=2, column=1, padx=5, pady=5)
        
        # Note
        tk.Label(
            add_frame,
            text="Note:",
            font=('Arial', 10),
            bg='#1a1a2e',
            fg='#e0e0e0'
        ).grid(row=3, column=0, sticky='ne', padx=5, pady=5)
        
        self.save_note_text = tk.Text(
            add_frame,
            height=3,
            width=40,
            bg='#0f3460',
            fg='#e0e0e0',
            insertbackground='#e0e0e0',
            font=('Arial', 10)
        )
        self.save_note_text.grid(row=3, column=1, padx=5, pady=5)
        
        # Buttons
        btn_frame = tk.Frame(add_frame, bg='#1a1a2e')
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        tk.Button(
            btn_frame,
            text="💾 Save Password",
            command=self.save_password,
            bg='#2ecc71',
            fg='#1a1a2e',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        tk.Button(
            btn_frame,
            text="🔄 Generate",
            command=self.generate_for_manager,
            bg='#00d4ff',
            fg='#1a1a2e',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        tk.Button(
            btn_frame,
            text="🗑️ Clear Fields",
            command=self.clear_fields,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        # Search frame
        search_frame = tk.LabelFrame(
            self.tab,
            text="Search Passwords",
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff',
            padx=10,
            pady=10
        )
        search_frame.pack(fill='x', padx=20, pady=10)
        
        self.search_entry = tk.Entry(
            search_frame,
            font=('Arial', 10),
            bg='#0f3460',
            fg='#e0e0e0',
            insertbackground='#e0e0e0',
            width=40
        )
        self.search_entry.pack(side='left', padx=5, fill='x', expand=True)
        
        tk.Button(
            search_frame,
            text="🔍 Search",
            command=self.search_passwords,
            bg='#3498db',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        tk.Button(
            search_frame,
            text="🔄 Show All",
            command=self.display_passwords,
            bg='#95a5a6',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        # Password list
        list_frame = tk.LabelFrame(
            self.tab,
            text="Saved Passwords",
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff',
            padx=10,
            pady=10
        )
        list_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Treeview
        columns = ('Title', 'Password', 'Category', 'Date')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=8)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Action buttons
        action_frame = tk.Frame(list_frame, bg='#1a1a2e')
        action_frame.pack(pady=10)
        
        tk.Button(
            action_frame,
            text="📋 Copy Password",
            command=self.copy_selected,
            bg='#3498db',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        tk.Button(
            action_frame,
            text="👁️ Show Password",
            command=self.show_selected,
            bg='#9b59b6',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        tk.Button(
            action_frame,
            text="🗑️ Delete",
            command=self.delete_selected,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        tk.Button(
            action_frame,
            text="📤 Export",
            command=self.export_passwords,
            bg='#f39c12',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        tk.Button(
            action_frame,
            text="📥 Import",
            command=self.import_passwords,
            bg='#2ecc71',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=5,
            cursor='hand2'
        ).pack(side='left', padx=5)
        
        # Statistics
        stats_frame = tk.LabelFrame(
            self.tab,
            text="Statistics",
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff',
            padx=10,
            pady=10
        )
        stats_frame.pack(fill='x', padx=20, pady=10)
        
        self.stats_label = tk.Label(
            stats_frame,
            text="",
            font=('Arial', 10),
            bg='#1a1a2e',
            fg='#e0e0e0'
        )
        self.stats_label.pack()
        
        self.update_stats()
    
    def save_password(self):
        """Save password"""
        title = self.save_title_entry.get().strip()
        password = self.save_password_entry.get().strip()
        category = self.save_category_var.get()
        note = self.save_note_text.get(1.0, tk.END).strip()
        
        if not title or not password:
            messagebox.showwarning("Warning", "Title and password are required!")
            return
        
        # Save
        success, msg = self.manager.add_password(title, password, category, note)
        
        if success:
            messagebox.showinfo("Success", msg)
            self.clear_fields()
            self.display_passwords()
            self.update_stats()
        else:
            messagebox.showwarning("Warning", msg)
    
    def generate_for_manager(self):
        """Generate password for manager"""
        password = self.generator.generate_quantum_password(length=16)
        self.save_password_entry.delete(0, tk.END)
        self.save_password_entry.insert(0, password)
    
    def display_passwords(self):
        """Display all passwords"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for title, data in self.manager.get_all_passwords().items():
            password = data['password']
            masked = mask_password(password)
            self.tree.insert('', 'end', values=(
                title,
                masked,
                data.get('category', 'Uncategorized'),
                data['date']
            ))
    
    def search_passwords(self):
        """Search passwords"""
        query = self.search_entry.get().strip()
        
        if not query:
            self.display_passwords()
            return
        
        results = self.manager.search(query)
        
        # Clear tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Display results
        for title, data in results.items():
            password = data['password']
            masked = mask_password(password)
            self.tree.insert('', 'end', values=(
                title,
                masked,
                data.get('category', 'Uncategorized'),
                data['date']
            ))
    
    def copy_selected(self):
        """Copy selected password"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a password entry!")
            return
        
        item = self.tree.item(selection[0])
        title = item['values'][0]
        
        data = self.manager.get_password(title)
        if data:
            self.app.root.clipboard_clear()
            self.app.root.clipboard_append(data['password'])
            messagebox.showinfo("Success", f"Password for '{title}' copied to clipboard!")
    
    def show_selected(self):
        """Show selected password"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a password entry!")
            return
        
        item = self.tree.item(selection[0])
        title = item['values'][0]
        
        data = self.manager.get_password(title)
        if data:
            messagebox.showinfo(f"Password: {title}", 
                               f"Password: {data['password']}\n\n"
                               f"Category: {data.get('category', 'Uncategorized')}\n"
                               f"Date: {data['date']}")
    
    def delete_selected(self):
        """Delete selected password"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a password entry to delete!")
            return
        
        item = self.tree.item(selection[0])
        title = item['values'][0]
        
        if messagebox.askyesno("Confirm Delete", f"Delete password for '{title}'?"):
            success, msg = self.manager.delete_password(title)
            if success:
                messagebox.showinfo("Success", msg)
                self.display_passwords()
                self.update_stats()
            else:
                messagebox.showerror("Error", msg)
    
    def clear_fields(self):
        """Clear form fields"""
        self.save_title_entry.delete(0, tk.END)
        self.save_password_entry.delete(0, tk.END)
        self.save_category_var.set('Uncategorized')
        self.save_note_text.delete(1.0, tk.END)
    
    def export_passwords(self):
        """Export passwords"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".enc",
            filetypes=[("Encrypted files", "*.enc"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                self.manager.export_passwords(filename)
                messagebox.showinfo("Success", "Passwords exported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Export failed: {str(e)}")
    
    def import_passwords(self):
        """Import passwords"""
        filename = filedialog.askopenfilename(
            filetypes=[("Encrypted files", "*.enc"), ("All files", "*.*")]
        )
        
        if filename:
            merge = messagebox.askyesno("Import Options", 
                                       "Do you want to merge with existing passwords?\n"
                                       "Click 'No' to replace all existing passwords.")
            
            try:
                success, msg = self.manager.import_passwords(filename, merge)
                if success:
                    messagebox.showinfo("Success", msg)
                    self.display_passwords()
                    self.update_stats()
                else:
                    messagebox.showwarning("Warning", msg)
            except Exception as e:
                messagebox.showerror("Error", f"Import failed: {str(e)}")
    
    def update_stats(self):
        """Update statistics"""
        stats = self.manager.get_stats()
        
        stats_text = f"Total Passwords: {stats['total']} | Categories: {stats['categories']}"
        
        # Add category breakdown
        if stats['by_category']:
            stats_text += "\n📂 Categories: "
            for category, count in stats['by_category'].items():
                stats_text += f"{category}: {count} "
        
        self.stats_label.config(text=stats_text)