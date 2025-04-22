import json, students, modules, system


# Loads json information to main.py, returns the info as dictionaries
def read_files(module_file_name: str, students_file_name: str) -> tuple[dict, dict] | None:
    with open(f"{module_file_name}", "r") as open_file:
        modules_data_object = json.load(open_file)
    
    with open(f"{students_file_name}", "r") as open_file:
        students_data_object = json.load(open_file)
        
    return modules_data_object, students_data_object
    
def insert_modules_in_system(modules_data: dict, school_system: system) -> None:
    # Iterates over the dictionary keys (module names) and adds each module to the school system object
    for module_key in modules_data.keys():
        
        module = modules.Module(module_key, modules_data[module_key])
        school_system.add_module(module)
        
def insert_student_info_in_system(students_data: dict, school_system: system) -> None:
    for student_key in students_data.keys():
        
        student = students.Student(students_data[student_key]["name"], students_data[student_key]["student_id"])
        
        for module in students_data[student_key]["modules"]:
            
            module_mark = module["mark"]
            module_object = school_system.find_module_object(module["module_id"])
            student.add_module(module["module_id"], module_object, module_mark)
            module_object.add_student(student)
            
        school_system.add_student(student)
            
            
def find_a_students_modules(student_id: int, school_system: system) -> None:
    for student in school_system.get_students_list():
        
        if student.get_id() == student_id:
            print("Student name: ", student.get_name())
            print("Modules:")
            for module_key in student.get_modules().keys():
                print("-- Name: ", student.get_modules()[module_key][0].get_name(), "   Mark: ", student.get_modules()[module_key][1])
                

def find_students_in_module(module_id: int, school_system: system) -> None:
    for module in school_system.get_modules_list():
        
        if module.get_id() == module_id:
            print("Module name: ", module.get_name())
            for student in module.get_students_list():
                print("-- Student name: ", student.get_name(), " -- Mark: ", student.get_modules()[module_id][1])
      
def print_module_averages(school_system: system) -> None:
    for module in school_system.get_modules_list():
        module.calculate_average_marks()
        print("Module name: ", module.get_name(), "-- Average mark: ", module.get_average_marks())

    
def print_student_averages_recursive(school_system: system) -> None:
    student_list_length = len(school_system.get_students_list())
    
    recursive_loop(0, student_list_length, 1, school_system)

def recursive_loop(start, end, step, school_system: system):
    if step > 0 and start < end:
        loop_up(start, end, step, school_system)
    else: 
        return
    
# Only needs to loop up as there is only one instance of a recursive loop
# and the loop only needs to increase to iterate through an iterable obj
def loop_up(start, end, step, school_system: system):
    if start >= end:
        return 
    else:
        student = school_system.get_students_list()[start]
        print("Student name: ", student.get_name(), "-- Average mark: ", student.get_average_mark())
        loop_up(start + step, end, step, school_system)


        
        
        
        
# Executed code

# Holds student list and module list
school_system = system.System()

modData, studentData = read_files("modData.json", "studentData.json")

insert_modules_in_system(modData, school_system)
insert_student_info_in_system(studentData, school_system)



# Inputs

student_id = 90
module_id = 109

# Ouputs
print()
print("List modules for a student")
print()
find_a_students_modules(student_id, school_system)
print()
print("------------------------")
print()

print("Find all students in a module")
print()
find_students_in_module(module_id, school_system)
print()
print("------------------------")
print()

print("List of student average marks")
print()
print_student_averages_recursive(school_system)
print()
print("------------------------")
print()

print("List of module average marks")
print()
print_module_averages(school_system)
print()

