
n = int(input("Enter a number:"))

def squares(n):
    for i in range(1, n+1):
        yield i*i

square_gen = squares(n)

# or use square_gen iterable object
for i in square_gen:
    print(i)

