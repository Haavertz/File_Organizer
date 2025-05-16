# 📁 File Organizer

A simple and efficient desktop application to organize your files by extension or type, built with Python and PySide6.

![image](https://github.com/user-attachments/assets/eb394cdd-9dbb-4d11-b0ae-fb1afca0bc77)

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
