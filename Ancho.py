grafo = {'Oradea': ['Zerind','Sibiu'],
          'Zerind': ['Arad','Oradea'],
		  'Sibiu': ['Oradea','Arad','Rimnicu Vilcea','Fagaras'],
		  'Arad': ['Zerind','Sibiu','Timisoara'],
		  'Timisoara': ['Arad','Lugoj'],
		  'Lugoj': ['Timisoara','Mehadia'],
		  'Mehadia': ['Lugoj','Dobreta'],
		  'Dobreta': ['Mehadia','Craiova'],
		  'Craiova': ['Dobreta','Rimnicu Vilcea','Pitesti'],
		  'Rimnicu Vilcea': ['Sibiu','Pitesti','Craiova'],
		  'Fagaras': ['Sibiu','Bucarest'],
		  'Pitesti': ['Rimnicu Vilcea','Craiova','Bucarest'],
		  'Bucarest': ['Fagaras','Pitesti','Giurgiu','Urziceni'],
		  'Giurgiu': ['Bucarest'],
		  'Urziceni': ['Bucarest','Vaslui','Hirsoya'],
		  'Hirsoya': ['Eforie','Urziceni'],
		  'Eforie': ['Hirsoya'],
		  'Vaslui': ['Urziceni','lasi'],
		  'lasi': ['Vaslui','Neami'],
		  'Neami': ['lasi']}

estado_inicial = input("Ingresa el nodo origen: ")
meta = input("Ingresa el nodo destino: ")
frontera = [estado_inicial]
ruta = []
visitados = []


def B_A(frontera):
  estado_actual = frontera.pop(0)
  if estado_actual not in visitados:
    visitados.insert(0,estado_actual)
    if(estado_actual == meta):
     print("Terminado")
    else:
     for key in grafo[estado_actual]:
      frontera.append(key) 
     B_A(frontera)
  else:
    B_A(frontera)


B_A(frontera)
print(visitados)