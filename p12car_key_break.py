key_location="chair"
locations=["garage","living room","chair","closet"]

for i in locations:
    if i==key_location:
        print("Key is found in ",i)
        break
    else:
        print("Key is not found ",i)

# Use break whenever we want to achieve the goal and then we have to stop it