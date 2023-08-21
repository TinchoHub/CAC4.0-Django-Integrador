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

a=12
b=18
print(f"El máximo común divisor entre {a} y {b} es {max_com_div(a,b)}")
print(f"El mínimo común múltiplo entre {a} y {b} es {min_com_mul(a,b)}")

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

una_cadena="la cosa es que cosa no es cosa es otra cosa"
print(f"Diccionario de palabras repetidas de: {una_cadena} = {dic_palabras(una_cadena)}")
