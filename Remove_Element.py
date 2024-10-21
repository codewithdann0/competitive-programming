
# def  removeElemnet(nums,val):
#     k=0
#     for i in range(len(nums)):
#        if nums[i] != val:
#            nums[k] = nums[i]
#            K +=1
#  return k;     
nums = [3,2,2,3]
val= 3
def removeElement(nums, val):
    k = 0  # Initialize the count of valid elements

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # Place valid elements at the beginning
            k += 1  # Increment the count of valid elements

    return k  # Return the count of valid elements
       


removeElement(nums, val)