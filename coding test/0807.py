from collections import defaultdict # key가 비어있는 경우 대비 
from itertools import combinations

def solution(info, query):
    answer = []
    _dict = defaultdict(list)
    
    for i in info:
        data = i.split(' ')
        score = int(data[-1])
        data = data[:-1]
        
        for n in range(5):
            for c in combinations(data, n): # 모든 조합을 구하라 
                key = ''.join(c)
                _dict[key].append(score)
                
    for value in _dict.values():
        value.sort()

    for q in query:
        q = q.split(' ')
        point = int(q[-1])
        q = q[:-1]
        
        q = ''.join(q)
        q = q.replace('-', '')
        q = q.replace('and', '')

        if q in _dict:
            scores = _dict[q]
            if len(scores) > 0:
                left, right = 0, len(scores) # lower bound 이용해서 인덱스 찾기
                
                while left < right:
                    mid = (left + right) // 2
                    
                    if scores[mid] >= point:
                        right = mid
                    else:
                        left = mid + 1
                answer.append(len(scores) - left)
        else:
            answer.append(0)
        
    return answer
