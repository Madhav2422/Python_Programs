exp=[2000,3000,4000,5000,6000]
total=0

for i in range(len(exp)):
    print("Month:", (i + 1), "Expenses:", exp[i])
    total=total+exp[i]

print("Total expense is :",total)
