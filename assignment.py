# 치환문 예

a = 1
b = a+1

print(a, b, sep=' , ')


# 한줄에 동시에 대입하고싶음
# 세미클론으로 치환문을 구분할 수 있다,
e = 3.5 ; f= 5.3
print(e, f)

# 여러 개를 한번에 치환하기
e, f = 3.5, 5.3

print(e,f) # packing unpacking이 일어나는 것

# 같은 값을 여러 변수에 대입
x = y = z = 10

# c 스타일은 지원 x
# x = (y=10) 같은

print(x,y,z)

# 동적 타이핑 : 변수에 새로운 값이 할당되면 값을 버리고 새로운 값으로 치환된다
a = 1 # 동적으로 type이 결정된다.   자바로는 Integer a= 1.

print(a, type(a))

a = 2
print(a, type(a)) # 위에 꺼랑 다른거다 위에 a는 가비지컬렉터가 삭제시킴, 그냥 이름테이블에서 a 쓰는 느낌

a = 'hello'
print(a, type(a))

# 확장 치환문
a = 10
a += 10 # a = a + 10

