lista=[]


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
def validarX(wl, indice):
    if (wl[indice] == 'X'):
        return True
def asignandoList():
    global lista
    x = len(lista) - 1
    p = lista[x]
    d = list(p)
    return d
def marcar(w,i):
    global lista
    d = w[i]
    w[i] = '[' + d + ']'
    aux = w.copy()
    lista.append(aux)
    w[i] = d
    w[i] = 'X'
    aux = w.copy()
    lista.append(aux)
    w[i] = d

def indicador(w,i):
    global lista
    d = w[i]
    w[i] = '[' + d + ']'
    aux = w.copy()
    lista.append(aux)
    w[i] = d
    w[i] = '#'
    aux = w.copy()
    lista.append(aux)
    w[i] = d
def guardarW(w):
    indicador(w,0)
def render(i):
    global lista
    d=asignandoList()
    m = d[i]
    d[i] = '[' + m + ']'
    aux = d.copy()
    lista.append(aux)
    d[i] = m
    aux = d.copy()
    lista.append(aux)
    d[i] = m

def principal(w):
    global lista
    x=True
    c=1
    i=0
    #Se encuentra en un blanco
    guardarW(w)
    i=i+1
    #MOV_R buscando una a
    if(validarA(w,i)):
        #La encuentra y marca un blanco #
        indicador(w,i)
    else :
        #No la encuentra
        return lista, False
    i=i+1
    lista, x, c,i = nmayor(w,i,c)

    if(c==1):
        i = i + 1
        while(c==1):
            lista, x, c ,i= nmayor(w, i, c)
            if c==1:
                i=i+1
    if(c>1):
        return lista, False
    lista, i = desmarcandoX(i)
    lista, x = final(i)
    return lista, x

def nmayor(w,i,b):
    encuentra=True
    c=0
    #MOV_R buscando una a para n >0
    if (validarA(asignandoList(), i)):
        # La encuentra y marca un blanco #
        indicador(asignandoList(), i)
    else :
        #No la encuentra
        b=b-1
        return lista, False, b,i
    #Como hay una a debe aber b
    d=asignandoList()
    #MOV_R hasta encontrar un blanco
    while(c!=1):
        #+1 MOV_R
        i = i + 1
        render(i)
        if(blancoR(d,i)):
            # Se encuentra en un blanco
            indicador(d,i)
            c=1 #sale del ciclo

    #MOV_L hasta encontrar una a
    while (c != 0):
        i=i-1
        #+1 MOV_L
        render(i)
        if (validarA(asignandoList(),i)):
            # Se encuentra una a
            marcar(asignandoList(),i)
            c=0 #sale del ciclo
        if (blancoR(d,i)):
            #se encuentra un blanco quiere decir que no encontro a
            encuentra=False
    if(encuentra==False):
        b=b+1
        return lista,False, b,i
    # MOV_L buscando una b
    i=i-1
    if (validarB(asignandoList(), i)):
        # La encuentra y marca una X
        marcar(asignandoList(), i)
    else:
        # No la encuentra
        b = b + 1
        return lista, False, b,i
    # MOV_L buscando una a
    i = i - 1
    if (validarA(asignandoList(), i)):
        # La encuentra y marca una X
        marcar(asignandoList(), i)
    else:
        # No la encuentra
        b = b + 1
        return lista, False, b,i
    # MOV_L hasta encontrar un blanco
    while (c != 1):
        # +1 MOV_L
        i = i - 1
        render(i)
        if (blancoR(asignandoList(),i)):
            # Se encuentra en un blanco
            indicador(asignandoList(), i)
            c = 1  # sale del ciclo
    return lista, False, b,i

def desmarcandoX(i):
    global lista
    c=1
    while c!=0:

        if (validarX(asignandoList(), i)):
            # EncontroX
            indicador(asignandoList(), i)
            i = i + 1
        else :
            c=0

    return lista,i

def final(i):
    global lista
    if (validarC(asignandoList(), i)):
        indicador(asignandoList(),i)
    else:
        return lista, False
    i=i+1
    if (validarC(asignandoList(), i)):
        indicador(asignandoList(),i)
    else:
        return lista, False
    i=i+1
    if not(blancoR(asignandoList(), i)):
        return lista,False
    return lista, True