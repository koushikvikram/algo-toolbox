# Naive algorithm
n = int(input())
input_list = [int(x) for x in input().split()]
assert(n == input_list)

product = 0

for i in range(0, n):
    for j in range(i+1, n):
        if i != j:  # prevent multiplying element by itself
            product = max(product, input_list[i]*input_list[j])

print(product)