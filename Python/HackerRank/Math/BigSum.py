import math
import sys
input_str = sys.stdin.read()

numbers = list(map(int, input_str.split('\n')))
values = 0

for index in list(range(0, len(numbers), 2)):
    values += numbers[index]**numbers[index+1]
    
print(values)
