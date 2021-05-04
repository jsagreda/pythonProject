# Python program to calculate the Fibonacci sequence
# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55


def fibo(fib_n):
    if fib_n <= 1:
        return fib_n
    else:
        return (fibo(fib_n - 1) + fibo(fib_n - 2))


# Calculate Fibonacci

result = fibo(10)
print('fibo(10) = ' + str(result))