# Obsidian Penetration Testing Templates

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/)

**Automated penetration testing engagement management for Obsidian.**

Create complete, structured pentest engagement folders with pre-populated templates in seconds. Designed for security professionals conducting FedRAMP, HIPAA, PCI-DSS, and other compliance-driven assessments.

---

## ✨ Features

- **🚀 One-Click Generation** - Create entire engagement structures with a single button
- **🔍 Auto-Detection** - Automatically finds your Obsidian vaults
- **📋 Form-Based Input** - Clean GUI with dropdowns and date pickers
- **🏷️ Smart Tagging** - Auto-generates tags based on engagement type and phases
- **📊 Dataview Integration** - Dynamic progress tracking and findings summaries
- **🔧 Flexible** - Choose phases: External, Internal, Web App testing
- **🌐 Cross-Platform** - Windows, macOS, and Linux support
- **🎯 FedRAMP Focused** - Includes NIST 800-53 control mappings

---

## 📸 Screenshots

![GUI Screenshot](docs/screenshots/gui-screenshot.png)
*Simple form-based interface*

![Generated Structure](docs/screenshots/folder-structure.png)
*Complete folder structure created automatically*

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+** with tkinter
- **Obsidian** with these plugins (optional but recommended):
  - [Templater](https://github.com/SilentVoid13/Templater)
  - [Dataview](https://github.com/blacksmithgu/obsidian-dataview)

### Installation

#### Option 1: Download Release (Easiest)

1. Download the [latest release](https://github.com/yourusername/obsidian-pentest-templates/releases)
2. Extract to a folder
3. Run the launcher:
   - **Windows:** Double-click `launch_generator.bat`
   - **Mac/Linux:** `./launch_generator.sh`

#### Option 2: Clone Repository

```bash
git clone https://github.com/yourusername/obsidian-pentest-templates.git
cd obsidian-pentest-templates

# Install templates
python scripts/install_templates.py

# Run generator
python scripts/engagement_generator.py
```

###  First Run

1. **Launch the generator**
2. **Fill in the form:**
   - Engagement Name: `2026_ClientName`
   - Client Name: Your client
   - Engagement Type: Select from dropdown
   - Dates: Use date pickers
   - Select testing phases
3. **Verify paths** (auto-detected)
4. **Click "Generate Engagement"**
5. **Open Obsidian** - Your engagement is ready!

---

## 📁 What Gets Created

```
2026_ClientName/
├── _Attachments/                     # Screenshots and evidence
├── 00_Engagement_Overview.md         # Master dashboard with Dataview queries
├── 01_External/
│   ├── _Attachments/
│   └── 2026_ClientName_External.md   # External testing checklist
├── 02_Internal/
│   ├── _Attachments/
│   └── 2026_ClientName_Internal.md   # Internal testing + AD + K8s
├── 02_WebApp/
│   ├── _Attachments/
│   └── 2026_ClientName_WebApp.md     # OWASP Top 10 + API testing
└── 03_Findings/                       # Individual findings go here
```

All files are pre-populated with your engagement details!

---

## 📋 Template Features

### Status Tracking
Each test item includes status indicators:
- 🔵 Not Started
- 🟡 In Progress
- 🟢 Complete
- 🔴 Blocked

### Evidence Sections
Pre-formatted areas for:
- Screenshots with auto-naming
- Command outputs
- Timestamps
- Notes and observations

### NIST 800-53 Mappings
Every test section maps to relevant controls:
- AC (Access Control)
- IA (Identification & Authentication)
- SC (System & Communications Protection)
- SI (System & Information Integrity)
- And more...

### Dynamic Queries
Dataview queries automatically track:
- Testing progress by phase
- Findings by severity
- Completion statistics
- Open vs. closed findings

---

## 🛠️ Usage

### Method 1: Python GUI (Recommended)

**Best for:** Most users, cross-platform, no Obsidian plugins needed

```bash
# Windows
launch_generator.bat

# Mac/Linux
python3 scripts/engagement_generator.py
```

### Method 2: QuickAdd Plugin (Advanced)

**Best for:** Power users who want in-Obsidian automation

1. Install QuickAdd plugin
2. Copy `scripts/create-engagement.js` to `Scripts/` in your vault
3. Configure macro in QuickAdd settings
4. Use `Ctrl+P` → "New Pentest Engagement"

See [docs/QUICKADD_SETUP.md](docs/QUICKADD_SETUP.md) for detailed instructions.

---

## 🎯 Workflow

### Planning Phase
1. Generate engagement using GUI or QuickAdd
2. Open `00_Engagement_Overview.md`
3. Update scope, timeline, and contacts
4. Review testing phases

### Execution Phase
1. Work through each phase checklist
2. Check off items as completed
3. Paste screenshots (auto-saves to `_Attachments/`)
4. Create findings using `TPL_Finding.md` template

### Reporting Phase
1. Review Dataview dashboards for completion
2. Export findings summaries
3. Use as reference for formal report

---

## 🏷️ Auto-Generated Tags

Tags are automatically created based on your selections:

```yaml
tags: [fedramp, acme-corp, 2026, external, internal, webapp]
```

Includes:
- Engagement type
- Client name (sanitized)
- Year
- Selected phases

---

## 🔧 Configuration

### Changing Default Paths

Edit `scripts/engagement_generator.py`:

```python
# Line ~80
self.default_base = Path.home() / "Documents" / "MyVault" / "Engagements"
```

### Adding Custom Engagement Types

Edit the values tuple:

```python
# Line ~115
self.engagement_type['values'] = ('FedRAMP', 'HIPAA', 'Your-Custom-Type')
```

### Customizing Templates

Templates are in `templates/` directory. Edit them to match your methodology:

- `TPL_External_Pentest.md` - External testing
- `TPL_Internal_Pentest.md` - Internal testing + containers
- `TPL_WebApp_Pentest.md` - Web app + API testing
- `TPL_Finding.md` - Individual findings
- `TPL_Engagement_Overview.md` - Master dashboard

---

## 📚 Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [QuickAdd Setup](docs/QUICKADD_SETUP.md)
- [Template Customization](docs/CUSTOMIZATION.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Contributing](CONTRIBUTING.md)

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
git clone https://github.com/yourusername/obsidian-pentest-templates.git
cd obsidian-pentest-templates

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

---

## 🐛 Bug Reports & Feature Requests

Please use the [issue tracker](https://github.com/yourusername/obsidian-pentest-templates/issues) for bugs and features.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Obsidian community for excellent plugins
- Security professionals who provided feedback
- Contributors to this project

---

## 🔒 Security Note

These templates are for **professional penetration testing only**. Always ensure you have proper authorization before conducting security assessments.

---

## 📊 Statistics

- **Templates:** 5 comprehensive checklists
- **Test Items:** 50+ security checks
- **NIST Controls:** 20+ mapped controls
- **Phases:** External, Internal, WebApp, Container/K8s

---

## ⭐ Show Your Support

If you find this project useful, please consider:
- ⭐ Starring this repository
- 🐛 Reporting bugs
- 💡 Suggesting features
- 🤝 Contributing improvements

---

**Made with ❤️ for the security community**
