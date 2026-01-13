#!/usr/bin/env python3
"""
Obsidian Pentest Engagement Generator
Creates a complete folder structure and populated templates for penetration testing engagements

Author: https://github.com/yourusername/obsidian-pentest-templates
License: MIT
"""

import os
import sys
import json
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from pathlib import Path
import shutil
import platform

class ObsidianVaultDetector:
    """Detects Obsidian vaults from the Obsidian configuration file"""
    
    @staticmethod
    def get_config_path():
        """Get the Obsidian config path based on OS"""
        system = platform.system()
        
        if system == "Windows":
            return Path.home() / "AppData" / "Roaming" / "obsidian" / "obsidian.json"
        elif system == "Darwin":  # macOS
            return Path.home() / "Library" / "Application Support" / "obsidian" / "obsidian.json"
        elif system == "Linux":
            return Path.home() / ".config" / "obsidian" / "obsidian.json"
        else:
            return None
    
    @staticmethod
    def detect_vaults():
        """Detect all Obsidian vaults from config file"""
        config_path = ObsidianVaultDetector.get_config_path()
        
        if not config_path or not config_path.exists():
            return []
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            vaults = []
            if 'vaults' in config:
                for vault_id, vault_info in config['vaults'].items():
                    if 'path' in vault_info:
                        vault_path = Path(vault_info['path'])
                        if vault_path.exists():
                            vaults.append({
                                'name': vault_path.name,
                                'path': vault_path
                            })
            
            return vaults
        except Exception as e:
            print(f"Error detecting vaults: {e}")
            return []

class EngagementGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Pentest Engagement Generator")
        self.root.geometry("650x750")
        self.root.resizable(False, False)
        
        # Detect Obsidian vaults
        self.detected_vaults = ObsidianVaultDetector.detect_vaults()
        
        # Default paths
        self.default_base = None
        self.default_templates = None
        
        if self.detected_vaults:
            # Use first detected vault as default
            first_vault = self.detected_vaults[0]['path']
            self.default_base = first_vault / "Engagements"
            self.default_templates = first_vault / "Engagements" / "z_Templates"
        else:
            # Fallback to Documents
            self.default_base = Path.home() / "Documents" / "Obsidian" / "Engagements"
            self.default_templates = self.default_base / "z_Templates"
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title = ttk.Label(main_frame, text="Create New Pentest Engagement", 
                         font=('Arial', 16, 'bold'))
        title.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Vault selection (if detected)
        if self.detected_vaults:
            vault_info = ttk.Label(main_frame, 
                                  text=f"✓ Detected {len(self.detected_vaults)} Obsidian vault(s)", 
                                  foreground="green")
            vault_info.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        row = 2
        
        # Engagement Name
        ttk.Label(main_frame, text="Engagement Name:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.engagement_name = ttk.Entry(main_frame, width=40)
        self.engagement_name.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5)
        self.engagement_name.insert(0, f"{datetime.now().year}_")
        row += 1
        
        # Client Name
        ttk.Label(main_frame, text="Client Name:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.client_name = ttk.Entry(main_frame, width=40)
        self.client_name.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5)
        row += 1
        
        # Engagement Type
        ttk.Label(main_frame, text="Engagement Type:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.engagement_type = ttk.Combobox(main_frame, width=37, state='readonly')
        self.engagement_type['values'] = ('FedRAMP', 'HIPAA', 'PCI-DSS', 'SOC 2', 'ISO 27001', 'General', 'Custom')
        self.engagement_type.current(5)  # Default to "General"
        self.engagement_type.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5)
        row += 1
        
        # Start Date
        ttk.Label(main_frame, text="Start Date:").grid(row=row, column=0, sticky=tk.W, pady=5)
        date_frame = ttk.Frame(main_frame)
        date_frame.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5)
        
        self.start_year = ttk.Combobox(date_frame, width=6, state='readonly')
        self.start_year['values'] = [str(y) for y in range(2024, 2031)]
        self.start_year.set(str(datetime.now().year))
        self.start_year.pack(side=tk.LEFT, padx=(0, 5))
        
        self.start_month = ttk.Combobox(date_frame, width=4, state='readonly')
        self.start_month['values'] = [f"{m:02d}" for m in range(1, 13)]
        self.start_month.set(f"{datetime.now().month:02d}")
        self.start_month.pack(side=tk.LEFT, padx=(0, 5))
        
        self.start_day = ttk.Combobox(date_frame, width=4, state='readonly')
        self.start_day['values'] = [f"{d:02d}" for d in range(1, 32)]
        self.start_day.set(f"{datetime.now().day:02d}")
        self.start_day.pack(side=tk.LEFT)
        row += 1
        
        # End Date
        ttk.Label(main_frame, text="End Date:").grid(row=row, column=0, sticky=tk.W, pady=5)
        end_date_frame = ttk.Frame(main_frame)
        end_date_frame.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5)
        
        self.end_year = ttk.Combobox(end_date_frame, width=6, state='readonly')
        self.end_year['values'] = [str(y) for y in range(2024, 2031)]
        self.end_year.set(str(datetime.now().year))
        self.end_year.pack(side=tk.LEFT, padx=(0, 5))
        
        self.end_month = ttk.Combobox(end_date_frame, width=4, state='readonly')
        self.end_month['values'] = [f"{m:02d}" for m in range(1, 13)]
        self.end_month.set(f"{datetime.now().month:02d}")
        self.end_month.pack(side=tk.LEFT, padx=(0, 5))
        
        self.end_day = ttk.Combobox(end_date_frame, width=4, state='readonly')
        self.end_day['values'] = [f"{d:02d}" for d in range(1, 32)]
        self.end_day.set(f"{datetime.now().day:02d}")
        self.end_day.pack(side=tk.LEFT)
        row += 1
        
        # Assessor Name
        ttk.Label(main_frame, text="Lead Assessor:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.assessor = ttk.Entry(main_frame, width=40)
        self.assessor.insert(0, os.getenv('USER', os.getenv('USERNAME', 'Assessor')))
        self.assessor.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5)
        row += 1
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, 
                                                            sticky=(tk.W, tk.E), pady=20)
        row += 1
        
        # Testing Phases Section
        ttk.Label(main_frame, text="Testing Phases:", 
                 font=('Arial', 12, 'bold')).grid(row=row, column=0, columnspan=2, 
                                                   sticky=tk.W, pady=(0, 10))
        row += 1
        
        # Checkboxes for phases
        self.include_external = tk.BooleanVar(value=True)
        ttk.Checkbutton(main_frame, text="External Network Testing", 
                       variable=self.include_external).grid(row=row, column=0, columnspan=2, 
                                                             sticky=tk.W, pady=2)
        row += 1
        
        self.include_internal = tk.BooleanVar(value=True)
        ttk.Checkbutton(main_frame, text="Internal Network Testing", 
                       variable=self.include_internal).grid(row=row, column=0, columnspan=2, 
                                                             sticky=tk.W, pady=2)
        row += 1
        
        self.include_webapp = tk.BooleanVar(value=True)
        ttk.Checkbutton(main_frame, text="Web Application Testing", 
                       variable=self.include_webapp).grid(row=row, column=0, columnspan=2, 
                                                           sticky=tk.W, pady=2)
        row += 1
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, 
                                                            sticky=(tk.W, tk.E), pady=20)
        row += 1
        
        # Destination Path
        ttk.Label(main_frame, text="Destination Folder:", 
                 font=('Arial', 10, 'bold')).grid(row=row, column=0, columnspan=2, 
                                                   sticky=tk.W, pady=(0, 5))
        row += 1
        
        path_frame = ttk.Frame(main_frame)
        path_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.dest_path = ttk.Entry(path_frame, width=50)
        self.dest_path.insert(0, str(self.default_base))
        self.dest_path.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        ttk.Button(path_frame, text="Browse", command=self.browse_destination).pack(side=tk.LEFT, 
                                                                                      padx=(5, 0))
        row += 1
        
        # Templates Path
        ttk.Label(main_frame, text="Templates Folder:").grid(row=row, column=0, columnspan=2, 
                                                              sticky=tk.W, pady=(10, 5))
        row += 1
        
        template_frame = ttk.Frame(main_frame)
        template_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.template_path = ttk.Entry(template_frame, width=50)
        self.template_path.insert(0, str(self.default_templates))
        self.template_path.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        ttk.Button(template_frame, text="Browse", command=self.browse_templates).pack(side=tk.LEFT, 
                                                                                       padx=(5, 0))
        row += 1
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="", foreground="gray")
        self.status_label.grid(row=row, column=0, columnspan=2, pady=(10, 0))
        row += 1
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=row, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Generate Engagement", 
                  command=self.generate_engagement).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
    def browse_destination(self):
        folder = filedialog.askdirectory(title="Select Engagements Folder")
        if folder:
            self.dest_path.delete(0, tk.END)
            self.dest_path.insert(0, folder)
            
    def browse_templates(self):
        folder = filedialog.askdirectory(title="Select Templates Folder")
        if folder:
            self.template_path.delete(0, tk.END)
            self.template_path.insert(0, folder)
    
    def generate_engagement(self):
        # Validate inputs
        if not self.engagement_name.get().strip():
            messagebox.showerror("Error", "Please enter an engagement name")
            return
            
        if not self.client_name.get().strip():
            messagebox.showerror("Error", "Please enter a client name")
            return
            
        # Check if at least one phase is selected
        if not (self.include_external.get() or self.include_internal.get() or 
                self.include_webapp.get()):
            messagebox.showerror("Error", "Please select at least one testing phase")
            return
        
        # Create engagement data
        engagement_data = {
            'engagement_name': self.engagement_name.get().strip(),
            'client_name': self.client_name.get().strip(),
            'engagement_type': self.engagement_type.get(),
            'start_date': f"{self.start_year.get()}-{self.start_month.get()}-{self.start_day.get()}",
            'end_date': f"{self.end_year.get()}-{self.end_month.get()}-{self.end_day.get()}",
            'assessor': self.assessor.get().strip(),
            'phases': {
                'external': self.include_external.get(),
                'internal': self.include_internal.get(),
                'webapp': self.include_webapp.get()
            },
            'dest_path': Path(self.dest_path.get()),
            'template_path': Path(self.template_path.get())
        }
        
        # Generate tags
        tags = [
            engagement_data['engagement_type'].lower().replace(' ', '-'),
            engagement_data['client_name'].lower().replace(' ', '-'),
            engagement_data['start_date'].split('-')[0]  # year
        ]
        
        if engagement_data['phases']['external']:
            tags.append('external')
        if engagement_data['phases']['internal']:
            tags.append('internal')
        if engagement_data['phases']['webapp']:
            tags.append('webapp')
        
        engagement_data['tags'] = tags
        
        try:
            self.status_label.config(text="Creating engagement structure...", foreground="blue")
            self.root.update()
            
            self.create_engagement_structure(engagement_data)
            
            messagebox.showinfo("Success", 
                              f"Engagement '{engagement_data['engagement_name']}' created successfully!\n\n"
                              f"Location: {engagement_data['dest_path'] / engagement_data['engagement_name']}")
            self.root.quit()
        except FileNotFoundError as e:
            messagebox.showerror("Template Error", 
                               f"Template files not found!\n\n{str(e)}\n\n"
                               f"Please ensure templates are in:\n{engagement_data['template_path']}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create engagement:\n\n{str(e)}")
            self.status_label.config(text="Error occurred", foreground="red")
    
    def create_engagement_structure(self, data):
        """Create the complete folder structure and populate templates"""
        
        # Create base engagement folder
        engagement_folder = data['dest_path'] / data['engagement_name']
        
        if engagement_folder.exists():
            if not messagebox.askyesno("Folder Exists", 
                                       f"Folder '{data['engagement_name']}' already exists. Overwrite?"):
                return
            shutil.rmtree(engagement_folder)
        
        engagement_folder.mkdir(parents=True, exist_ok=True)
        
        # Create subfolders
        (engagement_folder / "_Attachments").mkdir(exist_ok=True)
        (engagement_folder / "03_Findings").mkdir(exist_ok=True)
        
        if data['phases']['external']:
            (engagement_folder / "01_External" / "_Attachments").mkdir(parents=True, exist_ok=True)
            
        if data['phases']['internal']:
            (engagement_folder / "02_Internal" / "_Attachments").mkdir(parents=True, exist_ok=True)
            
        if data['phases']['webapp']:
            (engagement_folder / "02_WebApp" / "_Attachments").mkdir(parents=True, exist_ok=True)
        
        # Create and populate Engagement Overview
        self.create_engagement_overview(engagement_folder, data)
        
        # Create phase-specific files
        if data['phases']['external']:
            self.create_phase_file(engagement_folder / "01_External", "External", data)
            
        if data['phases']['internal']:
            self.create_phase_file(engagement_folder / "02_Internal", "Internal", data)
            
        if data['phases']['webapp']:
            self.create_phase_file(engagement_folder / "02_WebApp", "WebApp", data)
    
    def create_engagement_overview(self, folder, data):
        """Create the engagement overview file"""
        template_file = data['template_path'] / "TPL_Engagement_Overview.md"
        output_file = folder / "00_Engagement_Overview.md"
        
        if not template_file.exists():
            raise FileNotFoundError(f"Template not found: {template_file}")
        
        with open(template_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace template variables
        tags_str = ', '.join(data['tags'])
        
        replacements = {
            '<%tp.file.title%>': data['engagement_name'],
            '<%tp.system.prompt("Client Name")%>': data['client_name'],
            '<%tp.system.suggester(["FedRAMP", "HIPAA", "PCI-DSS", "SOC 2", "ISO 27001", "General"], "Select Engagement Type")%>': data['engagement_type'],
            '<%tp.date.now("YYYY-MM-DD")%>': data['start_date'],
            '<%tp.system.prompt("Expected End Date (YYYY-MM-DD)")%>': data['end_date'],
            '<%tp.date.now("YYYY")%>': data['start_date'].split('-')[0],
            'tags: [engagement, <%tp.date.now("YYYY")%>]': f'tags: [{tags_str}]',
            'Engagements/<%tp.file.title%>': f'Engagements/{data["engagement_name"]}'
        }
        
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def create_phase_file(self, folder, phase_name, data):
        """Create phase-specific testing file"""
        template_file = data['template_path'] / f"TPL_{phase_name}_Pentest.md"
        output_file = folder / f"{data['engagement_name']}_{phase_name}.md"
        
        if not template_file.exists():
            raise FileNotFoundError(f"Template not found: {template_file}")
        
        with open(template_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace template variables
        tags_str = ', '.join(data['tags'])
        folder_relative = str(folder.relative_to(data['dest_path'])).replace('\\', '/')
        
        replacements = {
            '<%tp.file.folder(true).split(\'/\')[0]%>': data['engagement_name'],
            '<%tp.file.folder(true)%>': folder_relative,
            '<%tp.date.now("YYYY-MM-DD")%>': data['start_date'],
            '<%tp.date.now("YYYY")%>': data['start_date'].split('-')[0],
            f'tags: [pentest, fedramp, {phase_name.lower()}, <%tp.date.now("YYYY")%>]': f'tags: [{tags_str}]',
            '<%tp.system.prompt("Target Scope/IP Range")%>': '[Enter target scope]',
            '<%tp.system.prompt("Client/Project Name")%>': data['client_name'],
            '<%tp.system.prompt("Application Name")%>': '[Enter application name]',
            '<%tp.system.prompt("Target URL")%>': '[Enter target URL]',
            '<%tp.system.prompt("Low privilege username:password")%>': '[Enter low user credentials]',
            '<%tp.system.prompt("Admin username:password")%>': '[Enter admin credentials]'
        }
        
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    root = tk.Tk()
    app = EngagementGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
