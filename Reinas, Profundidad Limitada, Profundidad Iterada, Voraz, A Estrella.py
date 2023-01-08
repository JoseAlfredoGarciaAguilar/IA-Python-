import sys  # Libreria
sys.setrecursionlimit(10000)  # n de profundidad de la pila


def calculo_Ataque(lista):
    n = len(lista)
    ataques = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (lista[i] == lista[j]):  # Verifica si hay ataque de manera hori o vertica
                ataques += 2
            elif ((abs(i-j)) == (abs(lista[i] - lista[j]))):
                ataques += 2
    return ataques


def goalTest(lista):
  return calculo_Ataque(lista) == 0


def expand(estadoAct):  # Expande todos los caminos posibles de ataques
    n = len(estadoAct)
    descendientes = []
    for i in range(n):
        auxiliar = list(estadoAct)
        valor_posicion = estadoAct[i]
        if valor_posicion < n:
            valor_posicion += 1
            auxiliar[i] = valor_posicion
            descendientes.append(auxiliar)
        else:
            return []
    return descendientes


def B_A(frontera):  # Busqueda a lo Ancho
    estadoAct = frontera.pop(0)
    if (estadoAct == None):
        return "Solucion no encontrada"
    if goalTest(estadoAct):
        print("Solucion encontrada en Busqueda a lo Ancho: ", estadoAct)
        return True
    else:
        offSpring = expand(estadoAct)
        for element in offSpring:
            frontera.append(element)
    B_A(frontera)


B_A([[1, 1, 1, 1]])


def B_P(frontera):  # Busqueda a lo Profundidad
    estadoAct = frontera.pop(0)
    if (estadoAct == None):
        return "Solucion no encontrada"
    if goalTest(estadoAct):
        print("Solucion encontrada en Busqueda a lo Profundo: ", estadoAct)
        return True
    else:
        offSpring = expand(estadoAct)
        offSpring.reverse
        for element in offSpring:
            frontera.insert(0, element) 
    B_P(frontera)


B_P([[1, 1, 1, 1]])


def B_P_Lim(frontera,n):  # Busqueda a lo Profundidad Limitada
  if len(frontera)==0:
    return None
  estadoAct=frontera[0][0]
  valor_posicion=frontera[0][1]
  while not goalTest(estadoAct):
    del frontera[0]
    if valor_posicion<n:
      offSpring=expand(estadoAct)
      offSpring.reverse
      for element in offSpring:
        frontera.insert(0, [element, valor_posicion+1])
    if len(frontera) == 0:
        return None
    estadoAct=frontera[0][0]
    valor_posicion=frontera[0][1]
  
  return frontera[0][0]

B_P_Lim([[[1,1,1,1], 0]], 6)

def B_P_Iter(): # Busqueda a lo Profundidad Iterada
  n=2
  termina=True
  while(termina):
    frontera= [[[1,1,1,1], 0]]
    if(B_P_Lim(frontera, n)==None):
      print("Solución no encontrada en el Nivel numero", n)
      n+=2
    else:
      termina=False
      return B_P_Lim(frontera, n),"Nivel: ",n 

frontera= [[[1,1,1,1], 0]]
print(B_P_Iter())

def B_Voraz(frontera):
    estadoAct = frontera.pop(0)
    frontera = srt(frontera.pop())

    if goalTest(estadoAct):
        print("Solución encontrada")
    else:
        offSpring = expand(estadoAct)
        offSpring = Evaluar(offSpring)
        offSpring = sort(offSpring)
        frontera = first(offSpring)
        
B_Voraz(frontera)


def A_Star(frontera):
    if frontera == null:
        
    else
    estadoAct = frontera.pop(0)

    if goalTest(estadoAct)
    else
    offSpring = expand()
    offSpring = Evaluar(offSpring)
    frontera = append(frontera, offSpring)
    frontera = sort(frontera)

A_Star(frontera)
