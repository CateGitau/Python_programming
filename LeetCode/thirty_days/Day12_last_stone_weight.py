arr = [2,2]


def lastStoneWeight(stones):
    if len(stones) > 1:
        stones = sorted(stones)
        x = stones[-2]
        y = stones[-1]
        
        if x == y:
            stones[-1] = y-x
            
        elif x!=y:
            stones[-1] = y-x
            
        stones.pop(-2)    
        return lastStoneWeight(stones)

    else:
        return stones
    
print(lastStoneWeight(arr))


#submitted code
def lastStoneWeight2(stones):
    while len(stones) > 0:
        if len(stones) == 1:
            return stones[0]
        
        else:
            stones = sorted(stones)
            x = stones[-2]
            y = stones[-1]

            if x == y or x!= y:
                stones[-1] = y-x
                
            stones.pop(-2)
            