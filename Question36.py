from functools import reduce
import operator

def product_of_elements(lst):
    return reduce(operator.mul, lst, 1)

# Example usage
numbers = [1, 2, 3, 4, 5]
product = product_of_elements(numbers)
print(product)  # Output: 120
