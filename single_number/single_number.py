'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

''' If we add each number once and multiply the sum by 2, 
we will get twice the sum of each element of the array. 
Then we will subtract the sum of the whole array from 
the twice_sum and get the required number 
(which appears once in the array).
'''

def single_number(arr):
    # Your code here
    return 2 * sum(set(arr)) - sum(arr)

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
