def solution(nums):
    # write your code in Python 3.6
    
    
    ## time complexity = O(N)*2 + O(N) = O(N)

    
    i = 1
    sum1 = sum(nums[:1])## part 1
    sum2 = sum(nums[1:])## part 2
    diff = abs(sum1 - sum2)
    minDiff = diff
    ans = 1
    
    while i < len(nums)-1 :
        sum1 = sum1 + nums[i]
        sum2 = sum2 - nums[i]
        diff = abs(sum1 - sum2)
        if minDiff > diff:
            minDiff = diff
            ans = i+1

        i = i + 1
    print(ans,minDiff)
    
    return minDiff
        
    
def main():
    #A = [1,6,4,3,2,1]
    #A = [1,2,3]
    #A = [1,3,4]
    #A = [2,3,4]
    #A = [1,2,3,-2000,2000]
    #A = [-1000,1000]
    #A = [-1,-2]
    #A = [1,4]
    #A = [2,3,3,3,3,4,5]
    #A = [-3,-1]
    A = [3,3,2,4,4]

    ans = solution(A)
    print("ans = {}".format(ans))

if __name__ == '__main__':
    main()