'''
Max time used: 0.16/5.00, max memory used: 29863936/536870912
'''

# Uses python3
n = int(input())
input_list = [int(x) for x in input().split()]

assert(len(input_list) == n)

# Alternate method - sort in descending order and print product of first two elements
input_list.sort(reverse=True)

print(input_list[0]*input_list[1])
