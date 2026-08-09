# 📬 Mail Checker

A lightweight, script-based email checker written in Python. This utility allows you to verify and process email data from a file or service. Ideal for small-scale verification tasks or automation scenarios.

---

## 🧩 Features

- ✅ Easy to use: run from a batch file or directly via Python
- 📄 Configurable and extendable
- 📦 Simple dependency management
- 🔍 Terminal-based output

---

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ArviiSoft/mail-checker.git
   cd mail-checker
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:

   - On Windows:  
     Double-click `başlat.bat`

   - Or run via terminal:  
     ```bash
     python main.py
     ```

---

## 📋 Requirements

| Package     | Description                  |
|-------------|------------------------------|
| `dnspython`  | For DNS   |
| `python-whois` | For WHOIS  |


> All dependencies are listed in `requirements.txt`.

---

## ▶️ Usage

```bash
python main.py
```

Depending on the implementation in `main.py`, this script will:
- Load a list of emails
- Send validation requests (e.g., via API or regex)
- Print results with color-coded status

---

## 🔄 Flowchart

```text
+--------------+
|  başlat.bat  |
+------+-------+
       |
       v
+--------------+
|  main.py     |
+------+-------+
       |
       v
+--------------------+
| Email check logic  |
+------+-------------+
       |
       v
+------------------+
| Console output   |
+------------------+
```

---

## 📂 File Structure

```
Mail Checker/
├── başlat.bat
├── main.py
└── requirements.txt
```

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Developed by [ArviS](https://discord.gg/uzPUNrrhH2)  
Feel free to contribute or suggest improvements!
