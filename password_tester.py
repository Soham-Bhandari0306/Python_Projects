
import re

password = input("Enter your password: ")

score = 0


# Check minimum length
if len(password) >= 8:
    score += 1
else:
    print(" Password must be at least 8 characters long.")


# Check uppercase letter
if re.search(r"[A-Z]", password):
    score += 1
else:
    print(" Add at least one uppercase letter.")


# Check digit
if re.search(r"[0-9]", password):
    score += 1
else:
    print(" Add at least one number.")


# Check special character
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    print(" Add at least one special character.")


# Rating system
if score <= 1:
    print("Password Strength: Weak")
elif score <= 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
