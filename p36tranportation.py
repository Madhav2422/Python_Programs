distance=int(input("Enter your distance "))

if distance <3:
    tr="Walk"
elif distance>=3 and distance<=15:
    tr="Bike"
else:
    tr="Car"

print("Mode of Transportation is ",tr)