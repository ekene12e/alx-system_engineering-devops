#!/usr/bin/python3

def solution(A):
    for i in range(1, 100000):
        if i not in sorted(A):
            return i

if __name__ == "__main__":
    a = solution([1,0,2, 3, 7,-5])
    b = solution([-1,-2,-3,-4,5,1])
    c = solution([56,77,88,99])
    print(a)
    print (b)
    print(c)

