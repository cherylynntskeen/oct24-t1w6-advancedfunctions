#Higher-order functions
#Wrapper

numbers = [5, 7, 2, 3]

# builds a new list with the result of
# calling cb on each item in the list
def with_list(nums, cb):
    result = []
    for n in nums:
        result.append(cb(n))

    return result

def square(n):
    return n * n

def cube(n):
    return n ** 3

# Main 
print(with_list(numbers, cube))