def isPalindrome(s: str) -> bool:
    # remove all non alphanumeric characters from the string
    # create 2 pointers from the start and the end
    # check each char, if it matches then proceed, else return False
    # if the pointers point to the same char or cross over, then return True

    alpha_num_s = [char.lower() for char in s if char.isalnum()] # finds only the alpha numeric chars and stores it in a list

    if(len(alpha_num_s) < 2):
        return True

    first_pointer = 0
    last_pointer = len(alpha_num_s) - 1

    while first_pointer < last_pointer:
        # chars match so modify both pointers
        if alpha_num_s[first_pointer] == alpha_num_s[last_pointer]:
            first_pointer += 1
            last_pointer -= 1
        else:
            return False

    return True

def isPalindromeStringManipulation(s : str) -> bool:
    alpha_num_s = [char.lower() for char in s if char.isalnum()] # finds only the alpha numeric chars and stores it in a list
    s_new = ''.join(alpha_num_s)

    if len(s_new) < 2:
        return True
    
    reverse_s = s_new[::-1]

    if s_new == reverse_s:
        return True
    else:
        return False

s = "Was it a car or a cat I saw?"
print(isPalindromeStringManipulation(s))