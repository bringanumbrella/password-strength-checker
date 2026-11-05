
def check_password(password):
    score = 0
    feedback = []
   
    common_passwords = [
        "password",
        "password123",
        "qwerty123",
        "admin123",
        "letmein"
    ]
    if password.lower() in common_passwords:
        score -= 2
        feedback.append("Avoid common passwords. Choose something less predictable.")
  

    if len(set(password)) == 1:
        feedback.append("Do not use the same character repeatedly.")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number.")

    if any(not char.isalnum() for char in password):
        score += 1
    else:
        feedback.append("Add a special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


password = input("Enter a password to test: ")

strength, feedback = check_password(password)

print("\nPassword strength:", strength)

if feedback:
    print("Suggestions:")
    for suggestion in feedback:
        print("-", suggestion)
else:
    print("Your password meets all basic requirements!")