# 퀵 정렬
import sys
input = sys.stdin.readline

def quick_sort(array, start, end):
    
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    
    # 엇갈리기 전까지 반복
    while left <= right: # 인덱스
        
        # left는 오른쪽으로 향하며 피벗보다 큰 값을 찾음.
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        
        # right는 왼쪽으로 향하며 피벗보다 작은 값을 찾음
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        # 엇갈렸다면
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
        
    # pivot을 제외하고 두 분할로 다시 정렬
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)       


n = int(input())
ns = []
for _ in range(n):
    ns.append(int(input()))

quick_sort(ns, 0, len(ns)-1)
print(ns)