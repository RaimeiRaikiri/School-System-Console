class Module:
    
    def __init__(self, name, id):
        self.name =  name
        self.id = id  
              
        self.students = []
        
        self.average_marks = 0
        
    def add_student(self, student):
        self.students.append(student)
        
        # Updates the average evertime a student is added
        self.calculate_average_marks()
        
    def calculate_average_marks(self):
        totalMarks = 0
        
        for student in self.students:
            totalMarks += student.modules[self.id][1]
        if len(self.students) != 0:
            self.average_marks = totalMarks / len(self.students)
        
