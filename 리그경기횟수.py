#리그 경기 횟수 구하기
#문제
#https://level.goorm.io/exam/43092/%EB%A6%AC%EA%B7%B8-%EA%B2%BD%EA%B8%B0-%ED%9A%9F%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

n = int(input())
#기본
sum = 0
for i in range(1,n):
    sum += i
print(sum)

#재귀
def add(n):
    if n == 1:
        return 1
    else:
        return add(n-1) + n
print(add(n-1))

# #단순 연산
print((n*n-n)//2)
