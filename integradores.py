def max_com_div(a,b):
    """
    Calcula el máximo común divisor entre dos número a y b
    """
    if (a<b):
        if (b%a==0):
            return (a)
        else:
            aux=int(a/2)
            for i in range(aux):
                if ((a%aux==0) and (b%aux==0)):
                    return (aux)
                else:
                    aux-=1
    else:
        if (a%b==0):
            return (b)
        else:
            aux=int(b/2)
            for i in range(aux):
                if ((a%aux==0) and (b%aux==0)):
                    return aux
                else:
                    aux-=1

def min_com_mul(a,b):
    """
    Calcula el mínimo común múltiplo
    """
    if (a<b):
        for i in range(1,a+1):
            if ((b*i)%a==0):
                return (b*i)
    else:
        for i in range(1,b+1):
            if ((a*i)%b==0):
                return (a*i)

#a=12
#b=18
#print(f"El máximo común divisor entre {a} y {b} es {max_com_div(a,b)}")
#print(f"El mínimo común múltiplo entre {a} y {b} es {min_com_mul(a,b)}")

def dic_palabras(cadena):
    """
    Devuelve un diccionario de palabras y veces que aparecen en la cadena 
    ingresada 
    """
    mi_dic = {}
    lista = cadena.split(" ")
    for ele in lista:
        if ele in mi_dic:
            mi_dic[ele]+=1
        else:
            mi_dic[ele]=1    
    return mi_dic

#una_cadena="la cosa es que cosa no es cosa es otra cosa"
#print(f"Diccionario de palabras repetidas de: {una_cadena} = {dic_palabras(una_cadena)}")

def mas_repetida(cadena):
    """
    Devuelve una tupla con la palabra con más frecuencia en la cadena, utilizando el 
    diccionario generado por la función definida anteriormente
    """
    mi_dic=dic_palabras(cadena)
    maximo=max(mi_dic, key=mi_dic.get)
    return (maximo, mi_dic[maximo])

#print(f"La palabra con más frecuencia en: {una_cadena}, es {mas_repetida(una_cadena)}")

def get_int():
    """
    Obtiene el valor entero ingresado por el usuario (se repite hasta obtener uno)
    """
    while True:
        valor=input("Ingrese un valor entero: ")
        try:
            valor_entero=int(valor)
            return valor_entero
        except:
            print("El valor ingresado no corresponde a un entero")

def get_int_r():
    """
    Obtiene el valor entero ingresado por el usuario (se repite hasta obtener uno recursivamente)
    """
    valor=input("Ingrese un valor entero: ")
    try:
        valor_entero=int(valor)
        return valor_entero
    except:
        print("El valor ingresado no corresponde a un entero")
        return get_int_r()

#print(get_int_r())

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

