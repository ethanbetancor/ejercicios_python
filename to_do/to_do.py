from datetime import datetime
import os
import json

tareas = []
seguir = True

if os.path.exists("file.json"):
    with open("file.json", "r") as f:
        tareas = json.load(f)
else:
    with open("file.json", "w") as f:
        json.dump([], f)

def añadir_actividad():
    ok = False
    while not ok:
        id = input("Seleccione un id: ")
        descripcion = input("Escriba una breve descripción: ")
        fecha = datetime.now().strftime("%d/%m a las %H:%M")
        
        if any(t["id"] == id for t in tareas):
            print("El id ya existe, prueba con otro")
        else:
            tareas.append({"id": id, "descripcion": descripcion, "fecha": fecha})
            print("Actividad añadida correctamente")
            ok = True

def eliminar_actividad():
    borrar = input("Dime el id de la actividad que desees eliminar: ")
    for i, tarea in enumerate(tareas):
        if tarea["id"] == borrar:
            del tareas[i]
            print("Actividad eliminada")
            return
    print("No se encontró ninguna actividad con ese id")

def mostrar_actividades():
    if not tareas:
        print("No hay actividades registradas")
    else:
        for tarea in tareas:
            print(f"ID: {tarea['id']} | Descripción: {tarea['descripcion']} | Fecha: {tarea['fecha']}")
            
def guardar():
    with open("file.json", "w") as f:
        json.dump(tareas, f, indent=4)
    print("Actividades guardadas correctamente.")

while seguir:
    print("\nBienvenido a tu gestor de actividades")
    print("1) Añadir actividad")
    print("2) Borrar actividad")
    print("3) Mostrar actividades")
    print("4) Guardar")
    print("5) Salir")
    
    menu = input("Elige una opción: ")

    match menu:
        case "1":
            añadir_actividad()
        case "2":
            eliminar_actividad()
        case "3":
            mostrar_actividades()
        case "4":
            guardar()
        case "5":
            seguir = False
            print("Saliendo...")
        case _:
            print("Opción no válida, intenta de nuevo")