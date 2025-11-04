

nums = [0,0,0,0]

i = 0

while i >= 0:
   
    if nums[i] == 0 and i < len(nums) -1:
        i+=1
    elif nums[i] > 0 and i < len(nums) -1:
        nums[i] -=1
        i-=1
    
    else:
        print("impossible")
        break

    for i in nums:
        if nums[i]==0:
        
    print("valid")
    
    