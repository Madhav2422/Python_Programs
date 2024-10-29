from importlib.resources import is_resource

items=["bread","butter","jam","fruits"]

print(items)
print(items[0])

            # Lists are mutable -means we can change it

items[1]="cheese"
print(items)

                # List slicing
print(items[0:2])
print(items[-1])

                # Insert an item in the last -append
items.append("butter")
print(items)

                # Insert an item at any location
items.insert(1,"pasta")
print(items)

             # Join two lists
food=['bread','butter','bhel']
bathroom=['shampoo','soap']
print(food+bathroom)

             # We cannot add list+string
# food+"soda"

            # Print length of the items
print(len(items))

             # To check whether the item is in list-We use "in" method
print("bread" in items)

