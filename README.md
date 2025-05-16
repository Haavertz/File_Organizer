# 📁 File Organizer

A simple and efficient desktop application to organize your files by extension or type, built with Python and PySide6.

---

## 🚀 Features

- 🗂️ Automatically categorizes files into folders (e.g. Images, Documents, Audio, etc.)
- 🔍 Detects files in selected directories
- 🎯 Clean and intuitive GUI built with PySide6 (Qt for Python)
- 📦 Lightweight executable (.exe) ready for Windows
- 💾 Supports drag-and-drop folder selection (optional, if implemented)

---

## 🖥️ Technologies

- **Python 3.8+**
- **PySide6 (Qt for Python)**
- **PyInstaller** for packaging

---

## 📦 Installation | Modification

Clone this repository:

```bash
git clone https://github.com/Haavertz/File_Organizer.git
cd File_Organizer
```

Create a virtual environment (only if you want)
```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```
Run the application:

```bash
python main.py
```
## 🏗️ Building the .exe (Windows):

```bash
pyinstaller --noconfirm --onefile --windowed --icon=icon2.ico main.py
```
