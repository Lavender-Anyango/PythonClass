class Student:
    school = "Akirachix"

    def __init__(self, first_name, last_name, age, country, code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.code = code

    def greeting(self):
        greeting = f'Hello {self.first_name} , welcome to {self.school}, Your code is {self.code}'
        return greeting
    
    def year_of_birth(self):

        return f'Hello {self.first_name} you were born in {2024 - self.age}'
    
    def show_fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    def show_initials(self):
        pass
 
    def check_if_minor(self):
        pass
    
    def enroll_student(self):
        """enrolls student to a class"""