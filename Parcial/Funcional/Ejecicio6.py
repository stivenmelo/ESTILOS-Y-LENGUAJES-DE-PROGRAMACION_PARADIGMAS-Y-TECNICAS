# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from functools import reduce

# ─────────────────────────────────────────────────────────
# FUNCIONES PURAS
# Cada función: recibe datos → retorna datos nuevos
# NUNCA modifica lo que recibe ni imprime nada
# ─────────────────────────────────────────────────────────

def calcular_promedio(notas):
    # reduce suma todas las notas una a una → divide entre la cantidad
    # reduce(f, [1,2,3]) = f(f(1,2), 3)
    return reduce(lambda acum, nota: acum + nota, notas) / len(notas)


def filtrar_aprobados(estudiantes):
    # filter devuelve solo los que cumplen la condición
    # aprobado = promedio >= 3.0 Y asistencia >= 75
    def es_aprobado(estudiante):
        promedio   = calcular_promedio(estudiante["notas"])
        asistencia = estudiante["asistencia"]
        return promedio >= 3.0 and asistencia >= 75

    return list(filter(es_aprobado, estudiantes))


def agregar_promedio(estudiantes):
    # map aplica la función a cada estudiante
    # NO modifica el original → crea un diccionario NUEVO con {**e, "promedio": ...}
    def enriquecer(estudiante):
        promedio = calcular_promedio(estudiante["notas"])
        return {**estudiante, "promedio": round(promedio, 2)}

    return list(map(enriquecer, estudiantes))


def ordenar_por_promedio(estudiantes):
    # sorted retorna una lista NUEVA ordenada, no modifica la original
    return sorted(estudiantes, key=lambda e: e["promedio"], reverse=True)


def generar_reporte(estudiantes):
    # map transforma cada estudiante en un diccionario de reporte
    def formatear(estudiante):
        return {
            "nombre":     estudiante["nombre"],
            "promedio":   estudiante["promedio"],
            "asistencia": estudiante["asistencia"],
            "estado":     "Aprobado"
        }

    return list(map(formatear, estudiantes))


# ─────────────────────────────────────────────────────────
# PIPELINE
# Aplica una lista de funciones en cadena sobre los datos
# resultado = f4(f3(f2(f1(datos))))
# ─────────────────────────────────────────────────────────

def pipeline(funciones, datos):
    # reduce aplica cada función pasando el resultado a la siguiente
    return reduce(lambda acum, funcion: funcion(acum), funciones, datos)


# ─────────────────────────────────────────────────────────
# DATOS DE PRUEBA
# ─────────────────────────────────────────────────────────

estudiantes = [
    {"nombre": "Ana",    "notas": [4.5, 3.8, 4.2, 3.9], "asistencia": 90},
    {"nombre": "Luis",   "notas": [2.0, 1.5, 2.5, 2.1], "asistencia": 80},
    {"nombre": "María",  "notas": [3.5, 4.0, 3.8, 4.1], "asistencia": 70},
    {"nombre": "Carlos", "notas": [4.0, 4.5, 3.9, 4.2], "asistencia": 95},
    {"nombre": "Sofía",  "notas": [2.8, 3.2, 3.0, 2.9], "asistencia": 85},
    {"nombre": "Pedro",  "notas": [1.5, 2.0, 1.8, 2.2], "asistencia": 60},
]


# ─────────────────────────────────────────────────────────
# EJECUTAR PIPELINE
# ─────────────────────────────────────────────────────────

reporte = pipeline(
    [filtrar_aprobados, agregar_promedio, ordenar_por_promedio, generar_reporte],
    estudiantes
)

for estudiante in reporte:
    print(f"{estudiante['nombre']:10} | promedio: {estudiante['promedio']} | asistencia: {estudiante['asistencia']}%")
