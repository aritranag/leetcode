'''
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

Input: temperatures = [22,21,20]
Output: [0,0,0]
'''
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    # start from the end and keep track of the max temp seen up until now and its index
    # for every value, need to check from its index till the max temp index, for increment of the index use the array calculated up until now to shorten the search
    res = [0] * len(temperatures)
    max_temp,max_temp_index = 0,0
    for i in range(len(temperatures)-1,-1,-1):
        cur_temp = temperatures[i]
        if cur_temp >= max_temp:
            # no warmer temperature has been found up until now, set the value for this res to 0 and set the max temp
            max_temp = cur_temp
            res[i] = 0
            max_temp_index = i
        else:
            j = i + 1
            while j <= max_temp_index:
                if temperatures[j] > cur_temp:
                    res[i] = j - i
                    break
                else:
                    if res[j] == 0: # if there is no higher temperature 
                        break
                    else:
                        j = j + res[j]

    return res


temperatures = [22,21,20,24,25]
print(dailyTemperatures(temperatures))
