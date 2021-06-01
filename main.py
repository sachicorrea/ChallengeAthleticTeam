"""
Autor del programa: Santiago Correa Restrepo
Nombre del reto: Equipo Atletismo
Grupo 
Fecha 31 Mayo-2021
"""""

import funciones as f
import math as m

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


def menuOpciones():
  bandera=0
  while(bandera == 0):
    print("\n ---------------EQUIPO DE ATLETISMO--------------- \n")
    print("Seleccione una opción: ")
    print("\n ...............................")
    print("1.Mostrar equipo de atletismo (1) ")
    print("...............................")
    print("2. Ingresar atleta (2) ")
    print("...............................")
    print("3. Buscar atleta por nombre (3) ")
    print("...............................")
    print("4. Eliminar atleta por nombre (4) ")
    print("...............................")
    print("5. Mostrar atleta más rapido (5) ")
    print("...............................")
    print("6. Mostrar atleta más lento (6) ")
    print("...............................")
    print("7. Mostrar el promedio del equipo de atletismo (7) ")
    print("...............................")
    print("8. Mostrar nombres de atletas ordenado alfabeticamente  (8) ")
    print("...............................")
    print("9. Mostrar equipo ordenado según tiempo de menor a mayor  (9) ")
    print("...............................")
    print("10. Generar subequipo por rangos de tiempo ")
    print("...............................")
    print("0. Salir ")
    print("\n .............OPCIONALES..................")
    print("11. Generar equipos automaticamente por categoria ALTA - MEDIA - BAJA (12) ")

    opcion = int(input("\n"))

    if(opcion == 1):
      # Show athletic team
      print("\n --- 1. Ver equipo de atletismo")
      f.MostrarEquipoAtletismo()
    
    elif(opcion == 2):
      print("\n --- 2. Ingresar atleta")
      nombre_nuevo_atleta = input("Ingrese nombre del atleta: ") 
      tiempo_nuevo_atleta = int(input("Ingrese tiempo del atleta:: "))

      # Casting athlete time to string
      tiempo_nuevo_atleta = str(tiempo_nuevo_atleta)

      f.IngresarAtleta(nombre_nuevo_atleta, tiempo_nuevo_atleta)

    elif(opcion == 3):
      print("\n --- 3. Buscar atleta por nombre")
      nombre_atleta = input("Ingrese nombre del atleta: ")

      f.BuscarAtleta(nombre_atleta)
    
    elif(opcion == 4):
      print("\n --- 4. Eliminar atleta por nombre")
      nombre_atleta = input("Ingrese nombre del atleta: ")

      f.EliminarAtleta(nombre_atleta)

    elif(opcion == 5):
      print("\n --- 5. Mostrar atleta más rapido")

      f.EncontrarAtletaRapido()

    elif(opcion == 6):
      print("\n --- 6. Mostrar atleta más lento")

      f.EncontrarAtletaLento()

    elif(opcion == 6):
      print("\n --- 6. Mostrar atleta más lento")

      f.EncontrarAtletaLento()
    
    elif(opcion == 7):
      print("\n --- 7. Mostrar el promedio del equipo de atletismo")
      f.CalcularPromedio()

    elif(opcion == 8):
      print("\n --- 8. Mostrar nombres de atletas ordenado alfabeticamente")
      f.MostrarNombresAlfabeticamente()

    elif(opcion == 9):
      print("\n --- 9. Mostrar equipo ordenado según tiempo de menor a mayor")
      f.MostrarEquipoVelocidadIncremental()
    
    elif(opcion == 10):
      print("\n --- 10. Generar subequipo por rangos de tiempo")

      rango_minimo = int(input("Ingrese rango mínimo: "))
      rango_maximo = int(input("Ingrese rango máximo: "))
      f.GenerarSubEquipo(rango_minimo, rango_maximo)

    #TODO Completar el codigo
    elif(opcion==0):
      bandera=1 

#RECUERDE QUE DEBE COMENTAR LA SIGUIENTE LINEA PARA EJECUTAR LOS TEST
menuOpciones()