# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸기
# 기준(pivot)을 설정하여 pivot보다 작은 데이터와 큰 데이터를 찾음
# 반으로 나눠서 다시 작업 진행

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 직관적인 형태의 퀵 정렬 코드
def quick_sort(array, start, end):
    if start >= end : # 원소가 1개인 경우 종료
        return 
    pivot = start # pivot은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right :
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot] :
            left += 1
        # pivot보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot] :
            right -= 1
        if left > right : # 엇갈렸다면 작은 데이터뫄 pivot을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else : # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)


# 파이썬의 장점을 살린 퀵 정렬 코드
def quick_sort_2(array) :
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1 :
        return array

    pivot = array[0] # pivot은 첫 번째 원소
    tail = array[1:] # pivot을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)

# quick_sort(array, 0, len(array) - 1)
print(quick_sort_2(array))
