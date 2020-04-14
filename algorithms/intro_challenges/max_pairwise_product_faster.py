'''
Good job! (Max time used: 0.10/5.00, max memory used: 29892608/536870912.)
'''

# Uses python3
n = int(input())
input_list = [int(x) for x in input().split()]
assert(len(input_list) == n)

largest = max(input_list)
input_list.remove(largest)
second_largest = max(input_list)

print(largest*second_largest)
