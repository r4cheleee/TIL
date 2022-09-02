## [프로그래머스] 월간코드챌3: 없는 숫자 더하기 

# 가장 기본적인 풀이 
def solution(numbers):
    answer=0
    for i in range(1,10):
        if i not in numbers:
            answer += i
    return answer
  
# 압축한 풀이
def solution(numbers):
    return sum(x for x in range(10) if x not in numbers)

# 기발한 풀이 
def solution(numbers):
    return 45 - sum(numbers)
  
  
## [프로그래머스] 월간코드챌3: 나머지가 1이 되는 수 

# 나의 풀이
def solution(n):
    answer = 0
    
    for i in range(1, n):
        if n % i == 1:
            return i
          
         
# 압축한 풀이
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]
