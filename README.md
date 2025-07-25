# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 D2

## 문제

```

0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.

N = 0.625
0.101 (이진수)
= 1*2-1 + 0*2-2 + 1*2-3
= 0.5 + 0 + 0.125
= 0.625

N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 소수점 아래가 12자리 이내인 N이 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

## 설계

```python
<소수를 이진수로 바꾸기>

# 이진수를 저장할 리스트를 만들고 12회 반복
for i in range(12):
	if N ≥ 2**(-1) :
		리스트에 1 추가
		N -= 2**(-1)		
	else:
		리스트에 0 추가

	# 종료 조건 추가하기
	if N == 0: 
		for i in binary:
			print(i, end='')

else:
	print('overflow')
	
'''
ex. N = 0.625

1. 0.625 > 0.5  → binary = 1, N = 0.125
2. 0.125 < 0.25 → binary += 0, N = 0.125
3. 0.125 = 0.125 → binary += 1, N = 0
'''
```

## 초기 코드 → Memory Error

```python
# 초기 코드 -> Memory Error
# Error Message: Memory error occurred, (e.g. segmentation error, memory limit Exceed, stack overflow,... etc)

# 테스트 케이스의 수 받아오기
T = int(input())

# 테스트 케이스 수(T)만큼 숫자 N을 받아온다.
for test_case in range(1, T+1):
    N = int(input())
	## 소수점 아래 12자리까지 계산한다.
    # 이진수를 저장할 빈 리스트를 만들고
    binary = []
    # 12회 반복한다.
    for i in range(-1, -13):
        if N >= 2 ** (i) :
            binary.append(1)  # 리스트에 1 추가
            N -= 2 ** (i)  # N 값 업데이트
        else:
            binary.append(0)  # 리스트에 0 추가
		
        # 종료 조건 추가하기
        if N == 0:
            print(f'#{test_case}', end=" ")
            # binary 리스트에 저장한 이진수를 출력한다.
            print("".join(x for x in binary))
            break

	# 소수점 아래 12자리 이내로 끝나지 않은 경우
    else:
		# overflow를 출력한다.
        print(f'#{test_case} overflow')
```

## 문제해결

1. N은 소수이기 때문에 float 형태로 받아야 함!
2. **출력 형식 오류**: `binary` 리스트에는 숫자(0 또는 1)가 들어있는데, `"".join()` 함수는 문자열 리스트를 합치는 데 사용됩니다. 숫자 리스트를 합치려고 하면 `TypeError`가 발생합니다. `map(str, binary)`를 사용해 리스트의 모든 숫자를 문자열로 변환한 후 합쳐야 합니다.