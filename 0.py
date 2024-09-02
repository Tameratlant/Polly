nums = [1,1]
#nums.append (nums[0] + nums[1]) #[2] элемент
n = 100
for i in range(2, n):
    nums.append(nums[i-1] + nums[i-2])
    print("Current nums[i] = ", nums[i]) 
print(nums[n-1])

#1 1 2 3 5 8