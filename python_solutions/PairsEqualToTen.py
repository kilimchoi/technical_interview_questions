#caltonji 10/31/2015
def pairsEqualToK(nums, k):
    tupleList = []
    for i in nums:
        if (k - i) in nums:
            tupleList.append((k-i, i))
    return tupleList
def moreEfficient(nums, k):
    tupleList = []
    hashMap = {}
    for i, num in enumerate(nums):
        if not num in hashMap:
            hashMap[num] = i
    for i, num in enumerate(nums):
        if (k - num) in hashMap:
            if ( not hashMap[k-num] == -1 and not hashMap[k-num] == i ):
                hashMap[num] = -1
                tupleList.append((k-i, i))
    return tupleList
testa = [2,3,2,-1, 11, 7]
testb = [2, 5, 3,2,-1, 5, 11, 7]
if __name__ == "__main__":
    print moreEfficient(testb, 10)

