# Gerenciador Simples de Funcionários

import json
import os


ARQUIVO_DADOS = "funcionarios.json"



def carregar_dados():

    if not os.path.exists(ARQUIVO_DADOS):
        return []
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            lista_dados = json.load(f)
            return lista_dados
    except Exception:
        
        print("\n[AVISO] Não consegui ler o arquivo de dados. Começando lista do zero.\n")
        return []

def salvar_dados(funcionarios):

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        # Salva em formato legível com indentação
        json.dump(funcionarios, f, ensure_ascii=False, indent=4)

# --- Funções do Menu 

def adicionar_funcionario(funcionarios):

    print("\n--- CADASTRO DE NOVO FUNCIONÁRIO ---")
    
    nome = input("Nome completo: ").strip()
    if not nome:
        print("Nome inválido. Cancelando operação.")
        return
        
    salario_str = input("Salário (Ex: 3500.50): ").strip().replace(",", ".")
    try:
        salario = float(salario_str)
    except ValueError:
        print("Salário inválido (use apenas números).")
        return
        
    cargo = input("Cargo (opcional): ").strip()

    # Define o ID 
    novo_id = len(funcionarios) + 1 
    
    novo_empregado = {
        "id": novo_id,
        "nome": nome,
        "salario": salario,
        "cargo": cargo
    }
    
    funcionarios.append(novo_empregado)
    salvar_dados(funcionarios)
    print(f"\nFuncionário '{nome}' (ID {novo_id}) adicionado com sucesso!\n")


def listar_funcionarios(funcionarios):

    print("\n--- LISTA GERAL DE FUNCIONÁRIOS ---")
    if not funcionarios:
        print("A lista está vazia. Adicione alguém primeiro (opção 1).")
        return
    
    for f in funcionarios:
        
        salario_formatado = f.get("salario", 0.00)
        
        print(f'ID: {f["id"]} | Nome: {f["nome"]} | Cargo: {f["cargo"]} | Salário: R$ {salario_formatado:.2f}')
    print("-" * 35 + "\n")
# Bucas de funcionarios 

def buscar_funcionario(funcionarios):

    print("\n--- BUSCA POR NOME ---")
    if not funcionarios:
        print("A lista está vazia.")
        return

    termo = input("Digite o nome ou parte do nome para buscar: ").strip().lower()
    
    # Filtra a lista 
    encontrados = [
        f for f in funcionarios if termo in f.get("nome", "").lower()
    ]

    if not encontrados:
        print(f"Nenhum funcionário encontrado com o termo '{termo}'.")
        return

    print(f"\n--- {len(encontrados)} RESULTADO(S) ENCONTRADO(S) ---")
    for f in encontrados:
        salario_formatado = f.get("salario", 0.00)
        print(f'ID: {f["id"]} | Nome: {f["nome"]} | Cargo: {f["cargo"]} | Salário: R$ {salario_formatado:.2f}')
    print("-" * 35 + "\n")


def calcular_media(funcionarios):

    print("\n--- CÁLCULO DE MÉDIA SALARIAL ---")
    if not funcionarios:
        print("Não há funcionários para calcular a média.")
        return

    # Soma todos os salários
    soma_salarios = sum(f.get("salario", 0) for f in funcionarios)
    media = soma_salarios / len(funcionarios)
    
    print(f"Total de funcionários na base: {len(funcionarios)}")
    print(f"A Média salarial é de: R$ {media:.2f}\n")




def menu_principal():
    
    # Cria uma lista de funcionários
    lista_funcionarios = carregar_dados()
    
    while True:
        print("\n=== GERENCIADOR - MENU PRINCIPAL ===")
        print("1. Cadastrar um novo funcionário") # Adicionar
        print("2. Ver a lista de todos os funcionários") # Listar
        print("3. Buscar funcionário por nome") # Buscar
        print("4. Calcular a Média Salarial") # Calcular Média
        print("5. Sair do programa")
        
        escolha = input("Escolha uma opção (1 a 5): ").strip()
        
        if escolha == "1":
            adicionar_funcionario(lista_funcionarios)
        elif escolha == "2":
            listar_funcionarios(lista_funcionarios)
        elif escolha == "3":
            buscar_funcionario(lista_funcionarios)
        elif escolha == "4":
            calcular_media(lista_funcionarios)
        elif escolha == "5":
            print("\nFinalizando. Até mais!")
            break
        else:
            print("\nOpção inválida. Digite um número de 1 a 5.")

if __name__ == "__main__":
    menu_principal()