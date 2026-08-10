'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Input: strs = ["x"]
Output: [["x"]]
'''

'''
Key Insight : Frequency map for each string, then created a sorted string with <character_count> to use in a map, store each string in its frequency key in the map
Alternate : Exploit that only lower case alphabets are present and store the frequency in a 26 array, will remove the need for sorting and allow the array to be directly used as tuple in the map
'''

def groupAnagrams(strs:list[str]) -> list[list[str]]:
    if len(strs) == 0:
        return [[""]]
    elif len(strs) == 1:
        return [[strs[0]]]
    else:
        result = {}
        for string in strs:

            # initialise all the counts to 0 for all letters
            letter_dict = {}

            # frequency count for characters in string using get method
            for c in string:
                letter_dict[c] = letter_dict.get(c,0) + 1

            sorted_string = ''
            # need to sort the keys such that each string gets modified to the form a1b2..
            # hence cat => a1c1t1
            for k in sorted(letter_dict.keys()):
                sorted_string += k + str(letter_dict[k])
                    
            
            if sorted_string in result:
                result[sorted_string].extend([string])
            else:
                result[sorted_string] = [string]

        f_result = []
        for k in result:
            f_result.append(result[k])

        return f_result


strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))