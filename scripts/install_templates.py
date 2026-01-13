#!/usr/bin/env python3
"""
Template Installer for Obsidian Pentest Templates
Installs templates to your Obsidian vault's Engagements/z_Templates folder
"""

import sys
from pathlib import Path
import shutil

def detect_vaults():
    """Simple vault detection"""
    import json
    import platform
    
    system = platform.system()
    if system == "Windows":
        config_path = Path.home() / "AppData" / "Roaming" / "obsidian" / "obsidian.json"
    elif system == "Darwin":
        config_path = Path.home() / "Library" / "Application Support" / "obsidian" / "obsidian.json"
    elif system == "Linux":
        config_path = Path.home() / ".config" / "obsidian" / "obsidian.json"
    else:
        return []
    
    if not config_path.exists():
        return []
    
    try:
        with open(config_path) as f:
            config = json.load(f)
        
        vaults = []
        for vault_id, vault_info in config.get('vaults', {}).items():
            if 'path' in vault_info:
                vaults.append(Path(vault_info['path']))
        return vaults
    except:
        return []

def main():
    print("\n" + "="*50)
    print("  Obsidian Pentest Templates Installer")
    print("="*50 + "\n")
    
    # Find templates directory
    script_dir = Path(__file__).parent
    templates_dir = script_dir / "templates"
    
    if not templates_dir.exists():
        print("❌ Templates directory not found!")
        print(f"   Expected: {templates_dir}")
        return 1
    
    # Detect vaults
    vaults = detect_vaults()
    
    if vaults:
        print(f"✓ Detected {len(vaults)} Obsidian vault(s):\n")
        for i, vault in enumerate(vaults, 1):
            print(f"   {i}. {vault.name} ({vault})")
        print(f"   {len(vaults)+1}. Enter custom path")
        
        choice = input("\nSelect vault (1-{}): ".format(len(vaults)+1))
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(vaults):
                vault_path = vaults[choice-1]
            elif choice == len(vaults) + 1:
                vault_path = Path(input("Enter vault path: "))
            else:
                print("Invalid choice")
                return 1
        except:
            print("Invalid input")
            return 1
    else:
        print("ℹ No vaults auto-detected")
        vault_path = Path(input("Enter your Obsidian vault path: "))
    
    # Create destination
    dest_path = vault_path / "Engagements" / "z_Templates"
    dest_path.mkdir(parents=True, exist_ok=True)
    
    # Copy templates
    print(f"\n📋 Installing templates to: {dest_path}\n")
    
    for template in templates_dir.glob("TPL_*.md"):
        dest_file = dest_path / template.name
        shutil.copy2(template, dest_file)
        print(f"   ✓ {template.name}")
    
    print("\n✅ Installation complete!\n")
    print(f"Templates installed to: {dest_path}")
    print("\nNext steps:")
    print("1. Run the engagement generator: python scripts/engagement_generator.py")
    print("2. Or use launch_generator.bat (Windows) / launch_generator.sh (Mac/Linux)")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
