import sys

# Gathered from: https://www.geeksforgeeks.org/python-sys-module/

# If you want to input and output to the console
# for line in sys.stdin:
#     if 'q' == line.rstrip():
#         break
#     print(f'Input: {line}')
# sys.stdout.write('I now quit')

# Total arguments
n = len(sys.argv)
print("Total arguments passed: ", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

#  Listing out all the paths
# print(sys.path)

# Removing the values
# sys.path = []

# importing pandas after removing sys.path values
import pandas

# print(sys.modules)

