name=raw_input("student's name: ")
course=raw_input("what course are you doing: ")
course_unit=raw_input("course_unit1: ")
grade=raw_input("what is the grade: ")
if grade==A:
	grade=5
if grade==B:
	grade=4
if grade==C:
	grade=3
if grade==D:
	grade=2
if grade==O:
	grade=1
if grade==F:
	grade="Failure"
if grade in range (5,0):
	print("equivalent for grade")
	A=5
	B=4
	C=3
	D=2
	O=1
	F=0
if grade in range(4,6):
	print("good performance")
elif grade in range(2,4):
	print("average score")
else:
	print("poor performance")

course_unit=raw_input("course_unit2: ")
grade=raw_input()
if grade in range (5,0):
	print("equivalent for grade")
	A=5
	B=4
	C=3
	D=2
	O=1
	F=0
if grade in range(4,6):
	print("good performance")
elif grade in range(2,4):
	print("average score")
else:
	print("poor performance")


course_unit=raw_input("course_unit3: ")
grade=raw_input()
if grade in range (5,0):
	print("equivalent for grade")
	A=5
	B=4
	C=3
	D=2
	O=1
	F=0
if grade in range(4,6):
	print("good performance")
elif grade in range(2,4):
	print("average score")
else:
	print("poor performance")

Overall_grade=sum()