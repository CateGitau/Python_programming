'''
For an integer N find the number of trailing zeroes in N!
'''
n = 5

def trail_zeros(n):
    if n<5:
        return 0
    else:
        return (n//5)+trail_zeros(n//5)

print(trail_zeros(5))


