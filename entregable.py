class Persona:
    """
    Clase Persona con atributos de Nombre, Edad y DNI. Métodos Getters y Setters y un mostrar 
    """
    def __init__(self, nuevo_nombre = "", nueva_edad = 0, nuevo_DNI = 0):
        self._nombre = nuevo_nombre
        try:
            self._edad = int(nueva_edad)
            if ((nueva_edad<0) or (nueva_edad>120)):
                print("Edad inválida, deberá volver a setearla luego")
                self._edad = 0
        except:
            self._edad = 0
            print("Edad inválida, deberá volver a setearla luego")
        try:
            self._DNI = int(nuevo_DNI)
            if ((nuevo_DNI<100000) or (nuevo_DNI>100000000)):
                print("DNI inválido, deberá volver a setearlo luego")
                self._DNI = 0
        except:
            self._DNI = 0
            print("DNI inválido, deberá volver a setearlo luego")
    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad
    @property
    def DNI(self):
        return self._DNI
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre=nuevo_nombre
    @edad.setter
    def edad(self, nueva_edad):
        try:
            self._edad = int(nueva_edad)
            if ((nueva_edad<0) or (nueva_edad>120)):
                print("Edad inválida, deberá volver a setearla luego")
                self._edad = 0
        except:
            self._edad = 0
            print("Edad inválida, deberá volver a setearla luego")
    @DNI.setter
    def DNI(self, nuevo_DNI):
        try:
            self._DNI = int(nuevo_DNI)
            if ((nuevo_DNI<100000) or (nuevo_DNI>100000000)):
                print("DNI inválido, deberá volver a setearlo luego")
                self._DNI = 0
        except:
            self._DNI = 0
            print("DNI inválido, deberá volver a setearlo luego")
        
    def mostrar(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, DNI: {self._DNI}")

    def es_mayor_de_edad(self):
        return (self._edad>=18)


class Cuenta(Persona):
    """
    Clase Cuenta con los atributos: titular de clase Persona y cantidad.
    Métodos: mostrar, ingresar y retirar
    """
    def __init__(self, nuevo_nombre, nueva_edad, nuevo_dni, nueva_cantidad = 0):
        super().__init__(nuevo_nombre, nueva_edad, nuevo_dni)
        self._cantidad = nueva_cantidad

    def mostrar(self):
        super().mostrar()
        print(f"Cantidad: {self._cantidad}")

    def ingresar(self, monto):
        if (monto>0):
            self._cantidad+=monto

    def retirar(self, monto):
        self._cantidad-=monto
    
class CuentaJoven(Cuenta):
    """
    Clase CuentaJoven hereda de Cuenta y agrega atributo de bonificación.
    Nuevo método es_titular_valido y agregado a mostrar
    """
    def __init__(self, nuevo_nombre, nueva_edad, nuevo_dni, nueva_cantidad, nueva_bonificacion):
        super().__init__(nuevo_nombre, nueva_edad, nuevo_dni, nueva_cantidad)
        self._bonificacion = nueva_bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, nueva_bonificacion):
        self._bonificacion=nueva_bonificacion
    
    def es_titular_valido(self):
        return ((self._edad>18) and (self._edad<25))
    
    def retirar(self, monto):
        if (self.es_titular_valido()):
            super().retirar(monto)

    def mostrar(self):
        print("* Cuenta Joven *")
        super().mostrar()
        print(f"Bonificación: {self._bonificacion}")

persona1 = Persona("Juan",36,31546879)
persona1.mostrar()
persona1.nombre = "Juan Perez"
persona1.edad = 39
persona1.DNI = 41202303
persona1.mostrar()
print(f"Nombre: {persona1.nombre}, edad: {persona1.edad}, DNI: {persona1.DNI}")

cuenta1 = Cuenta("Maria",45,21345678,3500)
cuenta1.mostrar()
cuenta1.ingresar(2000)
cuenta1.mostrar()
cuenta1.retirar(8000)
cuenta1.mostrar()

cuentajoven1 = CuentaJoven("Pepe",25,35264548,1500,25)
cuentajoven1.mostrar()
print(cuentajoven1.es_titular_valido())
cuentajoven1.retirar(100)
cuentajoven1.mostrar()
cuentajoven1.edad = 24
print(cuentajoven1.es_titular_valido())
cuentajoven1.retirar(100)
cuentajoven1.mostrar()