#고장난 컴퓨터
#문제
#https://level.goorm.io/exam/49095/%EA%B3%A0%EC%9E%A5%EB%82%9C-%EC%BB%B4%ED%93%A8%ED%84%B0/quiz/1

n, delay = map(int,input().split(' '))
times = input().split(' ')

for i in range(n):
    times[i] = int(times[i])

cnt = 1
for i in range(n-1):
    if times[i+1] - times[i] <= delay:
        cnt += 1
    else:
        cnt = 1

print(cnt)
