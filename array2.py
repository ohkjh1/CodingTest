'''

크기 n인 정수형 배열 A가 주어진다. 배열 A의 원소는 AO A1 ... AN-1이다. 
입력으로 i,j,k가 주어지면 배열 A의 i번째 원소 a1부터 j번째 원소 aj에 k를 곱하는 연산 수행하자.
연산을 수행한 후 배열 A의 모든 원소의 합을 출력하자. 

'''

#n, A: 원소의 개수가 n인 정수형 배열 A
#i,j,k : 배열 A의 i번째 원소부터 j번째 원소에 k를 곱하는 연산 수행 

def solution(A,i,j,k):
  
  for doc in range(i, j+1):
    A[doc] = A[doc]*k
     
  return sum(A)



#사용자에게 입렵받기 
# n = map(int,input().split())
A=list(map(int,input().split()))
i, j, k=map(int, input().split())
print(solution(A,i,j,k))

