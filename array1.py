'''
입력크기 n인 정수형 배열 A와 정수K가 주어진다. 배열 A의 원소는 a0 a1 a2  ... an-1이다. 
배열 A의 원소 중에서 값이 k인 원소의 개수를 출력하자. 
'''

#n, A: 원소의 개수가 n인 정수형 배열 A
#배열 A의 원소 중에서 값이 k인 원소의 개수를 반환한다. 
def solution(n,A,k):
  answer=0
  for i in A:
    if i==k:
      answer+=1
  return answer



#사용자에게 입력받기 
n,k = map(int,input().split())
A=list(map(int,input().split()))
print(solution(n,A,k))

