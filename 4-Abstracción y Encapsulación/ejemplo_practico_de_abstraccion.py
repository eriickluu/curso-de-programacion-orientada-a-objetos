class FilaBanco:
    usuarios = hash()

    def siguiente_usuario(self, numero):
        return self.usuarios.obtener(numero)

    def formar_usuario(self, numero, usuario):
        self.usuarios.agregar(numero, usuario)

class Hash():
    datos = {}

    def obtener(self, llave):
        datos[llave]

    def agregar(self, llave, valor):
        datos[llave] = valor

class Queue:
    def obtener(self):
        datos[0]

    def agregar(self, llave, valor):
        datos[len(datos)-1] = valor