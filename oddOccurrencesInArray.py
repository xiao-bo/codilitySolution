def solution(A):
    # write your code in Python 3.6
    if not A:
        return A
    ans = 0
    for x in A:
        ans = ans ^ x
        
    return ans
def main():
    a = [0,0,1,2,2,3,3,4,4,5,5]
    ans = solution(a)
    print('ans = {}'.format(ans))

if __name__ == '__main__':
    main()