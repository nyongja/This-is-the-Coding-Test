# sorted는 리스트 자료형 반환
# sort는 반환 없이 내부 원소 바로 정렬

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1] 

result = sorted(array, key = setting)
print(result)