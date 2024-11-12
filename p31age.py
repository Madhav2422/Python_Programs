age=int(input("Enter your age"))

if(age>0 and age<13):
    print("You are Child")
elif(age>=13 and age<=19):
    print("You are teenager")
elif(age>=20 and age<=59):
    print("You are Adult")
elif(age>=60):
    print("You are Senior")
else:
    print("Plz enter a valid age")