import math_ops

num1 = 5
num2 = 6

result_add = math_ops.add(num1, num2)
print(result_add)


result_subract = math_ops.subtract(num2, num1)
print(result_subract)

result_multiply = math_ops.multiply(num1, num2)
print(result_multiply)

result_divide = math_ops.divide(num1, num2)
print(result_divide)

print("----------")

# Another way to import

from math_ops import add, subtract, multiply, divide

result_add = add(num1, num2)
print(result_add)
print("********")
# Python's pre-defined modules
import math, random

num1 = math.pow(4,3)
print(num1)

num2 = math.sqrt(64)
print(num2)

randValue = random.randrange(1, 10)
print (randValue)