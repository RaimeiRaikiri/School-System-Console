class System:
    
    def __init__(self):
        self.__modules_list = []
        self.__student_list = []
        
    def add_student(self, student):
        self.__student_list.append(student)
        
    def add_module(self, module):
        self.__modules_list.append(module)
        
    def find_module_object(self, module_id):
        for module in self.__modules_list:
            if module.get_id() == module_id:
                return module
    
    def get_modules_list(self):
        return self.__modules_list
    
    def get_students_list(self):
        return self.__student_list