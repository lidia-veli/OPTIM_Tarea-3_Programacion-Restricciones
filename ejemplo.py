from ortools.sat.python import cp_model

def assign_tasks():
    # Crear el modelo
    model = cp_model.CpModel()

    # VARIABLES
    # Número de trabajadores y tareas
    num_workers = 4
    num_tasks = 4

    # Matriz de tiempo que tarda cada trabajador en realizar cada tarea
    task_times = [  [3, 5, 2, 7],
                    [4, 6, 3, 8],
                    [2, 4, 1, 6],
                    [5, 7, 2, 9]    ]

    # Matriz de asignación trabajador-tarea
    assignment = {}
    for worker in range(num_workers):
        for task in range(num_tasks):
            assignment[(worker, task)] = model.NewBoolVar(f'worker{worker}_task{task}')


    # RESTRICCIONES
    # 1) Cada trabajador realiza una tarea
    for worker in range(num_workers):
        model.Add(sum(assignment[(worker, task)] for task in range(num_tasks)) == 1)

    # 2) Cada tarea es realizada por un trabajador
    for task in range(num_tasks):
        model.Add(sum(assignment[(worker, task)] for worker in range(num_workers)) == 1)


    # FUNCIÓN OBJETIVO: Minimizar el tiempo total de trabajo
    total_time = model.NewIntVar(0, sum(max(row) for row in task_times), 'total_time')
    model.Add(total_time == sum(
        task_times[worker][task] * assignment[(worker, task)]
        for worker in range(num_workers)
        for task in range(num_tasks)
    ))

    # Solucionador
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Imprimir la solución
    if status == cp_model.OPTIMAL:
        print("Asignación óptima encontrada:")
        for worker in range(num_workers):
            for task in range(num_tasks):
                if solver.Value(assignment[(worker, task)]) == 1:
                    print(f"- Trabajador {worker + 1} realiza Tarea {task + 1}")
        print(f"Tiempo total de trabajo: {solver.Value(total_time)} horas")
    else:
        print("No se encontró una asignación óptima.")



# CODIGO EJECUTABLE
if __name__ == "__main__":
    assign_tasks()
