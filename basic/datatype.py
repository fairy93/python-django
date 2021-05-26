# *****************
# --- Data Type ---
# 21.05.26 기본 예제
# *****************
'''
Python has Five standard types
scalar
    Numbers : int, float, complex
    String : str
vector : List, Tuple, Dictionary, Set
hello = 'hello'
print(hello)
print(hello[0])
print(hello[2:5])
print(hello[2:])
'''
# List CRUD Example
ls = ['abcd', 786, 2.23, 'john', 70.2]
tinyls = [123, 'john']

# Create: ls 에 '100'을 추가 Create
ls.append('100')
print(ls)

# Read: ls 의 목록을 출력
print(ls)

# Update: ls와 tinyls 의 결합
ls = ls + tinyls
print(ls)

# Delete: ls 에서 786을 제거
ls.remove(786)

# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')

# Create: tp 에 '100'을 추가 Create
tp = tp + ('100',)
print(tp)

# Read: tp 의 목록을 출력
print(tp)

# Update: tp와 tinytp 의 결합
tp = tp + tinytp
print(tp)

# Delete: tp 에서 786을 제거
tp = list(tp)
tp.remove(786)
tp = tuple(tp)
print(tp)

# dictionary CRUD Example
dt = {'abcd': 786, 'john': 70.2}
tinydt = {'홍': '30세'}

# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
dt['tom'] = '100'
print(dt)

# Read: dt 의 목록을 출력
print(dt)

# Update: dt와 tinydt 의 결합
print('딕셔너리')
dt.update(tinydt)
print(dt)

# Delete: dt 에서 'abcd' 제거
dt.pop('abcd')
print(dt)
abc = 123
print(f"ddd'{abc}'")
