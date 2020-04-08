def countdown(n):
    if n == 0:
        return "Liftoff!!"
    else:
        print(n)
        return countdown(n-1)

print(countdown(3))