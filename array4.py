'''
크기가 nxn인 정수형 2차원 배열 A가 주어진다. 배열 A의 원소는 a00,a01, ... an-1n-1
이다. k가 주어지면 배열 A의 원소 중에서 값이 k인 원소의 개수를 출력하자.
입력1: 첫째줄 - n,k가 공백을 사이에 두고 순서대로 주어진다.
입력2: 두번째 줄 - n개의 줄에 걸쳐 배열 A의 첫번째 행부터 마지막 행까지 순서대로 주어진다. 
입력2의 띄어쓰기 하면서 n개 줄 입력하기 

'''
#n,A : 크기가 nxn인 정수형 2차원 배열 A
#2차원 배열 A의 원소 중에서 값이 k인 원소의 개수를 반환한다.

def solution(n,A,k):
    #2차원 배열 A의 원소 중에서 값이 k인 원소의 개수를 구한다. 
    answer=0 
    for i in range(n):
        for j in range(n):
            if A[i][j]==k:
                answer += 1 
                
    return answer
    
    
    #입력1 
    n, k = map(int, input().split())
    A=list(list(map(int, input().split())) for _ in range(n))
    #input().split()은 사용자로부터 입력을 받고, 받은 문자열을 공백을 기준으로 분리한 후 리스트로 저장합니다. 
    #map : "1 2 3"과 같은 문자열을 1 2 3 숫자로 변환 
    #for _ in range(n) 부분은 반복문을 의미합니다. 이 반복문은 n번 반복하며, 
    #각 반복에서 사용자로부터 공백으로 구분된 숫자를 입력받아 리스트 A의 각 행(row)으로 추가
    
    
    
    
    print(solution(n,A,k))