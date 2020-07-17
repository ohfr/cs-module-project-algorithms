from itertools import permutations
'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    temp = 0
    res = [1]  
        
    for i in range(1, n + 1): 
        s = i - 3 - 1
        e = i - 1
        if (s >= 0): 
            temp -= res[s]  
        temp += res[e]  
        res.append(temp)  
            
    return res[n]

    # if n < 0:
    #     return 0
    # if n ==0:
    #     return 1
    # ways = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    # return ways

def eating_cookies_cache(n, cache):
    if n < 0:
        return 0
    if n ==0 :
        return 1
    
    if cache[n] > 0:
        return cache[n]
    ways = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return ways
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
