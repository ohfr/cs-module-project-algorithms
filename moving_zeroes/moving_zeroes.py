'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # temp = []

    # for i in range(len(arr)):
    #     if arr[i] != 0:
    #         temp.append(arr[i])
    # for i in range(len(arr)):
    #     if arr[i] == 0:
    #         temp.append(arr[i])
    # return temp


    # o(n) runtime if you don't count appending.. o(1) space
    i=0

    # while i < len(arr):
    #     if arr[i] == 0:
    #         temp=arr[i]
    #         arr.pop(i)
    #         arr.append(temp)
    #     i+=1
    # return arr

    last =-1
    while i < len(arr):

        if arr[i] != 0 and last > 0:
            print(arr[last], arr[i])
            arr[last] = arr[i]
            last = -1

        if i < len(arr) -1:
            if arr[i] ==0 and arr[i+1] != 0:
                arr[i] = arr[i+1]
                arr[i+1] = 0
            elif arr[i] == 0 and arr[i+1] == 0:
                last = i
                print(last)

        i+=1
    return arr



    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")