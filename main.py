import sys
from tasks import listar_tarefas, adicionar_tarefa, concluir_tarefa, remover_tarefa

def exibir_menu():
    print("\n==================================")
    print("      GERENCIADOR DE TAREFAS      ")
    print("==================================")
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("0. Sair")
    print("==================================")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            listar_tarefas()
        elif opcao == "2":
            adicionar_tarefa()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "0":
            print("Saindo do programa... Até logo!")
            sys.exit(0)
        else:
            print("Opção inválida! Tente novamente.")

if _name_ == "_main_":
    main()