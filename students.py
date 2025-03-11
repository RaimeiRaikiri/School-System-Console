class Student:
    
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        
        self.__modules = { }

        self.__average_mark = 0
    
    def add_module(self, module_id, module, mark):
        self.__modules.update( {module_id:
            [module, mark] 
            })
        # Updates the average evertime a module is added
        self.calculate_average_mark()
        
    def calculate_average_mark(self):
        total_marks = 0
        number_of_marks = 0
        
        for module_key in self.get_modules().keys():
            total_marks += self.get_modules()[module_key][1]
            number_of_marks += 1
            
        self.__average_mark = total_marks / number_of_marks
        
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_modules(self):
        return self.__modules
    
    def get_average_mark(self):
        return self.__average_mark