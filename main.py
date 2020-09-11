# Author: Cole Black-Stallard cdb5655@psu.edu
# Collaborator: N/A *Solo*

def getGradePoint(Gin):
  if Gin == "A":
    grade = "4.0"
  elif Gin == "A-":
    grade = "3.67"
  elif Gin == "B+":
    grade = "3.33"
  elif Gin == "B":
    grade = "3.0"
  elif Gin == "B-":
    grade = "2.67"
  elif Gin == "C+":
    grade = "2.33"
  elif Gin == "C":
    grade = "2.0"
  elif Gin == "D":
    grade = "1.0"
  else: 
    grade = "0.0"
  return grade 

def run():
  mark1  = input("Enter your course 1 letter grade: ")
  GPA1 = float(getGradePoint(mark1))
  C1 = float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {GPA1}.")

  mark2  = input("Enter your course 2 letter grade: ")
  GPA2 = float(getGradePoint(mark2))
  C2 = float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {GPA2}.")

  mark3  = input("Enter your course 3 letter grade: ")
  GPA3 = float(getGradePoint(mark3))
  C3 = float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {GPA3}.")

  GPA = (GPA1 * C1 + GPA2 * C2 + GPA3 * C3) / (C1 + C2 + C3)
  print(f"Your GPA is: {GPA}")

if __name__ == "__main__":
  run()