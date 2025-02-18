class Student:
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
        self.modules = { }

        self.average_mark = 0
        
    def add_module(self, module_id, module, mark):
        self.modules.update( {module_id:
            [module, mark] 
            })
        # Updates the average evertime a module is added
        self.calculate_average_mark()
        
    def calculate_average_mark(self):
        total_marks = 0
        number_of_marks = 0
        
        for module_key in self.modules.keys():
            total_marks += self.modules[module_key][1]
            number_of_marks += 1
            
        self.average_mark = total_marks / number_of_marks