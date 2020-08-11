
'''
Given an array of citations (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia:
"A scientist has index h if h of his/her N papers have at least h citations each, 
and the other N − h papers have no more than h citations each."
'''
citations = [3, 0, 6, 1, 5]
0,1,3,5,6
def hIndex(citations):
    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= (n-i):
            return n-i
    return 0

def hIndex2(citations):
    N = len(citations)
    citations.sort()
    i = 0
    while i < N and citations[N - 1 - i] > i:
        i += 1
    return i

print(hIndex2(citations))

