from itertools import combinations # 조합을 위한 라이브러리 함수 
from collections import Counter # 딕셔너리보다 카운트 함수를 활용 

def solution(orders, course):
    answer = []
    
    for num in course:
        array = []
        for order in orders:  # 주문 문자열 정렬
            order = sorted(order) 
            array.extend(list(combinations(order, num))) # array에 현재 주문에서 num개를 뽑아 나올 수 있는 경우를 넣음
       
        count = Counter(array)  # 카운터를 사용하여 중복되는 횟수를 셈
        
        if count:
            if max(count.values()) >= 2:  # 제일 많이 나온 조합이 두번 이상이면? 
                for key, value in count.items():
                    if value == max(count.values()):   # 현재 조합이 가장 많이 나오면 결과 배열에 추가
                        answer.append("".join(key))
    
    return sorted(answer)
