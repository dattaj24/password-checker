import re
import math
import os

# ===== CONFIG =====
COMMON_PASSWORD_FILE = r"C:\Users\datta\OneDrive\Desktop\data analytics project\Data\rockyou-75.txt"


# ===== LOAD COMMON PASSWORDS =====
def load_common_password(file_path):
    if not os.path.exists(file_path):
        print(f"[ERROR] File not found: {file_path}")
        return set()

    print("[INFO] Loading password database...")
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            passwords = set(f.read().splitlines())
        print(f"[INFO] Loaded {len(passwords)} common passwords\n")
        return passwords
    except Exception as e:
        print(f"[ERROR] Failed to load file: {e}")
        return set()


# ===== ENTROPY CALCULATION =====
def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[!@#$%^&*]', password): charset += 10

    if charset == 0:
        return 0

    return len(password) * math.log2(charset)


# ===== CRACK TIME ESTIMATION =====
def estimate_crack_time(entropy):
    guesses_per_second = 1e9  # 1 billion guesses/sec
    seconds = 2 ** entropy / guesses_per_second

    if seconds < 1:
        return "Instantly cracked ⚠️"
    elif seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds/60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds/3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds/86400)} days"
    else:
        return f"{int(seconds/31536000)} years"


# ===== MAIN AUDIT FUNCTION =====
def password_audit(password, common_passwords):
    hack_score = 0
    issues = []

    # Length
    if len(password) < 8:
        hack_score += 30
        issues.append("Too short (<8 characters)")

    # Character checks
    if not re.search(r'[a-z]', password):
        hack_score += 10
        issues.append("Missing lowercase")

    if not re.search(r'[A-Z]', password):
        hack_score += 10
        issues.append("Missing uppercase")

    if not re.search(r'\d', password):
        hack_score += 10
        issues.append("Missing numbers")

    if not re.search(r'[!@#$%^&*]', password):
        hack_score += 10
        issues.append("Missing special characters")

    # Common password check
    if password in common_passwords:
        hack_score = 95
        issues.append("Password found in leaked database (CRITICAL)")

    # Entropy
    entropy = calculate_entropy(password)

    if entropy < 28:
        hack_score += 20
    elif entropy < 50:
        hack_score += 10

    hack_score = min(hack_score, 100)
    strength = 100 - hack_score
    crack_time = estimate_crack_time(entropy)

    return hack_score, strength, entropy, crack_time, issues


# ===== UI OUTPUT =====
def print_report(password, hack, strength, entropy, crack_time, issues):
    print("\n" + "="*40)
    print("      🔐 PASSWORD SECURITY REPORT")
    print("="*40)

    print(f"Password Entered : {password}")
    print(f"Hackability      : {hack}%")
    print(f"Strength         : {strength}%")
    print(f"Entropy          : {round(entropy,2)} bits")
    print(f"Crack Time       : {crack_time}")

    # Risk Level
    if hack > 80:
        print("Risk Level       : 🔴 HIGHLY VULNERABLE")
    elif hack > 50:
        print("Risk Level       : 🟠 MODERATE RISK")
    else:
        print("Risk Level       : 🟢 SECURE")

    # Issues
    if issues:
        print("\nWeak Points:")
        for i in issues:
            print(f" - {i}")
    else:
        print("\nNo major weaknesses detected 💪")

    print("="*40)


# ===== MAIN =====
def main():
    print("=== CYBERSEC PASSWORD AUDITOR ===\n")

    common_passwords = load_common_password(COMMON_PASSWORD_FILE)

    password = input("Enter password to audit: ")

    hack, strength, entropy, crack_time, issues = password_audit(password, common_passwords)

    print_report(password, hack, strength, entropy, crack_time, issues)

if __name__ == "__main__":
    main()