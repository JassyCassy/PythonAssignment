from collections import Counter
def singleNumber(nums):
    freq = Counter(nums)
    for i in freq:
        if(freq[i] == 1):
            return i
 
 

a = [4, 1, 2, 1, 2]
print("The element with single occurrence is ",
      int(singleNumber(a)))


#Exercise Task #3:
#Given a non-empty list of integers, every element appears twice except for one. Find that single one.      