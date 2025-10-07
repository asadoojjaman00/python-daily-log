# Write a function that returns the sum of all even numbers in a list
# Example input: [1,2,3,4] → Output: 6

def sum_even(numbers):
    result = 0
    for number in numbers:
        if number%2== 0:
            result += number
    return result
    
numbers_list = [23, 54, 623, 23, 12, 64, 70, 4, 8]
print(f"the sum of all even numbers in a list : {sum_even(numbers_list)}")

