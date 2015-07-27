def open_file():
	file=open("C:\Users\User\Documents\python-tutorials\assignment4.txt", "r")
	data=file.readlines
	return data

name=raw_input("Name: ")
course=raw_input("Course: ")
Course_unit=raw_input("Course_unit 1: ")
grade=raw_input("Course_grade: ")
counter=0

def computed_grade(Course_grade):
	grade_value= None
	grade_list=["F", "O", "D", "C", "B", "A"]
	index=0
	for g in grade_list:
		index=index+1
		if user_grade == g:
			grade_value=index
		if grade_value== None:
			print("wrong grade; Please re-enter your grade")
			exam() 
		else:
			print ("Your grade value is : "+str(grade_value))
			return(grade_value)

def determining_performance (grade):
	if grade>=4:
		print("good performance")
	elif grade>=2 and grade <4:
		print ("average score")
	else:
		print("poor performance")

def exam():
	raw_grade = course()
	grade_value=computed_grade(raw_grade)
	determining_performance(grade_value)


