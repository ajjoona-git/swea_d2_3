# 테스트 케이스의 수 받아오기
T = int(input())
 
# 테스트 케이스 수(T)만큼 숫자 N을 받아온다.
for test_case in range(1, T+1):
    N = float(input())
    ## 소수점 아래 12자리까지 계산한다.
    # 이진수를 저장할 빈 리스트를 만들고
    binary = []
    # 12회 반복한다.
    for i in range(-1, -13, -1):
        if N >= 2 ** (i) :
            binary.append(1)  # 리스트에 1 추가
            N -= 2 ** (i)  # N 값 업데이트
        else:
            binary.append(0)  # 리스트에 0 추가
         
        # 종료 조건 추가하기
        if N == 0:
            print(f'#{test_case}', end=" ")
            # binary 리스트에 저장한 이진수를 출력한다.
            print("".join(x for x in map(str, binary)))
            break
 
    # 소수점 아래 12자리 이내로 끝나지 않은 경우
    else:
        # overflow를 출력한다.
        print(f'#{test_case} overflow')