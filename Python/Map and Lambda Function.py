cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers 
    if n == 0:
        return [] 
    prev1, prev2 = 0, 1
    for i in range(n):
        yield prev1
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr  
