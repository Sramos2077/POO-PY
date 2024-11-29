class Coffee:
    def __init__(self, name, taste, texture): #constructor
        #atributos
        self.name = name
        self.taste = taste
        self.texture = texture
    #Funciones    
    def Drink(self): #al no recibir nada la funcion, en los parentesis declaramos self haciendo referencia al objeto 
        print(f"you're drinking Coffee {self.name}")
    
    def Buy(self):
        print(f"you're buying coffee {self.name}")
            
coffee1 = Coffee('Espresso', 'intense and bitter', 'dense and creamy')
coffee2 = Coffee('American', 'soft', 'filtered')


#print(f'the Coffee is: {coffee1.name} its taste is: {coffee1.taste} and its texture is: {coffee1.texture}')
#print(f'the Coffee is: {coffee2.name} its taste is: {coffee2.taste} and its texture is: {coffee2.texture}')
coffee2.Buy()
coffee1.Drink()

    

