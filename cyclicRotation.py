def solution(nums, count):
    # write your code in Python 3.6
    
    if not nums:
        return 0
    if count == len(nums):
        return nums

    ans = []
    count = count % len(nums)
    i = len(nums) - count
    
    while i < len(nums):
        ans.append(nums[i])
        print(i)
        i = i + 1

    i = 0
    
    while i+count < len(nums):
        ans.append(nums[i])
        i = i + 1
    return ans

def main():
    #nums = [1,2,3,4]
    #nums = [3, 8, 9, 7, 6]
    nums = [1000,1001,1002,1003,1004]
    #nums = []
    #nums = [1]
    #solution(nums,1)  ## ans = [4,1,2,3]
    #solution(nums,2)  ## ans = [3,4,1,2]
    #solution(nums,3)  ## ans = [2,3,4,1]
    #solution(nums,4)  ## ans = [1,2,3,4]
    ans = solution(nums,3)
    print("ans = {}".format(ans))
if __name__ == '__main__':
    main()