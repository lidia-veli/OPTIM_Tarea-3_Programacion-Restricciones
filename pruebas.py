from ortools.sat.python import cp_model

def assign_tasks():
    # Crear el modelo
    model = cp_model.CpModel()

    # Número de trabajadores y tareas
    num_workers = 3
    num_tasks = 3

    # Matriz de asignación trabajador-tarea
    assignment = {}
    for worker in range(num_workers):
        for task in range(num_tasks):
            assignment[(worker, task)] = model.NewBoolVar(f'worker{worker}_task{task}')

    # Cada trabajador realiza una tarea
    for worker in range(num_workers):
        model.Add(sum(assignment[(worker, task)] for task in range(num_tasks)) == 1)

    # Cada tarea es realizada por un trabajador
    for task in range(num_tasks):
        model.Add(sum(assignment[(worker, task)] for worker in range(num_workers)) == 1)

    # Restricciones para asignación específica
    model.Add(assignment[(0, 0)] == 1)  # Trabajador 1 realiza tarea 1
    model.Add(assignment[(1, 1)] == 1)  # Trabajador 2 realiza tarea 2
    model.Add(assignment[(2, 2)] == 1)  # Trabajador 3 realiza tarea 3

    # Crear el solucionador
    solver = cp_model.CpSolver()

    # Resolver el problema
    status = solver.Solve(model)

    # Mostrar la solución
    if status == cp_model.OPTIMAL:
        print("Asignación óptima encontrada:")
        for worker in range(num_workers):
            for task in range(num_tasks):
                if solver.Value(assignment[(worker, task)]) == 1:
                    print(f"Trabajador {worker + 1} realiza Tarea {task + 1}")
    else:
        print("No se encontró una asignación óptima.")

if __name__ == "__main__":
    assign_tasks()
