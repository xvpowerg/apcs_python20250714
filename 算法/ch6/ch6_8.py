import random
nums = random.sample(range(1,100),10)
nums.sort(reverse = True)
print(nums)
maxList = nums[:3]
maxSum = 0 
for v in maxList:
    maxSum += v
print(maxSum)
