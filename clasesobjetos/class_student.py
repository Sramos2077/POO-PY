class student: #clase estudiante
    def __init__(self, name, age, grade): #constructor
        self.name = name 
        self.age = age
        self.grade = grade
    
    def study(self): #metodos de la clase
        print(f'{self.name} is studying')
    
count = 0 #contador de ciclo
name = input("writte your name: ")
age = input("writte your age: ")
grade = input("writte your grade of studies: ")

student1 = student(name, age, grade) #objeto o instancia de clase

print(f'name: {student1.name}, age: {student1.age}, grade: {student1.grade}')

while count != 3: #hasta que el contador llegue a 3 se cierra el ciclo
    actions = input("what actions do yo want to do: 1.(study) :")
    if(actions.lower() == "study"): #el metodo lower convierte el string en minuscula 
        student1.study()
        break
    else:
        print('try again')
        count += 1
if(count == 3):
    print('you got the limit of times')
