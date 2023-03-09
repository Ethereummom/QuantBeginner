#다양한따옴표의사용
#case1)
a = '"python is easy."'
#작은따옴표 안에 큰 따옴표는 문자열을 만드는 기호로 인식되지 않음.
print(a)
#출력 시 큰따옴표 자체도 그냥 문자로 인식되어 출력됨.
#case2) 백슬래시 사용
b = 'python\'s favorite food is pasta.'
#python's에서 's가 문자열로 인식됨!
print(b)

#case3) 줄바꿈 - 이스케이프코드 \n사용
multiline = "Life is too short \n so you need CHATGPT"
print(multiline)
#백슬래시n을 통하여 문자열의 줄 바꿈 가능.

#case4)백슬래시n이 불편할경우 '''나 """사용
multiline2 = """ChatGpt
is legend
is crazy
"""
print(multiline2)

#파이썬은 문자열 곱이 가능.. 매우 직관적임
c = "CHATGPT"
print(c * 5)