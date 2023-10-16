'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

#n, A: 원소의 개수가 n인 정수형 배열 A
#배열 A의 원소 중에서 값이 k인 원소의 개수를 반환한다. 
def solution(n,A,k):
  answer=0
  for i in A:
    if i==k:
      answer+=1
  return answer



#사용자에게 입렵받기 
n,k = map(int,input().split())
A=list(map(int,input().split()))
print(solution(n,A,k))

