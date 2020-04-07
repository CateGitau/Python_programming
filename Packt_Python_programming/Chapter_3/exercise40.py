#linear search algorithm
# O(n) complexity

l = [5, 8, 1, 3, 2]

search_for = 8

for i in range(len(l)):
    if l[i] == search_for:
        print(i)