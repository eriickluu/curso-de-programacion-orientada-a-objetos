class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self, saludo):
        print(saludo + self.nombre)
        

erick = Usuario()

erick.saludar("Mi nombre es: ")
