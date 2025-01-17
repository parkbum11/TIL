import re

# 1. 문자열 판단하기

print('====#1====')
print(re.match('Hello', 'Hello, world!'))
print(re.match('Python', 'Hello, world!'))

# ^문자열 : 문자열이 맨 앞에 오는지 판단 / 문자열$ : 문자열이 맨 뒤에 오는지 판단(특정 문자열로 끝나는지)
# re.search : 문자열 일부분이 매칭되는지 판단

print(re.search('^Hello', 'Hello, world!'))
print(re.search('world!$', 'Hello, world!'))

# 문자열1|문자열2 : 특정 문자열에서 문자열1 또는 문자열2 중 하나라도 포함되는지 판단(OR 연산자와 개념이 비슷)

print(re.match('hello|world', 'hello'))


# 2. 범위 판단하기
print('\n====#2====')

# (1)문자열이 숫자로 되어있는지 판단
# []안에 숫자 범위 넣고 * 또는 +를 붙인다.
# [0-9]* : 0부터 9까지 숫자가 0개 이상 있는지
# [0-9]+ : 0부터 9까지 숫자가 1개 이상 있는지

print(re.match('[0-9]*', '1234'))
print(re.match('[0-9]+', '1234'))
print(re.match('[0-9]+', 'abcd'))

print(re.match('a*b', 'b')) # b에는 a가 0개 이상 있으므로 패턴에 매칭됨
print(re.match('a+b', 'b')) # b에는 a가 1개 이상 없으므로 패턴에 매칭되지 않음
print(re.match('a*b', 'aab')) # aab에는 a가 0개 이상 있으므로 패턴에 매칭됨
print(re.match('a+b', 'aab')) # aab에는 a가 1개 이상 있으므로 패턴에 매칭됨

# (2)문자가 한 개만 있는지 판단
# 문자? : 문자가 0개 또는 1개인지 판단
# 문자. : 문자가 1개인지 판단

print(re.match('H?', 'H')) # H 뒤에 문자가 0개 또는 1개 있으므로 패턴에 매칭됨
print(re.match('H?', 'Hi')) # H 뒤에 문자가 0개 또는 1개 있으므로 패턴에 매칭됨
print(re.match('H.', 'Hi')) #  H 뒤에 문자가 1개 있으므로 패턴에 매칭됨

# (3)문자 개수 판단하기
# 문자{개수} : 문자가 개수만큼 있는지
# (문자열){개수} : 문자열이 개수만큼 있는지

print(re.match('h{3}', 'hhhello'))
print(re.match('(hello){3}', 'hellohellohelloworld'))

# [0-9]{개수} : 0~9 범위 사이의 숫자가 개수만큼 있는지 확인
# (문자){시작개수,끝개수} : 문자가 시작개수~끝개수 범위 사이의 숫자 개수만큼 있는지 확인
# (문자열){시작개수,끝개수} : 문자열이 시작개수~끝개수 범위 사이의 숫자 개수만큼 있는지 확인
# [0-9]{시작개수,끝개수} : 0~9 범위 사이의 숫자가 시작개수~끝개수 범위 사이의 숫자 개수만큼 있는지 확인
# 시작개수와 끝개수 사이 붙어있어야 함

print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-1000'))
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-100'))
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-100-1000'))
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-10-1000'))

print(re.match('[a-zA-Z0-9]+', 'Hello1234')) # a~z, A~Z, 0~9까지 1개 이상 있는지
print(re.match('[a-zA-Z0-9]+', 'hello1234'))
print(re.match('[a-zA-Z0-9]+', '가나다'))