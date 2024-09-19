def add_student():
    name = input("Enter name of student: ")
    surname = input("Enter surname of student: ")
    age = int(input("Enter age of student: "))
    return {'name': name, 'surname': surname, 'age': age}
def remove_student(student_list):
    index = int(input("Enter the index of the student to remove: "))
    if 0 <= index < len(student_list):
        removed_student = student_list.pop(index)
        print(f"Removed student: {removed_student}")
    else:
        print("Invalid index. No student removed.")

def view_student_profile(student):


def main():
        groups = ['sca23', 'csc23', 'aco23', 'mar23']
        print("Available groups:")
        for i, group in enumerate(groups):
            print(f"{i}. {group}")
        student_info_list = [
            {'name': "Michael", 'surname': "Jackson", 'age': 35},
            {'name': "Mike", 'surname': "Johnson", 'age': 28}
        ]
        print("Existing students:")
        for n, info in enumerate(student_info_list):
            print(f"{n+1}) {info['name']} {info['surname']} ({info['age']} years old)")
        add_new_student = input("Do you want to add a new student? (yes/no): ").lower()
        if add_new_student.lower().startswith('y'):
            new_student = add_student()
            student_info_list.append(new_student)
        print("Existing students:")
        for n, info in enumerate(student_info_list):
            print(f"{n}) {info['name']} {info['surname']} ({info['age']} years old)")
        remove_existing_student = input("Do you want to remove a student? (yes/no): ").lower()
        if remove_existing_student.lower().startswith('y'):
            remove_student(student_info_list)
        print("Existing students:")
        for n, info in enumerate(student_info_list):
            print(f"{n+1}) {info['name']} {info['surname']} ({info['age']} years old)")
if __name__ == "__main__":
    main()