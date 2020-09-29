"""
Algorithms to compute Fibonacci numbers
"""

input_number = 20

# Naive algorithm


def fib_recurs(n):
    """
    recursively calculate the n-th fibonacci number
    """
    if n <= 1:
        return n
    else:
        return fib_recurs(n-2)+fib_recurs(n-1)


print("fib_recurs({}): {}".format(input_number, fib_recurs(input_number)))

# measuring lines of code i.e. T(n) executed by fib_recurs(n)
# T(n) = 2                     if n <= 1        i.e if case, return statement
#      = 3 + T(n-2) + T(n-1)   else             i.e. if, else, return + T(fib_recurs(n-2)) + T(fib_recurs(n-1))
# this looks more or less like the formula for Fibonacci numbers
# from this, you can easily show that T(n) >= F(n)
# T(100) = 1.77 * 10^21 ----> Takes 56,000 years on 1 GHz CPU


# why is this algorithm so slow?
#   - huge tree of recursive calls where most calls are repeated


# -----------------------------------------------------------------------------------------------------------------------------------------------


# Efficient Algorithm - imitate hand computation

def fib_list(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-2] + fib[i-1])
    return fib[n]


print("fib_list({}): {}".format(input_number, fib_list(input_number)))


# T(n) = 2 + 2n    i.e list assignment + return + (append + addition)*n in the loop


# -----------------------------------------------------------------------------------------------------------------------------------------------


# Fibonacci last digit

def fib_last_digit(n):
    if n<=1:
        return n
    previous, current = 0, 1
    for _ in range(2, n+1):
        previous, current = current, (previous+current)%10
    return current


print("fib_last_digit({}): {}".format(input_number, fib_last_digit(input_number)))
