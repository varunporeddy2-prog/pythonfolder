d={"name":"Alice","age":30,"city":"New York"}
print(d["name"])  # Output: Alice
d["age"]=31 # Update age                    
print(d)
d["profession"]="Engineer" # Add new key-value pair    
print(d)
del d["city"] # Remove key-value pair   
print(d)
print(d.keys())  # Output: dict_keys(['name', 'age', 'profession'])
print(d.values())  # Output: dict_values(['Alice', 31, 'Engineer'])
print(d.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('profession', 'Engineer')])
for key in d:
    print(key, ":", d[key])     
for key, value in d.items():
    print(key, "->", value)         
d2={"name":"Bob","age":25,"city":"Los Angeles"}
d.update(d2) # Merge d2 into d
print(d)    
