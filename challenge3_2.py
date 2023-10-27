class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def get_student_data():
  student_list = []
  while True:
      name = input("Enter student name (or type 'done' to finish): ")
      if name.lower() == 'done':
          break
      roll_number = input("Enter student roll number: ")
      cgpa = float(input("Enter student CGPA: "))
      student = Student(name, roll_number, cgpa)
      student_list.append(student)
  return student_list

def sort_students(student_list):
  n = len(student_list)
  for i in range(n - 1):
      for j in range(0, n - i - 1):
          if student_list[j].cgpa < student_list[j + 1].cgpa:
              student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]

  return student_list

if __name__== "__main__":
  students = get_student_data()
  sorted_students = sort_students(students)
  print("\nSorted List of Students:")
  for student in sorted_students:
     print(f"Name:\t{student.name}\nRoll Number:{student.roll_number}\nCGPA:\t {student.cgpa}")