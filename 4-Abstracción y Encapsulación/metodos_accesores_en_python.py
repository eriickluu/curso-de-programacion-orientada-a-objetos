class Usuario:
    __edad = 0

    def __init__(self, nombre):
        self._nombre = nombre

    def saludar(self, saludo):
        print(saludo + self._nombre)

    # Getter
    @property 
    def edad(self):
        return self.__edad

    # Setter
    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError('Edad no puede ser menor a 0')
        self.__edad = valor
        

class Empleado(Usuario):
    __salario = 0

    # Setter
    def modificar_salario(self, salario):
        self.__salario = salario

    # Getter
    def ver_salario(self):
        print(self.__salario)

    def saludar(self):
        print("Mi nombre es: " + self._nombre + "y ganó: " + str(self.__salario))

empleado = Empleado("Erick")

empleado.edad = 26

print(empleado.edad)




