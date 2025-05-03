def is_multiple(n,m):
    if n % m == 0:
        return True
    else:
        return False
    
n = int(input("Enter an integer: "))
m = int(input("Enter another integer: "))
print(is_multiple(n,m))