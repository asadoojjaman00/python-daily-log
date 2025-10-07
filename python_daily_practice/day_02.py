# Problem 1: Fibonacci Sequence

def fibonacci_fun(num):
    if num <= 0:
        return []
    elif num <= 1:
        return [0]
    
    fibonacci = [0,1]
    for i in range(2,num):
        new_num = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(new_num)
    return fibonacci

print(f"Fibonacci Sequence : {fibonacci_fun(num = 10)}")