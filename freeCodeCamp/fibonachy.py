
# Una recursion o callback es cuando una funcion se llama a si misma 
def find_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return find_fibonacci(n-1) + find_fibonacci(n-2)

for i in range(10):
    print(find_fibonacci(i))