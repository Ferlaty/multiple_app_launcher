# Multiple App Launcher

![Version](https://img.shields.io/badge/version-1.4.0-blue)
![Python](https://img.shields.io/badge/python-3.9+-green)
![Size](https://img.shields.io/badge/size-<30MB-orange)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey)
![License](https://img.shields.io/badge/license-Apache_2.0-red)

A powerful yet simple utility to launch a suite of applications with a single click. Fully customizable via a user-friendly GUI.

<p align="center">
  <img width="1104" alt="Launcher Preview" src="https://github.com/user-attachments/assets/65b6c7c7-4939-4b04-bc94-347616f865d6">
</p>

🔗 **Official Website:** [ferlaty.pages.dev/multiple_app_launcher](https://ferlaty.pages.dev/multiple_app_launcher)

---

## 🔥 Highlights

- **Beginner-Friendly:** Simple interface designed for ease of use.
- **Lightweight:** Tiny footprint (under 30MB).
- **Custom Sequencing:** Launch up to 10 different apps with custom delays (default 5s).
- **Portable:** No installation required. Just copy, paste, and run.
- **Instance Support:** Run multiple independent configurations by placing the launcher in different directories.
- **Hybrid Interface:** Features both a console based launcher and a settings app with GUI.
- **Cross-platform compatibility:** Supports both Windows and Linux.

---

## ⚙️ Settings GUI
Configure your paths, delays, and commands without touching a single line of code.

<p align="center">
  <img width="400" alt="Settings GUI" src="https://github.com/user-attachments/assets/e9c8965c-a824-42c8-8ef6-6af70a3a7516">
</p>

---

## 🚀 Quick Start (No Python Required)

1. **Download:** Head to the [Releases](https://github.com/Ferlaty/multiple_app_launcher/releases) page and grab the latest version.
2. **Extract:** Unzip the archive to your preferred location.
3. **Run:** Execute `multiple_app_launcher.exe` on *Windows*, `multiple_app_launcher` on *Linux*.
4. **Optional (Shortcut, Windows only):** To access it from your Start Menu, paste a shortcut into:
   `C:\ProgramData\Microsoft\Windows\Start Menu\Programs`

---

## 🛠️ Installation from Source

### Prerequisites
* Python 3.9 or higher
---
### Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ferlaty/multiple_app_launcher.git
   cd multiple_app_launcher
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run compile the settings app**
   ```bash
   python compile.py
   ```
   *Select `settings` and hit enter.*

4. **Move the executable to the main folder**
   ```bash
   cd dist
   ```
   *Windows*
    ```bash
    move settings.exe ..
    ```
   *Linux*
    ```bash
    mv settings ..
    ```

5. **Run the Application:**
   ```bash
   python MultipleAppLauncher.py
   ```  
---
### Pro tip
* You can edit the settings file file manually by clicking `Open config file in text editor` in the settings app.


2026 Ferlaty