'''
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Input: s = "XYYX", k = 2
Output: 4

Input: s = "AAABABB", k = 1
Output: 5
'''


def characterReplacement_Brute(s: str, k: int) -> int:
    # base cases, s = 0 or k > s
    if len(s) == 0:
        return 0

    # if k is equal to or greater than s we can replace all chars and make it same
    if k >= len(s):
        return len(s) 

    max_length = 0

    char_set = set(s)
    for char in char_set:
        l, count = 0,0
        for r in range(len(s)): #look through all the window in the string
            if s[r] == char:
                count += 1

            while (r-l + 1) - count > k: # when window size - most frequent char count is greater than k, we need to adjust the window and count
                if s[l] == char:
                    count -= 1 # when we are sliding the window we have to ensure that if the char being removed is also part of the count, then adjust
                l += 1

            max_length = max(max_length,r-l+1)
            

    return max_length


#s = "AAAAABBBBCBB"
s = "XYYXAAABBCDECBBAAADDBBBYX"
k = 4
print(characterReplacement_Brute(s,k))