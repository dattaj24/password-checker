# password-checker# 🔐 CyberSec Password Auditor

A Python-based **password security analysis tool** that evaluates the strength and vulnerability of passwords using entropy, common password detection, and heuristic scoring.

---

## 🚀 Features

* ✅ Detects weak passwords based on:

  * Length
  * Character diversity (lowercase, uppercase, numbers, symbols)
* 📂 Checks against a **common leaked password dataset**
* 📊 Calculates **entropy (password randomness)**
* ⏱ Estimates **crack time**
* ⚠️ Generates a **hackability score**
* 🧠 Provides detailed **weakness analysis**

---

## 🛠️ Technologies Used

* Python 3
* `re` (Regex)
* `math`
* `os`

---

## 📁 Project Structure

```
password-auditor/
│
├── password_auditor.py
├── rockyou-75.txt   # Common password dataset
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/password-auditor.git
cd password-auditor
```

2. Make sure Python is installed:

```bash
python --version
```

---

## ▶️ Usage

Run the script:

```bash
python password_auditor.py
```

Enter a password when prompted:

```
Enter password to audit: MyPassword123!
```

---

## 📊 Example Output

```
========================================
      🔐 PASSWORD SECURITY REPORT
========================================
Password Entered : MyPassword123!
Hackability      : 35%
Strength         : 65%
Entropy          : 78.5 bits
Crack Time       : 120 years
Risk Level       : 🟢 SECURE

No major weaknesses detected 💪
========================================
```

---

## 🧠 How It Works

### 1. Entropy Calculation

* Uses character set size and password length:

```
Entropy = Length × log2(Character Set Size)
```

### 2. Crack Time Estimation

* Assumes attacker speed = **1 billion guesses/sec**

### 3. Hackability Score

* Based on:

  * Missing character types
  * Short length
  * Low entropy
  * Presence in leaked password database

---

## ⚠️ Dataset Requirement

You must provide a common password file (e.g., `rockyou.txt`).

Update this path in the script:

```python
COMMON_PASSWORD_FILE = "path/to/your/password_list.txt"
```

---

## 🔒 Security Note

This tool is for:

* ✅ Educational purposes
* ✅ Security awareness
* ✅ Personal password strength testing

❌ Do NOT use it for unauthorized activities.

---

## 📌 Future Improvements

* GUI interface (Tkinter / Web app)
* Integration with APIs (HaveIBeenPwned)
* Password suggestions generator
* Hash-based password checking

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, open an issue first.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Datta J**

---

⭐ If you found this useful, consider giving it a star!
