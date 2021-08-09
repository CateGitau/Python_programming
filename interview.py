lista1 = []
lista2 = [1]
lista3 = [2, 3]
lista4 = [1, 2, 3, 4]


listb1 = []
listb2 = [lista1, lista2]
listb3 = [lista3, lista4]

listc1 = [listb1, listb2, listb3]


# print(listc1)

def print_values(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(*lst[i][j])
    return

# print(print_values(listc1))

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

print(flatten(listc1))






