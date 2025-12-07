
def password_strength(password):

    strength = 0

    # Check for uppercase letter
    for c in password:
        if c.isupper():
            strength += 1
            break

    # Check for lowercase letter
    for c in password:
        if c.islower():
            strength += 1
            break

    # Check for digit
    for c in password:
        if c.isdigit():
            strength += 1
            break
    
    # Check for special character
    special = "!@#$%&*(),_-+=[]{}|\\:;?'. "
    for c in password:
        if c in special:
            strength += 1
            break

    # Check length
    if len(password) >= 8:
        strength += 1

    return strength


def strength_label(score):
    if score <= 2:
        return "Weak Password"
    elif score == 3 or score == 4:
        return "Medium Strength"
    else:
        return "Strong Password"


password = input("Enter password: ")
score = password_strength(password)
label = strength_label(score)

print(f"Strength Score: {score}")
print(f"Strength Label: {label}")

