def fibonacci_recr(n):
    if n <= 0:
        print ("error - numbers cannot be negative for Fib sequence.")
        exit()
    elif n == 0:
        return 0
    elif n == 2 or n == 1:
        return 1
    else:
        return fibonacci_recr(n - 1) + fibonacci_recr(n - 2)

def fibonacci_gen(n):
    if n < 0:
        print("error - cannot be neg. number.")
    else:
        a = 0
        b = 1
        for _ in range(n):
            yield a
            # a, b = b, a + b
            total = a + b
            a = b
            b = total

def factorial(n):
    if n == 1:
        yield 1
    else:
        yield n * factorial(n-1)

n = int(input("Enter a number:"))
def squares(n):
    for i in range(1, n+1):
        yield i*i

square_gen = squares(n)
for i in square_gen:
    print(i)

# fibonacci series
n = int(input("Enter number for fibonacci series: "))
fib = fibonacci_gen(n)
# print(f'fib({n}) = {fib}')
for n in fib:
      print(n)

# def main():
#     n = int(input("Enter number for fibonacci series: "))
#     fib = fibonacci(n)
#     for n in fib:
#         print(n)
#
# if __name__ == '__main()__':
#     main()