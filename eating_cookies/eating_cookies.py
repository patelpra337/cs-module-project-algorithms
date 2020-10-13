'''
Input: an integer
Returns: an integer
'''
# Function for Fibonacci sequence using recursion.
def eating_cookies(n, cache=None):
    if cache is None:
        cache = {}
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    if cache and cache[n]:
        return cache[n]

    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]
        
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

'''Fibonacci series is basically a sequence. In that sequence, each number is sum 
of previous two preceding number of that sequence. Initial two number of the series 
is either 0 and 1 or 1 and 1. We will consider 0 and 1 as first two numbers in our example. 
So, the first few number in this series are

0 1 1 2 3 5 8 13 21 34

1st Fibonacci number = 0 (by assumption)
2nd Fibonacci number = 1 (by assumption)
3rd Fibonacci number = 1st + 2nd
= 0 + 1
= 1
4th Fibonacci number = 2nd + 3rd
= 1 + 1
= 2
5th Fibonacci number = 3rd + 4th
= 1 + 2
= 3
6th Fibonacci number = 4th + 5th
= 2 + 3
= 5
So, nth Fibonacci number = (n-1)th Fibonacci + (n-2)th Fibonacci
'''

'''
0|1
1|1
2|2
3|4
4|7
5|13
'''
