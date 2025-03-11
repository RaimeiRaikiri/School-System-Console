class Module:
    
    def __init__(self, name, id):
        self.__name =  name
        self.__id = id  
              
        self.__students = []
        
        self.__average_marks = 0
        
    def add_student(self, student):
        self.__students.append(student)
        
        # Updates the average evertime a student is added
        self.calculate_average_marks()
        
    def calculate_average_marks(self):
        totalMarks = 0
        
        for student in self.get_students_list():
            totalMarks += student.get_modules()[self.get_id()][1]
        if len(self.get_students_list()) != 0:
            self.__average_marks = totalMarks / len(self.get_students_list())
        
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_average_marks(self):
        return self.__average_marks
    
    def get_students_list(self):
        return self.__students