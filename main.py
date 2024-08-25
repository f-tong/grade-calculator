import os

average = 0
new = 0

def select_grading():
  grading = input("How was it graded? (percentage, fraction, level, letter) ")
  final_grading = grading.lower()
  if (final_grading == "percentage"):
    percent = input("Enter percentage (number only): ")
    try:
      mark = int(percent)
      return mark
    except ValueError:
      print("Please enter a number only. Try again.")
      get_assessment()
  elif (final_grading == "fraction"):
    try:
      out_of = float(input("Total marks: "))
    except ValueError:
      print("Please enter the total marks as a number only. Try again.");
      get_assessment();
    num = float(input("Your grade: "))
    mark = num / out_of * 100
    return mark
  elif(final_grading == "level" or final_grading == "letter"):
    grade = input("Enter grade: ").upper()
    if (grade == "R" or grade == "F"):
      mark = 0
      return mark
    elif (grade == "1-" or grade == "D-"):
      mark = 45
      return mark
    elif (grade == "1" or grade == "D"):
      mark = 50
      return mark
    elif (grade == "1+" or grade == "D+"):
      mark = 55
      return mark
    elif (grade == "2-" or grade == "C-"):
      mark = 60
      return mark
    elif (grade == "2" or grade == "C"):
      mark = 65
      return mark
    elif (grade == "2+" or grade == "C+"):
      mark = 70
      return mark
    elif (grade == "3-" or grade == "B-"):
      mark = 75
      return mark
    elif (grade == "3" or grade == "B"):
      mark = 80
      return mark
    elif (grade == "3+" or grade == "B+"):
      mark = 86
      return mark
    elif (grade == "4-" or grade == "A-"):
      mark = 91
      return mark
    elif (grade == "4" or grade == "A"):
      mark = 95
      return mark
    elif (grade == "4+" or grade == "A+"):
      mark = 98
      return mark
    else:
      print("Please enter a valid grade.")
      get_assessment()
  else:
    print("Please select one of: percentage, fraction, level, letter")
    get_assessment()

def calculate_weight():
  weight = int(input("What is its weight (percent number)? "))
  global new
  mark = weight * (new / 100)
  global average
  average += mark

def get_assessment():
  print()
  name = input("Enter assessment name: ")
  global new
  new = select_grading()
  grades_list[name] = new
  calculate_weight()
  answer = input("Do you have another assessment to input? ").lower()
  if (answer == "yes"):
    get_assessment()
  else:
    print()
    assessments = grades_list.keys()
    for a in assessments:
      print(a + " - " + str(grades_list[a]))
    print("Final grade: " + str(average))
    exit()


num_grades = 0

grades_list = {}

print("Welcome to the grade calculator!")
get_assessment()