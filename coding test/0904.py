# set 함수로 중복된 폰켓몬의 종류를 찾은 뒤 개수를 구함.

def solution(nums):
    unique_types = len(set(nums))

    if len(nums) / 2 > unique_types:
        return unique_types
    else:
        return len(nums) / 2
