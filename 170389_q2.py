class Student:
    def _init_(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' added with grade {grade} for {self.name}.")

    def display_grades(self):
        if self.assignments:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f"  - {assignment}: {grade}")
        else:
            print(f"{self.name} has no assignments yet.")


class Instructor:
    def _init_(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) added to {self.course_name}.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"No student found with ID {student_id}.")

    def display_all_students_grades(self):
        if self.students:
            print(f"Grades for all students in {self.course_name}:")
            for student in self.students:
                student.display_grades()
        else:
            print("No students in the course.")