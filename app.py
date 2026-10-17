import json
import xml.etree.ElementTree as ET
import yaml
from pathlib import Path

CARPETA = Path(__file__).parent
ARCHIVO_JSON = CARPETA / "docentes.json"
ARCHIVO_YAML = CARPETA / "docentes.yaml"
ARCHIVO_XML = CARPETA / "docentes.xml"


def cargar_json(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al cargar JSON: {e}")
        return []


def cargar_yaml(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error al cargar YAML: {e}")
        return []


def cargar_xml(ruta):
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        docentes = []
        for elem in root.findall("docente"):
            docente = {
                "numero_empleado": elem.find("numero_empleado").text,
                "nombre": elem.find("nombre").text,
                "especialidad": elem.find("especialidad").text,
            }
            docentes.append(docente)
        return docentes
    except Exception as e:
        print(f"Error al cargar XML: {e}")
        return []


def mostrar_docentes(docentes, formato):
    print(f"\n--- LISTA DE DOCENTES ({formato}) ---")
    if not docentes:
        print("No se encontraron registros.")
        return
    for d in docentes:
        print(
            f"ID: {d.get('numero_empleado')} | Nombre: {d.get('nombre')} | Especialidad: {d.get('especialidad')}"
        )


def menu():
    while True:
        print("\n====================================")
        print("    SISTEMA DE DOCENTES UTC         ")
        print("====================================")
        print("1. Leer datos desde JSON")
        print("2. Leer datos desde YAML")
        print("3. Leer datos desde XML")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            docentes = cargar_json(ARCHIVO_JSON)
            mostrar_docentes(docentes, "JSON")
        elif opcion == "2":
            docentes = cargar_yaml(ARCHIVO_YAML)
            mostrar_docentes(docentes, "YAML")
        elif opcion == "3":
            docentes = cargar_xml(ARCHIVO_XML)
            mostrar_docentes(docentes, "XML")
        elif opcion == "4":
            print("¡Saliendo del sistema!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
