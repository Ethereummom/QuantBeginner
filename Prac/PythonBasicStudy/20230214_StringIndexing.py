##파이썬 문자열 인덱싱&슬라이싱
#인덱싱 = 문자열 안의 특정한 값을 뽑아냄.

a = "CHATGPTISGOD"
print(a[10])
#a라는 문자열의 10번째 인덱스값 추출.
for i in range(0,10):
    print(a[i])

#슬라이싱

print(a[0:4])
#0번에서 3번인덱스까지 슬라이싱하여 추출
#주의! 4번인덱스는 미포함임.
#즉 범위로 나타내면, 0 <= a < 4

#슬라이싱으로문자열나눠보기
b = "20230214Cloudy"

date = b[:8]
weather = b[8:]

print("날짜: " + date + "날씨: " + weather)

#포맷코드
# %s = string, %f = float , %c = char , %d = integer
# %s를 사용하면 뒤에 있는 값을 자동으로 문자열로 바꾸기때문에
# 자료형과 관계없이 편하게 사용할 수 있음!

c1 = input()
c = "ChatGPT is %s" %c1
print(c)