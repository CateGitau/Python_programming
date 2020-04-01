"""
Given a non-empty array of integers, 
every element appears twice except for one. 
Find that single one.
"""

nums =  [4,1,2,1,2]

# list operation
# Time compexity O(n^2)
# Space complexity: O(n)
def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()


#Hash Table
#Time compexity O(n)
# Space complexity: O(n)
def singleNumber2(nums):
    count_dic = {}
    
    
    for i in nums:
        if i not in count_dic:
            count_dic[i] = 1
        else:
            count_dic[i] += 1
    return min(count_dic, key=count_dic.get)


#Math
# Time complexity O(n+n) = O(n)
# Space complexity(O(n+n)) = O(n)
def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)

    
# Bit Manipulation
# Time complexity: O(n)
# Space complexity: O(1)
def singleNumber4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
    

