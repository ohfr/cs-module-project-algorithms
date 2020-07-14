from itertools import permutations
'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n <=1 :
        return 1
    temp = [n] * n
    ways = list(permutations(temp, 3))
    return len(ways)
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
