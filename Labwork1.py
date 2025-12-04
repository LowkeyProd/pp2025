def get_string_input(prompt):
    return input(prompt).strip()

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

students = {}
courses = {}
marks = {}

def select_from_list(prompt, items):
    for i, item in enumerate(items):
        print(f"{i + 1}. {item}")
    while True:
        choice_idx = get_int_input(prompt) - 1
        if 0 <= choice_idx < len(items):
            return choice_idx
        else:
            print("Invalid choice. Please try again.")

def input_data():
    num_students = get_int_input("Enter the number of students: ")
    for _ in range(num_students):
        student_id = get_string_input("Enter student ID: ")
        student_name = get_string_input("Enter student name: ")
        student_dob = get_string_input("Enter student date of birth: ")
        students[student_id] = {'name': student_name, 'dob': student_dob}

    num_courses = get_int_input("Enter the number of courses: ")
    for _ in range(num_courses):
        course_id = get_string_input("Enter course ID: ")
        course_name = get_string_input("Enter course name: ")
        courses[course_id] = {'name': course_name}

    print("\nSelect a course to input marks:")
    course_items = [f"{course_data['name']} ({course_id})" for course_id, course_data in courses.items()]
    course_choice_idx = select_from_list("Enter your choice: ", course_items)
    
    selected_course_id = list(courses.keys())[course_choice_idx]
    marks[selected_course_id] = {}
    print(f"\nEntering marks for course: {course_items[course_choice_idx]}")
    for student_id, student_data in students.items():
        mark = get_float_input(f"Enter mark for {student_data['name']} ({student_id}): ")
        marks[selected_course_id][student_id] = mark

def list_data():
    if not courses:
        print("\nNo courses to display.")
        return
    if not students:
        print("\nNo students to display.")
        return

    print("\nAvailable courses:")
    for course_id, course_data in courses.items():
        print(f"- {course_data['name']} ({course_id})")

    print("\nStudent list:")
    for student_id, student_data in students.items():
        print(f"- {student_data['name']} ({student_id}), DOB: {student_data['dob']}")

    print("\nSelect a course to view marks:")
    course_items = [f"{course_data['name']} ({course_id})" for course_id, course_data in courses.items()]
    course_choice_idx = select_from_list("Enter your choice (number): ", course_items)
    
    selected_course_id = list(courses.keys())[course_choice_idx]
    if selected_course_id in marks:
        print(f"\nMarks of {course_items[course_choice_idx]}:")
        course_marks = marks[selected_course_id]
        for student_id, student_data in students.items():
            mark = course_marks.get(student_id, "N/A")
            print(f"{student_data['name']} ({student_id}): {mark}")
    else:
        print("\nNo marks recorded for this course yet.")

def main():
    INPUT_DATA_CHOICE = '1'
    LIST_DATA_CHOICE = '2'
    EXIT_CHOICE = '3'

    while True:
        print("\n--- Student Mark Manager ---")
        print(f"{INPUT_DATA_CHOICE}. Input data (students, courses, marks)")
        print(f"{LIST_DATA_CHOICE}. List data (students, courses, marks)")
        print(f"{EXIT_CHOICE}. Exit")
        
        choice = get_string_input("Enter your choice: ")

        if choice == INPUT_DATA_CHOICE:
            input_data()
        elif choice == LIST_DATA_CHOICE:
            list_data()
        elif choice == EXIT_CHOICE:
            break
        else:
            print("Invalid choice. Re-enter")

if __name__ == "__main__":
    main()