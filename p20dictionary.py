# Dictinary-Key Pair values and order doesnt matter ,access values through keys

d={
  "madhav":7043070430,
  "sinu":9999999999,
    "sahil":7878787878
}
print(d)

# Accessing elements
print(d["sinu"])

# Add new elements
d["sam"]=7879097382
print(d)

# Delete from directory
del d["sam"]
print(d)

# Print all the directory values
for key in d:
    print("key:",key,"value:",d[key])

# Another way
for k,v in d.items():
    print("key",key,"value",v)

# Check if element is there or not in dictionary
print("tom"in d)

# Trash all the entries from the dictionary
print(d.clear())