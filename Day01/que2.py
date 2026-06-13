import random as rd

numbers = [rd.randint(1,6) for _ in range(5)]
print(numbers)
print(" ")

#Slicing 
sliced_numbers = numbers[1:6]
print(f"Sliced numbers : {sliced_numbers}")
print(" ")

#Reverse the list 
print(f"Reversed List : {numbers[::-1]}")
print(" ")
# Find the maximum and minimum values in the list
print(f"Maximum Values in the list : {max(numbers)}")
print(f"Minimum Values in the list : {min(numbers)}")
print(" ")
# Even numbered squares 
print(f"Even numbered squares : {[x**2 for x in numbers if x % 2 == 0]}")
print(" ")



