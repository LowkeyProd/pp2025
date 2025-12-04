class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student date of birth: ")
            self.students.append(Student(student_id, student_name, student_dob))

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            self.courses.append(Course(course_id, course_name))

    def input_marks(self):
        if not self.courses:
            print("\nNo courses available. Please input courses first.")
            return

        print("\nSelect a course to input marks:")
        for i, course in enumerate(self.courses):
            print(f"{i + 1}. {course.name} ({course.course_id})")

        course_choice = int(input("Enter your choice: ")) - 1
        if 0 <= course_choice < len(self.courses):
            selected_course = self.courses[course_choice]
            self.marks[selected_course.course_id] = {}
            print(f"\nEntering marks for course: {selected_course.name}")
            for student in self.students:
                mark = float(input(f"Enter mark for {student.name} ({student.student_id}): "))
                self.marks[selected_course.course_id][student.student_id] = mark
        else:
            print("Invalid course choice.")

    def list_courses(self):
        if not self.courses:
            print("\nNo courses to display.")
            return
        print("\nCourse list:")
        for course in self.courses:
            print(f"- {course.name} ({course.course_id})")

    def list_students(self):
        if not self.students:
            print("\nNo students to display.")
            return
        print("\nStudent list:")
        for student in self.students:
            print(f"- {student.name} ({student.student_id}), DOB: {student.dob}")

    def show_marks(self):
        if not self.courses:
            print("\nNo courses available.")
            return

        print("\nSelect a course to view marks:")
        for i, course in enumerate(self.courses):
            print(f"{i + 1}. {course.name} ({course.course_id})")

        course_choice = int(input("Enter your choice (number): ")) - 1
        if 0 <= course_choice < len(self.courses):
            selected_course = self.courses[course_choice]
            if selected_course.course_id in self.marks:
                print(f"\nMarks for {selected_course.name}:")
                course_marks = self.marks[selected_course.course_id]
                for student in self.students:
                    mark = course_marks.get(student.student_id, "N/A")
                    print(f"{student.name} ({student.student_id}): {mark}")
            else:
                print("\nNo marks recorded for this course.")
        else:
            print("Invalid course choice.")

def main():
    manager = MarkManager()
    while True:
        print("\n--- Student Mark Management ---")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks for a course")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.input_students()
        elif choice == '2':
            manager.input_courses()
        elif choice == '3':
            manager.input_marks()
        elif choice == '4':
            manager.list_courses()
        elif choice == '5':
            manager.list_students()
        elif choice == '6':
            manager.show_marks()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
