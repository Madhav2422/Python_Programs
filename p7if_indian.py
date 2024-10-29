indian=["samosa","idli","dosa"]
chinese=["bhel","egg role","pot sticker"]
italian=["pizza","pasta","risotto"]

dish=input("Enter a dish name :")

if dish in indian:
     print("Indian")
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print("Italian")
else:
    print("I dont know which is your cusine")
