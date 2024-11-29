import random
import time


class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
    
    def hablar(self):
        topic = random.randint(1, 5)
        if(topic == 1):
            print(f'{self.nombre} esta hablando de baseball')
        elif(topic == 2):
            print(f'{self.nombre} esta hablando de programacion')
        elif(topic == 3):
            print(f'{self.nombre} esta hablando de animes por estrenarse')
        elif (topic == 4):
            print(f'{self.nombre} esta hablando de videojuegos')
        elif(topic == 5):
            print(f'{self.nombre} esta hablando de autos')
            
    def dormir(self):
        horas_de_dormir = [10, 11, 12, 1, 2, 3 ,4 ,5 ,6]
        turno = ['am', 'pm']
        hora =  random.choice(horas_de_dormir)
        turno_random = random.choice(turno)
        print(f'{self.nombre} se durmio a las {hora}:00 {turno_random}')
        
    def despertar(self):
        horas_de_despertar = [10, 11, 12, 1, 2, 3 ,4 ,5 ,6]
        turno = ['am', 'pm']
        turno_random = random.choice(turno)
        hora =  random.choice(horas_de_despertar)
        print(f'{self.nombre} se desperto a las {hora}:00 {turno_random}')
        
    def comer(self):
        comidas = ['ensalada', 'huevo con papas', 'carne asada', ' hamburgesa', 'pizza', 'guisado']
        platillos = random.choice(comidas) 
        print(f'{self.nombre} esta comiendo {platillos}')

class programador(Persona):
    def __init__(self, nombre, edad, pais, rol, lenguaje_de_prgramacion_favorito):
        Persona.__init__(self, nombre, edad, pais)
        self.rol = rol
        self.lenguaje_de_programacion_favorito = lenguaje_de_prgramacion_favorito
    
    def codificar(self):
        print(f'{super().nombre} en el area de {self.rol} programando en {self.lenguaje_de_programacion_favorito}')

