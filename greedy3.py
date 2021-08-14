#숫자 카드 게임
#여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다. 단, 게임의 룰을 지키며 카드를 뽑아야 한다
# 1 숫자가 쓰인 카드들이 N*M 형태로 놓여있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
# 2 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 3 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다
# 4 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려해 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

#[전략] 여러 행들 중 가장 큰 최소값을 가진 행을 찾아내고, 그 최소값을 출력해내자.


#if 조건문 활용
print('행과 열의 개수를 입력하세요 : ',end='')
N, M = map(int, input().split(' '))

min_number = 0
new_min_number = 0

for i in range (N):
    li = list(map(int, input().split(' ')))
    new_min_number = min(li)
    if new_min_number >= min_number:
        min_number = new_min_number
    else:
        pass
print(min_number)


#min, max 활용
print('행과 열의 개수를 입력하세요 : ',end='')
N, M = map(int, input().split(' '))
min_number = 0

for i in range(N):
    li = list(map(int, input().split(' ')))
    new_min_number = min(li)
    min_number = max(min_number, new_min_number)

print(min_number)



