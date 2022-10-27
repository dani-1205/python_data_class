def name(input):
    print("제 이름은 " + input + "입니다.")
name("다은")


def name():
    print("이름 함수 호출")
name()


def sum(a, b):
    return a + b    # return은 함수에서 output과 같은 역할을 함.

total = sum(3, 4)
print(total)


# Q1. 성적과 이름을 입력하고, 성적에 따른 등급을 알려주는 프로그램을 만드시오.
# 90점 이상 A등급
# 80점 이상 B등급
# 70점 이상 C등급
# 60점 이상 D등급
# 60점 미만 F등급

grade = ""
def result_grade(score, name):
	if score >= 90:
		print(name + " 학생은 A등급 입니다.")
	elif score >=80:
		print(name + " 학생은 B등급 입니다.")
	elif score >=70:
		print(name + " 학생은 C등급 입니다.")
	elif score >=60:
		print(name + " 학생은 D등급 입니다.")
	else:
		print(name + " 학생은 F등급 입니다.")

result_grade(100, "다은")