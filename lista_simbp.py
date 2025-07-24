def simBP(n:int, m:int) -> int:
    ''' Requiere: n>0, m>0
        Devuelve: la similitud binaria de prefijo entre n y m, definida como
        la longitud del prefijo común más largo entre las representaciones
        binarias de n y m. '''
    # Inicialización
    i:int=0 #  para iterar el ciclo while
    res:int=0 #  variable retorno
    # Transformacion de los parametros a binario
    num_binario_n:int=bin(n).replace('0b','') 
    num_binario_m:int=bin(m).replace('0b','')
    #Longitudes de los numeros binarios
    longitud_binario_n:int=len(num_binario_n)
    longitud_binario_m:int=len(num_binario_m)
    #ciclo para obtener la simbp
    while(i<longitud_binario_n and i<longitud_binario_m): 
        # si ambos tienen los mismos valores en su posicion i, res aumenta en 1
        if(num_binario_n[i]==num_binario_m[i]):
            res=res+1
        # en caso contrario, que es cuando se acaba la simbp, detemos el ciclo while
        else:
            i=longitud_binario_n # para que no se cumpla la condicion del while y acabe el ciclo
        i=i+1 
    return res

def lista_elementos_simBP_con_N(n:int, xs:list[int]) -> list[int]:
    """
    Requiere: n>0, xs con valores > 0
    Devuelve: una lista que contiene, en el mismo orden
    en que aparecen en xs, las simBPs entre n y cada
    uno de los elementos de xs
    """
    # Inicialización
    i:int=0
    vr:list[int]=[]
    #Longitud de la lista xs para usar en el ciclo
    longitud_xs:int=len(xs)
    while(i<longitud_xs):
        # Agregamos a vr la simbp entre n y los elementos de xs, en el orden pedido
        vr.append(simBP(n,xs[i])) #Llamado a la funcion auxiliar para sacar la simbp
        i=i+1
    return vr

