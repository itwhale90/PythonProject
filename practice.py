# 형변환
int_v = '2'
print(int(int_v) + 2)

str_v = 4
print(str(str_v) + "개")
print(int(float('3.14')))

# 논리 연산자
print(3 < 5 and 7 < 5) # AND
print(3 < 5 or 7 < 5) # OR
print(not 3 < 5) # NOT (반전)

# 멤버 연산자
print('c' in 'cat') # IN (포함)
print('c' not in 'cat') # NOT IN (미포함)


# 인덱스와 슬라이싱
# 인덱스
lang = 'PYTHON'
print(lang[0])
print(lang[5]) # print(lang[-1])
print(lang[4:]) # 4부터 끝까지

