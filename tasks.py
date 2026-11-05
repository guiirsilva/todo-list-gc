from storage import carregar_tarefas, salvar_tarefas

def listar_tarefas():
    # OBS: Alterações nesta linha (no cabeçalho) podem gerar conflitos intencionais entre branches!
    print("\n--- MINHAS TAREFAS ---")
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    for t in tarefas:
        status = "[X]" if t["concluida"] else "[ ]"
        print(f"{t['id']}. {status} {t['descricao']}")

def adicionar_tarefa():
    descricao = input("Digite a descrição da nova tarefa: ").strip()
    if not descricao:
        print("A descrição não pode ser vazia.")
        return
    
    tarefas = carregar_tarefas()
    novo_id = max([t["id"] for t in tarefas], default=0) + 1
    tarefas.append({"id": novo_id, "descricao": descricao, "concluida": False})
    
    salvar_tarefas(tarefas)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def concluir_tarefa():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("\n--- MINHAS TAREFAS ---\nNenhuma tarefa cadastrada.")
        return
    
    listar_tarefas()
    try:
        tarefa_id = int(input("Digite o ID da tarefa que deseja marcar como concluída: "))
        encontrado = False
        for t in tarefas:
            if t["id"] == tarefa_id:
                t["concluida"] = True
                encontrado = True
                break
        
        if encontrado:
            salvar_tarefas(tarefas)
            print(f"Tarefa {tarefa_id} marcada como concluída!")
        else:
            print("ID de tarefa não encontrado.")
    except ValueError:
        print("Por favor, digite um número válido.")

def remover_tarefa():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("\n--- MINHAS TAREFAS ---\nNenhuma tarefa cadastrada.")
        return
    
    listar_tarefas()
    try:
        tarefa_id = int(input("Digite o ID da tarefa que deseja remover: "))
        tarefas_filtradas = [t for t in tarefas if t["id"] != tarefa_id]
        
        if len(tarefas_filtradas) < len(tarefas):
            salvar_tarefas(tarefas_filtradas)
            print(f"Tarefa {tarefa_id} removida com sucesso!")
        else:
            print("ID de tarefa não encontrado.")
    except ValueError:
        print("Por favor, digite um número válido.")