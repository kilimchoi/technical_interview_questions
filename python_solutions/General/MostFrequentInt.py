#caltonji 10/31/2015
lista = [0, 1, 3, 2, 23, 43, 2, 1, 5, 2, 5, 2, 56, 23, 0, -1, 2, 2]
listb = [4, 0, 1, 0, 4, 4, 4, 4, 0, 1, 1, 1,-6, 7]
def mostFrequent(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 0
    maxKey = None
    maxVal = 0
    for key, value in freq.iteritems():
        if value > maxVal:
            maxVal = value
            maxKey = key
    return maxKey
    
if __name__ == "__main__":
    print "Most Frequent for a: " +  str(mostFrequent(lista))
    print "Most Frequent for b: " +  str(mostFrequent(listb))


# http://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary`
