'''

n개의 정수가 저장된 배열 A와 B가 주어진다. 배열 A의 원소는 ao, a1,  ... an-1
배열 B의 원소는 b0,b1,b2 ... bn-1이다. i=0,1,2 ... n-1에 대하여 배열  A의 원소  
ai와 배열 B의 원소 bi를 차례대로 비교한다. A원소가 더 큰 경우의 수 A
B원소가 더 큰 경우는 b라고 한다. a가 b보다 크면 1, 그렇지 않으면 0을 출력하자! 

'''
#A,B: 각각 n개의 정수가 저장된 1차원 배열 
#a>b이면 1, 그렇지 않으면 0을 반환한다. 
def solution(A,B):
    a,b =0,0
    for x,y in zip(A,B):
        if x > y:
            a+=1
        elif x <= y:
            b+=1
    return int(a>b)
    
    
#입력받기
A=map(int, input().split())
B=map(int, input().split())
print(solution(A,B))