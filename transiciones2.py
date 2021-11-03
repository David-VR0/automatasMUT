lista=[]
posicion=0
cantidad=0
estado=0
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
    d=asignandoList()
    #print(d)
    #print(w)
    #print("+1")
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

def render(i):
    global lista
    d=asignandoList()
    # print(w)
    # print("+1")
    m = d[i]
    d[i] = '[' + m + ']'
    aux = d.copy()
    lista.append(aux)
    d[i] = m
    aux = d.copy()
    lista.append(aux)
    d[i] = m
    # print(lista)

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
    global cantidad
    x=True
    n=0
    #print(wl)
    if blancoR(wl,indice):
        agregar1(wl,indice)
        indice=indice+1
        #print("hola")
    else :
        return wl,False
    while n!=2:
        if validarA(wl,indice):
            agregar(indice)
            indice=indice+1
            n=1
            cantidad= cantidad + 1
        elif n==1:
            n=2
        else :
            return lista, False
    global posicion
    posicion = indice
    lista, x = paso2(wl, x)
    return lista, x

def paso2(w,x):
    global posicion
    global lista
    global cantidad
    global estado
    n=0

    while n!=2:
        render(posicion)
        if blancoR(w, posicion):
            agregar(posicion)
            n=2
        if n!=2:
            posicion=posicion + 1
    posicion=posicion-1
    #print("c")
    while n!=0:
        if validarC(w,posicion):
            agregar(posicion)
            n=n-1
            posicion=posicion-1
            estado=estado+1
        elif n==2:
            return lista,False
        else :
            return lista , False
    #print(estado)
    if(estado==2):
        lista, x = paso3(w,x)
    if x==False and estado==2 and cantidad==1:
        return lista, True
    if x==True and estado==1:
        return lista, False
    return lista, x

def paso3(w,x):
    global posicion
    global cantidad
    global estado
    n=1
    y=0
    #print("----")
    d=asignandoList()
    while n!=2:
        render(posicion)
        if blancoR(d, posicion):
            agregar(posicion)

            n = 2
        if n != 2:
            posicion = posicion - 1
    posicion=posicion+1
    while n!=0:
        n=3
        d = asignandoList()
        if validarB(d,posicion):
            agregar(posicion)
            n=2
            posicion=posicion+1
        else:
            return lista, False
        if validarA(d,posicion):
            y = y + 1
            agregar(posicion)
            n=1
            posicion=posicion+1
        else:
            return lista, False
        if(y==cantidad-2) and validarA(d,posicion):
            estado=2
            continue
        if validarA(d,posicion):
            agregar(posicion)
            n=1
            posicion=posicion+1
        elif n==1:
            n=0
        if(y)>(cantidad - 2):
            estado=0

            return lista, False

    return lista, x

def asignandoList():
    global lista
    x = len(lista) - 1
    p = lista[x]
    d = list(p)
    return d