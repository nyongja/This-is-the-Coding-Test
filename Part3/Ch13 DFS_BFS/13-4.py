# 13-4 18. 괄호변환
<<<<<<< HEAD
=======

>>>>>>> 7bb61eb5b6c500e9c1dd11afc238fc72f4499a96
# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p) :
    count = 0 # 왼쪽 괄호 개수
    for i in range(len(p)) :
        if p[i] == "(" :
            count += 1
        else :
            count -= 1
        if count == 0 :
            return i
# 올바른 괄호 문자열인지 판단
def check_proper(p) :
    count = 0 # 왼쪽 괄호 개수
<<<<<<< HEAD
    for i in p : 
=======
    for i in p :
>>>>>>> 7bb61eb5b6c500e9c1dd11afc238fc72f4499a96
        if i == '(' :
            count += 1
        else :
            if count == 0 : # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    if p == '' :
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1 :]
    # 올바른 괄호 문자열이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u) :
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면 아래의 과정을 수행
    else :
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자 제거
        for i in range(len(u)) :
            if u[i] == "(" :
                u[i] = ")"
            else :
                u[i] = '('
        answer += "".join(u)
    return answer

p = input()
<<<<<<< HEAD
print(solution(p))  
=======
print(solution(p))
>>>>>>> 7bb61eb5b6c500e9c1dd11afc238fc72f4499a96