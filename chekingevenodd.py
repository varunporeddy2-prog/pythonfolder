nums = [2, 5, 7, 8, 10, 11, 13, 14, 16,18,21,25,30]
even = len([n for n in nums if n % 2 == 0])
odd = len(nums) - even
print("Even:", even, "Odd:", odd)


nums = [2, 5, 7, 8, 10, 11, 13, 14, 16,18,21,25,30,32,33,34,35,36]

even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even, "Odd:", odd)

print("you got the even and odd count correctly!")

