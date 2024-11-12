stu_marks=int(input("Enter your score"))

if(stu_marks>=90 and stu_marks <= 100):
    print("You got the A grade")
elif(stu_marks>=80 and stu_marks <=89):
    print("You got B grade ")
elif(stu_marks>=70 and stu_marks<=79):
    print("You got the C grade ")
elif(stu_marks>=60 and stu_marks<=69):
    print("You got the D grade ")
elif(stu_marks>0 and stu_marks<60):
    print("You got the F grade ")
else:
    print("You got the negative marks")