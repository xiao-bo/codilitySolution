def solution(nums):
    # write your code in Python 3.6
    if not nums:
        return 1
    '''
    for index in range(1,len(nums)+1):
        if index not in nums:
            ## hash table is exceed time limit
            return index
    #return len(tmp)+1
    '''

    tmp = sorted(nums)
    for index in range(0,len(tmp)):
        ## check index and value are same  
        if tmp[index] != index+1:
            return index+1
    return len(tmp)+1
    


def main():
    nums = [1,2,3,5]
    #nums = [3]
    #nums = [2,3]
    #nums = [1,3,4]
    nums = [1,2]
    ans = solution(nums)
    print('ans = {}'.format(ans))

if __name__ == '__main__':
    main()