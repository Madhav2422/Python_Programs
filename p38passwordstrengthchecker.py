password=input("Enter your password")
password_length=len(password)

if password_length<6:
    strength="Weak"
elif password_length>=6 and password_length<15:
    strength="Medium"
else:
    strength="Hard"

print("Your password is ",strength)

