lista=[]
posicion=0
def agregar1(w,indice):
    global lista
    global posicion
    d=w[indice]
    #print(w)
    #print("+1")
    w[indice]='['+d+']'
    aux=w.copy()
    lista.append(aux)
    w[indice] = d
    w[indice]='#'
    aux=w.copy()
    lista.append(aux)
    w[indice] = d
    #print(lista)
def agregar(indice):
    global lista
    global posicion
    x=len(lista)-1
    p=lista[x]
    d=list(p)
    print(d)
    #print(w)
    print("+1")
    n=d[indice]
    d[indice]='['+n+']'
    aux=d.copy()
    lista.append(aux)
    d[indice] = n
    d[indice]='#'
    aux=d.copy()
    lista.append(aux)
    d[indice] = n
    #print(lista)

def renderR(w, indice):
    global lista
    x = len(lista) - 1
    p = lista[x]
    d = list(p)
    for i in range(indice,len(w)):
        n = d[i]
        d[i] = '[' + n + ']'
        aux = d.copy()
        lista.append(aux)
        d[i] = n
        if i==(len(w)-1):
          aux = d.copy()
          lista.append(aux)
          d[i] = n
    return len(w)-1

def renderL():
    global lista
    global posicion
    n=0
    x = len(lista) - 1
    p = lista[x]
    d = list(p)
    for i in range(posicion,5,-1):
        m = d[i]
        d[i] = '[' + m + ']'
        aux = d.copy()
        lista.append(aux)
        d[i] = m
        if i==6:
          aux = d.copy()
          lista.append(aux)
          d[i] = m

        n=i
    return n

def blancoR(wl, indice):
    if(wl[indice]=='#'):
        return True
def validarA(wl,indice):
    if(wl[indice]=='a'):
        return True
def validarB(wl, indice):
    if (wl[indice] == 'b'):
        return True

def validarC(wl, indice):
     if (wl[indice] == 'c'):
         return True

def paso1(wl,indice):
    global lista
    x=True
    #print(wl)
    if blancoR(wl,indice):
        agregar1(wl,indice)
        indice=indice+1
    else :
        return wl,False

    for i in range (0,6):
        if validarA(wl,indice):
            agregar(indice)
            indice=indice+1
            print("si")
        else:
            print("nu")
            return lista, False
    global posicion
    posicion=indice
    #print(wl)
    lista,x=paso2(wl,x)
    return lista, x

def paso2(w,x):
    global posicion
    global lista
    #print(w)
    #print("si3")
    i=renderR(w,posicion)
    if blancoR(w, i):
        #print("si2")
        #agregar( i)
        #print(lista)
        i=i-1
    else:
        return lista, False
    for c in range(0,2):
        #print("uwu")
        if validarC(w,i):
            agregar( i)
            i = i - 1
        else:
            return lista, False
    posicion=i
    lista, x = paso3(w, x)
    return lista, x

def paso3(w,x):
    global posicion
    #print(w)
    i=renderL()+1
    for c in range(0,5):
        if validarA(w,i):
            agregar( i)
            i=i+1
        else:
            return lista, False
        if validarB(w,i):
            agregar(i)
            i = i + 1
        else:
            return lista, False
        if validarA(w,i):
            agregar( i)
            i = i + 1
        else:
            return lista, False
    #print(lista)
    return lista ,x