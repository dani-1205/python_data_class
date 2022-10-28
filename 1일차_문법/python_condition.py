number = int(input())

if number < 5:
    print("숫자가 5보다 작습니다.")
elif 5 < number < 10:
    print("5보다 크고 10보다 작습니다.")
else:
    print("10보다 큽니다.")


# Q1. 일상 예제(1)
money = int(input())

if money == 70000:
    print("비행기 타기")
elif money == 50000:
    print("기차 타기")
elif money == 30000:
    print("버스 타기")
else:
    print("걸어가기")


for i in range(10):
    print("hello world")


countries = ["kor", "usa", "china"]
for country in countries:
    print(country)


for country in countries:
    if country == "kor":
        print("한글로 분석해주세요.")
    elif country == "usa":
        print("영어로 분석해주세요")
    elif country == "china":
        print("중국어로 분석해주세요")


a = 0
while a < 5:
    a += 1
    print(a)


# Q2. 1부터 5까지 더하는 프로그램을 만들어보시오.
# for 사용
total = 0
for i in range(1, 6):
    total += i
print(total)

# while 사용
total = 0
i = 1
while i <= 5:
    total += i
    i += 1
print(total)


for i in range(10):     # 0~9
    if 3<=i<=5:
        continue    # 반복문의 코드 처음으로 돌아간다.
    print(i)


for i in range(10):
    if 3<=i<=5:
        break
    print(i)