'''
Given a list of strings that contains anagrams, write a function to print pairs of those anagrams.
'''

def anagrams(lst):
    """
    Function to find anagram pairs
    :param lst: A lst of strings
    :return: Group of anagrams
    """

    dictionary = {}

    for string in lst:
        key = ''.join(sorted(string))

        if key in dictionary.keys():
            dictionary[key].append(string)
        
        else:
            dictionary[key] = []
            dictionary[key].append(string)

    result = []
    for key, value in dictionary.items():
        if len(value) >= 2:
            result.append(value)

    result = sorted(result) # sort the list

    return result

# Driver to test above code
if __name__ == '__main__':

    lst = ['tom marvolo riddle ', 'abc', 'def', 'cab', 'fed', 'clint eastwood ', 'i am lord voldemort', 'elvis', 'old west action', 'lives']
    print (anagrams(lst))
    