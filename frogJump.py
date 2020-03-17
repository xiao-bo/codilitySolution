import math
def solution(origin, destination, distance):
    # write your code in Python 3.6
    return int(math.ceil((destination - origin) / distance ))

def main():
    origin = 10
    destination = 90
    distance = 30
    ans = solution(origin,destination,distance)
    print('ans = {}'.format(ans))


if __name__ == '__main__':
    main()