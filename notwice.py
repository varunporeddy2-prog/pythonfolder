# Remove Duplicates
nums = [1,2,3,3,5,2,5,5,5,6,6,6,3,4,3,4,5,6,6,7,8,8,8,8]
unique = list(set(nums))
print(unique)
print("Length of original list:", len(nums))
print("Length of unique list:", len(unique))                    
if len(nums) == len(unique):
    print("No duplicates found")        
else:
    print("Duplicates found")




