def max_com_div(a,b):
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

print(max_com_div(12,18))