import json
import os

ARQUIVO_TAREFAS = 'tarefas.json'

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, 'r') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as f:
        conteudo = json.dumps(tarefas, indent=4)
        f.write(conteudo)

def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i+1}. {status} {tarefa['descricao']}")

def adicionar_tarefa(tarefas):
    desc = input("Digite a descrição da tarefa: ").strip()
    if desc:
        tarefas.append({"descricao": desc, "concluida": False})
        salvar_tarefas(tarefas)
        print("Tarefa adicionada com sucesso!")
    else:
        print("Descrição vazia não é permitida.")

def concluir_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    try:
        i = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= i < len(tarefas):
            tarefas[i]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def remover_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    try:
        i = int(input("Digite o número da tarefa a remover: ")) - 1
        if 0 <= i < len(tarefas):
            del tarefas[i]
            salvar_tarefas(tarefas)
            print("Tarefa removida.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n==== MENU TO-DO ====")
        print("1. Ver tarefas")
        print("2. Adicionar tarefa")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            mostrar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()