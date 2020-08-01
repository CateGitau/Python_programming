
num = 700
div3 = []
div5 = []
final = []
for i in range(num):
    if i % 13 == 3:
        div3.append(i)
print(len(div3))
for j in range(len(div3)):
    if j % 12 == 5:
        div5.append(j)
print(div5)
for k in range(len(div5)):
    if k % 11 == 0:
        final.append(k)

print(final)



