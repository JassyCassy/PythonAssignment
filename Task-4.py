def solve(number):
   n=len(nums)
   rs=[nums[0]]

   for i in range(1,n):
      nums[i]+=nums[i-1]
      rs.append(nums[i])
   return rs

nums = [1,2,3,4]
print(solve(nums))




#Exercise Task #4:
#Given a list nums. We define a running sum of a list as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.