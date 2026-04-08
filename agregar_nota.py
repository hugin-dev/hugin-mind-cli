import sqlite3
import os

conexion = sqlite3.connect("hugin_mind.db")
cursor = conexion.cursor()

def agregar_nota(cursor, conexion):

    continuar = True

    while continuar:


        concepto = input("Concepto: ").capitalize()
        categoria = input("Categoría: ").upper()
        definicion = input("Definición: ")
        ejemplo = input("Ejemplo: ")

        cursor.execute('''
                INSERT INTO notas(concepto, categoria, definicion, ejemplo)
                VALUES (?, ?, ?, ?)           
                ''', (concepto, categoria, definicion, ejemplo))
        
        conexion.commit()

        opcion = input("\n¿Quieres agregar otra nota? (s/n): ").lower()
        if opcion == 'n':
            continuar = False

def eliminar_nota(cursor, conexion):

    ver_notas(cursor)

    id_borrar = input("\n Ingresa el ID de la nota que quieres eliminar: ")

    #Ejecutar borrado
    cursor.execute("DELETE FROM notas WHERE id = ?",(id_borrar,))

    print("Nota eliminada de la constelación")

    input("\nPresiona Enter para volver al menú...")

    conexion.commit()

def aleatorio(cursor):

    # Seleccionamos una fila al azar desde la base de datos
    cursor.execute("SELECT concepto, definicion, ejemplo FROM notas ORDER BY RANDOM() LIMIT 1")
    nota = cursor.fetchone()

    if nota:
        print("\n" + "-"*30)
        print("RETO DE MEMORIA")
        print("-"*30)
        print(f"\nCONCEPTO: {nota[0]}")
        
        input("\nPresiona Enter para revelar la respuesta...")
        
        print(f"\nDEFINICION: {nota[1]}")
        print(f"EJEMPLO: {nota[2]}")
        print("\n" + "-"*30)
    else:
        print("\nLa base de datos esta vacia.")

    input("\nPresiona Enter para volver al menu...")

def ver_notas(cursor):

    #Ejecutar consulta
    cursor.execute("SELECT * FROM notas")

    #Obtener todos los resultados
    todas_las_notas = cursor.fetchall()

    #Validar si hay notas

    if not todas_las_notas:
        print("Aun no hay notas en tu constelación")
    else:
        print("\n--- TUS NOTAS ACTUALES ---")

        for nota in todas_las_notas:

            print(f"ID: {nota[0]} | {nota[1]} ({nota[2]})")
            print(f"Definición: {nota[3]}")
            print(f"Ejemplo: {nota[4]}")
            print("-" * 30)

    input("\nPresiona Enter para volver al menú...")
        

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n--- HUGIN-MIND: RECOLECTOR DE NOTAS ---")
    print("1. Agregar Nota")
    print("2. Ver notas")
    print("3. Reto Aleatorio")
    print("4. Eliminar nota")
    print("5. Salir")

    opcion = input("\n Selecciona una opcion: ")

    match opcion:
            case "1":
              agregar_nota(cursor=cursor, conexion=conexion)
            case "2":
                ver_notas(cursor=cursor)
            case "3":
                aleatorio(cursor=cursor)
            case "4":
                eliminar_nota(cursor=cursor, conexion=conexion)
            case "5":
                print("Hasta luego!")
                break
            case _:
                print("Opción no valida, intenta nuevamente.")


conexion.close()
