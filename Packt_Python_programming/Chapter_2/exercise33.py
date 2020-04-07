# Set Operations
# Sets support common operations such as unions and intersections. 
# A union operation returns a single set that contains all the unique elements in both set A and B;
# an intersect operation returns a single set that contains unique elements that belong to set 
# A and also belong to set B at the same time.


s5 = {1,2,3,4}
s6 = {3,4,5,6}

#union
print(s5 | s6)
print(s5.union(s6))

print('-' * 20)

#intersection
print(s5 & s6)
print(s5.intersection(s6))

print('-' * 20)

#difference between two sets
print(s5 - s6)
print(s5.difference(s6))

print('-' * 20)

#check if one set is a subset of another
print(s5 <= s6)
print(s5.issubset(s6))
s7 = {1,2,3}
s8 = {1,2,3,4,5}
print(s7 <= s8)
print(s7.issubset(s8))

print('-' * 20)

#check if s7 is a formal subset of s8, 
#and whether a set can be a proper subset
print(s7 < s8)
s9 = {1,2,3}
s10 = {1,2,3}
print(s9 < s10)
print(s9 < s9)

print('-' * 20)

#check if it is superset
print(s8 >= s7)
print(s8.issuperset(s7))
print(s8 > s7)
print(s8 > s8)