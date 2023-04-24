'''
최대공약수 구는 문제
시도
(1) 유클리드 호제법 -> 500000000000000000 500000000000000002를 입력하면 메모리 오류
'''

def GCD(a,b):
    if b == 0:
        return a
    return GCD(b,a%b)
a,b = list(map(int,input().split()))
a,b = (b,a) if b > a else (a,b)
# 시도 (1)
# a,b = int('1'*a),int('1'*b)

print('1'*GCD(a,b))

#시도(2)
# print((b-a)*'1')