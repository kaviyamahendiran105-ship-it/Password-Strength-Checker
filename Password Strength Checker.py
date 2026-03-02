# Password Strength Checker with Change Option (No Class)

rules = (
    "Minimum 8 characters",
    "At least one uppercase letter",
    "At least one lowercase letter",
    "At least one digit",
    "At least one special character"
)

special_chars = set("!@#$%^&*()_+-=[]{}|;:',.<>?/")

print("Password Rules:")
for rule in rules:
    print("-", rule)

while True:
    password = input("\nEnter your password: ")

    password_chars = list(password)
    conditions = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "digit": False,
        "special": False
    }

    if len(password) >= 8:
        conditions["length"] = True

    for ch in password_chars:
        if ch.isupper():
            conditions["uppercase"] = True
        elif ch.islower():
            conditions["lowercase"] = True
        elif ch.isdigit():
            conditions["digit"] = True
        elif ch in special_chars:
            conditions["special"] = True

    score = 0
    for value in conditions.values():
        if value:
            score += 1

    if score <= 2:
        strength = "POOR"
    elif score <= 4:
        strength = "GOOD"
    else:
        strength = "EXCELLENT"

    print("\nPassword Strength:", strength)

    if strength == "EXCELLENT":
        print("Password accepted successfully!")
        break
    else:
        print("Please change your password to make it stronger.")
