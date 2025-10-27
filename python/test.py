def lexicalOrder(n: int):
    result = []
    curr = 1
    for _ in range(n):
        result.append(curr)
        if curr * 10 <= n:
            curr *= 10
        else:
            while curr % 10 == 9 or curr + 1 > n:
                curr //= 10
            curr += 1
    return result

def findKthNumber( n: int, k: int) -> int:
    result = 0
    curr = 1
    for _ in range(k):
        result = curr
        if curr * 10 <= n:
            curr *= 10
        else:
            while curr % 10 == 9 or curr + 1 > n:
                curr //= 10
            curr += 1
    return result

print(lexicalOrder(681692778))
#print(findKthNumber(681692778,351251360))