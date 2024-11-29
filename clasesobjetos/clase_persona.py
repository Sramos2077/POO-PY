#clase para crear personas sims
class Sim:
    #constructor
    def __init__(self, color, height, age, country):
        self.color = color
        self.height = height
        self.age = age
        self.country = country
    #Metodos, siempre en cada metodo debemos poner self referenciando al objeto creado de la clase
    def talk(self):
        print("talking about a topic")
    
    def walking(self):
        print("walking in a street")
    
    def sleep(self):
        print("sleeping zzz")
    
    def eat(self):
        print("eating a bacon")

#instancia o objeto
sergio = Sim('white', 1.87, 20, 'spain')

sergio.sleep()
sergio.eat()