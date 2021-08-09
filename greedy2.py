#큰 수의 법칙
#다양한 수로 이루어진 배열이 있을 때 주어진 수들을 m 번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 k번을 초과해 더해질 수 없는 것이 이 법칙의 특징이다.
# 단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다. 예를 들어 순서대로 3,4,3,4,3 으로 이루어진 배열이 있을 때 M이 7이고 K가 2이면
#2번째 원소와 4번째 원소를 다른 것으로 취급한다.

#입력 조건
#첫째 줄에 N, M, K의 자연수가 주어지며, 각 자연수는 공백으로 구분한다
#둘째 줄에 n개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다.
#K는 항상 M보다 작거나 같다

n,m,k = map(int,input().split())
li = list(map(int,input().split()))
li.sort()

#연산에 사용할 큰 수
f = li[n-1]
s = li[n-2]

cnt = (m // (k+1)) * k
cnt += m % (k+1)

result = (cnt * f) + (m // (k+1)) * s
print(result)


# (+)연속 조건이 없고, 무조건 원소 1개의 최대 입력 횟수가 k번일 경우
# n,m,k = map(int,input().split())
# li = list(map(int,input().split()))
#
# li2 = sorted(li, reverse=True)
#
#
# result = 0
#
# for i in li2:
#     if m>=k:
#         result += i * k
#         m -= k
#     elif m < k and m >= 0:
#         result += i * m
#     else:
#         pass
# print(result)
#
