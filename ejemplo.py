from ortools.sat.python import cp_model

# Instanciar el modelo y el solucionador de CP-SAT
model = cp_model.CpModel()
solver = cp_model.CpSolver()

# Definir variables para representar las asignaciones de clases
num_cursos = 10
num_aulas = 3
num_profesores = 5

# Definir las variables de asignación
asignaciones = {}
for curso in range(num_cursos):
    for aula in range(num_aulas):
        for profesor in range(num_profesores):
            asignaciones[(curso, aula, profesor)] = model.NewBoolVar(f"Curso_{curso}_Aula_{aula}_Profesor_{profesor}")

# Aplicar restricciones
# PONER RESTRICCIONES

# Crear un solucionador y resolver el problema

solver.Solve(model)

# Imprimir la solución
for curso in range(num_cursos):
    for aula in range(num_aulas):
        for profesor in range(num_profesores):
            if solver.Value(asignaciones[(curso, aula, profesor)]) == 1:
                print(f"Curso {curso} en Aula {aula} con Profesor {profesor}")
