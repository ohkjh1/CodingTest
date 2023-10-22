'''
크기 n인 정수형 배열 A가 주어진다. A의 원소는 a0,a1,...an-1이다.
입력으로 i,j,k가 주어지면 배열A의 첫번째 A의 i번째 원소 ai에 k를 곱하는 연산을 수행하자.
연산을 수행한 후 배열 A의 모든 원소의 합을 출력하자!

(첫 번째 줄에 n이 주어진다.
두번째 줄에 배열A의 원소 a0 a1 .... an-1
세번째 줄에 i,j,k가 공백을 사이에 두고 순서대로 주어진다.)

'''
def solution(n,A,i,j,k):
    for idx in range(i,j,+1):
        A[idx]=A[idx]*k
        
    return sum(A)


n=map(int,input().split()) 
A=list(map(int,input().split()))
i,j,k=map(int,input().split())
print(solution(n,A,i,j,k))

#공백으로 입력할 것 