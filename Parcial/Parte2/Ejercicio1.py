estudiantes = [
 {"nombre": "Ana", "notas": [4.5, 3.8, 4.2]},
 {"nombre": "Luis", "notas": [2.1, 1.9, 2.5]},
 {"nombre": "Maria", "notas": [3.0, 3.5, 2.8]},
 {"nombre": "Carlos", "notas": [4.8, 4.6, 4.9]},
]

def  procesar_notas(estudiantes:dict):
    respuesta:dict = {}
    promedioGeneral:float = 0
    mejorPromedio:float = 0
    estudiantesAprobados:list[str] = []
    estudiantesReprobados:list[str] = []
    for estudiante in estudiantes:
        promedioEstudiante:float = 0
        promedioEstudiante = sum(estudiante["notas"])/float(len(estudiante["notas"]))
        promedioGeneral +=promedioEstudiante

        if(mejorPromedio< promedioEstudiante):
            mejorPromedio = promedioEstudiante
            respuesta["mejor_estudiante"] = estudiante["nombre"]


        if(promedioEstudiante >= 3.0):
            estudiantesAprobados.append(estudiante["nombre"])
        else:
            estudiantesReprobados.append(estudiante["nombre"])

        promedioEstudiante= 0

    promedioGeneral= promedioGeneral/float(len(estudiantes))
    
    respuesta["promedio_general"] = promedioGeneral
    respuesta["aprobados"] = estudiantesAprobados
    respuesta["reprobados"] = estudiantesReprobados
        
    print(f"\n\n{respuesta}")


procesar_notas(estudiantes)

# Salida esperada:
 # {
 # "promedio_general": 3.635,
 # "mejor_estudiante": "Carlos",
 # "aprobados": ["Ana", "Maria", "Carlos"],
 # "reprobados": ["Luis"]
 # }