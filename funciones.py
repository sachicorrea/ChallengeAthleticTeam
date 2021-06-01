import math as m

lista_nombres=["Sergio","Willy","Ana","Lina","Benn","Julian","Sofia","Mario","Estefany","Pablo"]

lista_tiempos=[53.2, 104.9, 65.0, 771.2, 30.0, 83.3, 122.95, 154.1, 332.5, 341.6]

# Show athletic team list function
# casting lista_tiempos items
lista_tiempos_Mod = [str(x) for x in lista_tiempos]

def MostrarEquipoAtletismo():
  #Muestra el equipo de atletismo imprimiento en cada linea el nombre del atleta y su tiempo, ejemplo Sergio : 53.2
  for i in range(len(lista_nombres)):
    print(lista_nombres[i] + ' : ' + lista_tiempos_Mod[i])

# Function to insert a new athlete
def IngresarAtleta(nombre_nuevo_atleta, tiempo_nuevo_atleta):
  #Adiciona un nuevo atleta a la lista de nombres y la tiempo que corresponda a la lista de tiempos
  lista_nombres.append(nombre_nuevo_atleta)
  lista_tiempos.append(tiempo_nuevo_atleta)

  # Casting athlete time to string
  tiempo_nuevo_atleta = str(tiempo_nuevo_atleta)
  #print("Nombre : Tiempo")
  #print(nombre_nuevo_atleta + ' : ' + tiempo_nuevo_atleta)
  
def BuscarAtleta(nombre_atleta):
  #Busca al atleta por nombre, si lo encuentra retorna el nombre y tiempo. Sino retorna un mensaje "Atleta no encontrado"
  if nombre_atleta in lista_nombres:
    # Athlete index in lista_nombres
    indexAthlete = lista_nombres.index(nombre_atleta)
    # Index in lista_tiempos using indexAthlete
    timeAthlete = lista_tiempos[indexAthlete]

    print(nombre_atleta, " : " , timeAthlete)
  else:
    print("Atleta no encontrado")
  return

def EliminarAtleta(nombre_atleta):
  #Busca al atleta por nombre, si lo encuentra lo elimina de la lista de nombres y tiempos y retorna el mensaje "Atleta eliminado". Sino retorna un mensaje "Atleta no encontrado"
  if nombre_atleta in lista_nombres:
    indexAthlete = lista_nombres.index(nombre_atleta)

    # Delete name of athlete
    lista_nombres.pop(indexAthlete)

    # Delete time of athlete
    lista_tiempos.pop(indexAthlete)
  else:
    print("Atleta no encontrado")
  return

def EncontrarAtletaRapido():
  #Busca al atleta más rápido y retorna el mensaje nombre atleta : tiempo
  #Recuerde que el atleta más rapido es quien realizo el recorrido en el menor tiempo
  
  smallest = lista_tiempos[0] if lista_tiempos else None

  #Find the smalest number
  for i in lista_tiempos:
    if i < smallest:
      smallest = i

  #smallest = min(lista_tiempos)
  
  # Find index of the fastest athlete
  indexSmallest = lista_tiempos.index(smallest)

  # Find name onf the fastest one
  nameFastest = lista_nombres[indexSmallest]
  
  print(nameFastest, ":", smallest)
  return 
  
def EncontrarAtletaLento():
  #Busca al atleta más lento y retorna el mensaje nombre atleta : tiempo
  #Recuerde que el atleta más lento es quien realizo el recorrido en el mayor tiempo
  largest = lista_tiempos[0] if lista_tiempos else None

  #Find the smalest number
  for i in lista_tiempos:
    if i > largest:
      largest = i

  # Find index of the fastest athlete
  indexLargest = lista_tiempos.index(largest)

  # Find name onf the fastest one
  nameSlowest = lista_nombres[indexLargest]
  
  print(nameSlowest, ":", largest)
  return

def CalcularPromedio():
  #Calcula y retorna el promedio del equipo de atletismo
  sumList = sum(lista_tiempos)
  numberItems = len(lista_tiempos)

  #Calcula y retorna el promedio del equipo de atletismo
  avg = sumList / numberItems
  return print(avg)

def MostrarNombresAlfabeticamente():
  #Muestra los nombres del equipo de atletistmo ordenados alfabeticamente
  lista_nombres.sort()
  print(lista_nombres)

def MostrarEquipoVelocidadIncremental():
  #Muestra el nombres del atleta y la tiempo ordenados incrementalmente según la tiempo, es decir, primero el que menos tiempo tarda y ultimo el que mas tiempo tarda
  #TODO Implementar la función
  lista_tiempos.sort()
  print(lista_tiempos)

def GenerarSubEquipo(rango_minimo, rango_maximo):
  #Genera y muestra un subequipo incluyendo como integrantes los atletas que cumplan con el rango minimo y rango maximo definido. Muestra los atletas que hacen parte del subequipo en la forma nombre: tiempo

  filter_time = [x for x in lista_tiempos if rango_minimo < x < rango_maximo]
  print(filter_time)
