class Usuario:
    def __init__(self, nombre):
        # Protegidos
        self._nombre = nombre

    def saludar(self, saludo):
        print(saludo + self._nombre)

class Empleado(Usuario):
    # Privados
    __salario = 0

    def modificar_salario(self, salario):
        self.__salario = salario

    def ver_salario(self):
        print(self.__salario)

    def saludar(self):
        print("Mi nombre es: " + self._nombre + "y ganó: " + str(self.__salario))

# class Administrativo(Empleado):

#     def mi_salario(self):
#         print(self.___salario)

empleado = Empleado("Erick")

empleado.modificar_salario(1000)

empleado.ver_salario()

# admin = Administrativo("Erick")

# admin.ver_salario()