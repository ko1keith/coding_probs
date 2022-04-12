# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


from two_sum import TwoSum

def main():
    obj = TwoSum()
    # solution = obj.twoSum( [2,7,11,15], 9)
    # print("Expected output: [0, 1]")
    # print("Actual output: "),
    # print(solution)
    
    # solution = obj.twoSum( [3,2,4], 6)
    # print("Expected output: [1, 2]")
    # print("Actual output: "),
    # print(solution)
    
    solution = obj.twoSumHash( [2,7,11,15], 9)
    print("Expected output: [0, 1]")
    print("Actual output: "),
    print(solution)
    
    solution = obj.twoSumHash( [3,2,4], 6)
    print("Expected output: [1, 2]")
    print("Actual output: "),
    print(solution)
    
if __name__ == '__main__':
    main()
    