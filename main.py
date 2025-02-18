import json, students, modules, system


# Loads json information to main.py
def read_files(module_file_name, students_file_name):
    with open(f"{module_file_name}", "r") as openFile:
        modules_data_object = json.load(openFile)
    
    with open(f"{students_file_name}", "r") as openFile:
        students_data_object = json.load(openFile)
        
    return modules_data_object, students_data_object
    
def insert_modules_in_system(modules_data: dict):
    for module_key in modules_data.keys():
        
        module = modules.Module(module_key, modules_data[module_key])
        school_system.add_module(module)
        
def insert_student_info_in_system(students_data):
    for student_key in students_data.keys():
        
        student = students.Student(students_data[student_key]["name"], students_data[student_key]["student_id"])
        
        for module in students_data[student_key]["modules"]:
            
            module_mark = module["mark"]
            module_object = school_system.find_module_object(module["module_id"])
            student.add_module(module["module_id"], module_object, module_mark)
            module_object.add_student(student)
            
        school_system.add_student(student)
            
            
def find_a_students_modules(student_id):
    for student in school_system.student_list:
        
        if student.id == student_id:
            print("Student name: ", student.name)
            print("Modules:")
            for module_key in student.modules.keys():
                print("-- Name: ", student.modules[module_key][0].name, "   Mark: ", student.modules[module_key][1])
                

def find_students_in_module(module_id):
    for module in school_system.modules_list:
        
        if module.id == module_id:
            print("Module name: ", module.name)
            for student in module.students:
                print("-- Student name: ", student.name, " -- Mark: ", student.modules[module_id][1])
      
def print_module_averages():
    for module in school_system.modules_list:
        module.calculate_average_marks()
        print("Module name: ", module.name, "-- Average mark: ", module.average_marks)

    
def print_student_averages_recursive():
    student_list_length = len(school_system.student_list)
    
    recursive_loop(0, student_list_length, 1)

def recursive_loop(start, end, step):
    if step > 0 and start < end:
        loop_up(start, end, step)
    else: 
        return
    
# Only needs to loop up as there is only one instance of a recursive loop
# and the loop only needs to increase 
def loop_up(start, end, step):
    if start >= end:
        return 
    else:
        student = school_system.student_list[start]
        print("Student name: ", student.name, "-- Average mark: ", student.average_mark)
        loop_up(start + step, end, step)


        
        
        
        
# Executed code

# Holds student list and module list
school_system = system.System()

modData, studentData = read_files("modData.json", "studentData.json")

insert_modules_in_system(modData)
insert_student_info_in_system(studentData)



# Inputs

student_id = 90
module_id = 109

# Ouputs
print()
print("List modules for a student")
print()
find_a_students_modules(student_id)
print()
print("------------------------")
print()

print("Find all students in a module")
print()
find_students_in_module(module_id)
print()
print("------------------------")
print()

print("List of student average marks")
print()
print_student_averages_recursive()
print()
print("------------------------")
print()

print("List of module average marks")
print()
print_module_averages()
print()

