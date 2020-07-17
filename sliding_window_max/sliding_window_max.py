'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # this takes o(n) space
    # arr = []
    # i =0
    # while i < len(nums) - k+1:
    #     curMax = -10000
    #     for j in range(k):
    #         if nums[j+i] > curMax:
    #             curMax = nums[j+i]
    #     arr.append(curMax)
    #     curMax=0
    #     i+=1
    # return arr
    i =0
    while i < len(nums) - k+1:
        curMax = max(arr[i:k+i])
        nums[i] = curMax
        curMax=0
        i+=1
    while i < len(nums):
        nums.pop(i)
    return nums



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
