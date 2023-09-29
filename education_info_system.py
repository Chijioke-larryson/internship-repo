educational_info_with_credentials = {}

def add_course():
    course_name = input("Enter the course name: ")
    course_description = input("Enter the course description: ")

    educational_info_with_credentials[course_name] = {
        "Description": course_description,
    }
    print("Course added successfully!")


def list_courses():
    if educational_info_with_credentials:
        print("List of Courses:")
        for course_name, course_data in educational_info_with_credentials.items():
            print(f"Course Name: {course_name}")
            print(f"Course Description: {course_data['Description']}")
            print("-" * 20)
    else:
        print("No courses found.")



while True:
    print("Educational Information Capturing System with Student Credentials")
    print("1. Add a Course")
    print("2. List Courses")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_course()
    elif choice == '2':
        list_courses()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
