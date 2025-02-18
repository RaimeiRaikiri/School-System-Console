class System:
    
    def __init__(self):
        self.modules_list = []
        self.student_list = []
        
    def add_student(self, student):
        self.student_list.append(student)
        
    def add_module(self, module):
        self.modules_list.append(module)
        
    def find_module_object(self, module_id):
        for module in self.modules_list:
            if module.id == module_id:
                return module
        