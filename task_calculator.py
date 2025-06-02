# task_calculator.py
def add_task(tasks, task_description):
    """Adiciona uma nova tarefa à lista."""
    tasks.append({"description": task_description, "completed": False})
    print(f"Tarefa '{task_description}' adicionada com sucesso!")

def list_tasks(tasks):
    """Lista todas as tarefas."""
    if not tasks:
        print("Nenhuma tarefa na lista.")
        return
    print("\nLista de Tarefas:")
    for i, task in enumerate(tasks, start=1):
        status = "Concluída" if task["completed"] else "Pendente"
        print(f"{i}. {task['description']} - {status}")

def complete_task(tasks, task_index):
    """Marca uma tarefa como concluída."""
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Tarefa '{tasks[task_index - 1]['description']}' marcada como concluída!")
    else:
        print("Índice de tarefa inválido.")

def main():
    tasks = []
    while True:
        print("\n=== Calculadora de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair")
        
        choice = input("Escolha uma opção (1-4): ")
        
        if choice == "1":
            task_description = input("Digite a descrição da tarefa: ")
            add_task(tasks, task_description)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks)
            try:
                task_index = int(input("Digite o número da tarefa para marcar como concluída: "))
                complete_task(tasks, task_index)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif choice == "4":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()