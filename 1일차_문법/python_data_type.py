x = "python"
x = 123
x = "123"
x = [1, 2, 3, 4]
x = {"name":"daeun", "age":"23"}
x = True
print(type(x))


a = 1 + 1
a = 100 - 1
a = 12 * 12
a = 3 / 4
print(a)


a = "Act as though \nit is impossible to fail"
print(a)

a = """Act as though
it is impossible to fail"""
print(a)



# Q1. 문장 그대로 표현하기
a = '"Failure is simply the opportunity to begin again." he says."'
a = """ "Failure is simply the opportunity to begin again." he says." """
a = "\"Failure is simply the opportunity to begin again.\" he says.\""
print(a)



a = "A"
print(a*10)


c = "hello python!"
print(len(c))
print(c[0]) #indexing -> 하나만 지정
print(c[0:5]) #slicing, 0 <= c < 5 -> 범위를 지정
print(c[6:])
print(c[:])



# Q2. "Titanic James" 변수를 영화제목(title)과 감독(director)으로 슬라이싱 해보세요.
x = "TitanicJames"
title = print(x[:7])
director = print(x[7:])



a = ["a", "b", "c", "d", "e"]
a = ["a", "b", ["c", "d", "e"]]
print(a[1])
print(a[2][1])


t = ("a", "a", "a", "b")
print(type(t))

 
x = {"key1":"value1", "key2":"value2"}
print(x["key2"])


x = set([1, 1, 1, 2])
print(x)    # 중복을 없애줌