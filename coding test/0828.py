# 1. 풀이 
def solution(numbers):
    answer = []
    
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    # 중복을 제거하고 오름차순으로 정렬
    answer = sorted(list(set(answer)))
    
    return answer

  ''' sort와 sorted의 차이점
  - sort는 리스트형 메소드이며 리스트 원본값을 직접 수정한다
  - sorted는 내장함수이며 원본값은 그대로 두고 정렬 값을 반환한다 ''' 

  
  
# 2. 다른 사람의 풀이 (무려 한줄..) 
# list comprehension을 이용한 풀이 

from itertools import combinations
def solution(numbers):
    return sorted(list(set([sum([i,j]) for i,j in combinations(numbers,2)])))
  
  
''' itertools : 파이썬 기본 라이브러리
combination 내장함수를 활용해 인자값에 따라 구할 수 있는 모든 조합을 리턴한다.
하위 함수로 permutation(list 순열 리턴), product(두개 이상의 리스트에서 조합을 리턴)을 가진다. '''
  
