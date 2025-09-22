import json
import os

ARQUIVO = "pacientes.json"

# Função para carregar pacientes do arquivo
def carregar_pacientes():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as file:
        return json.load(file)

# Função para salvar pacientes no arquivo
def salvar_pacientes(pacientes):
    with open(ARQUIVO, "w", encoding="utf-8") as file:
        json.dump(pacientes, file, indent=4, ensure_ascii=False)

# Função para cadastrar paciente
def cadastrar_paciente(pacientes):
    nome = input("Nome: ")
    idade = input("Idade: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "email": email
    }
    
    pacientes.append(paciente)
    salvar_pacientes(pacientes)
    print("✅ Paciente cadastrado com sucesso!")

# Função para listar pacientes
def listar_pacientes(pacientes):
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    print("\n=== Lista de Pacientes ===")
    for i, paciente in enumerate(pacientes):
        print(f"{i+1}. {paciente['nome']} | Idade: {paciente['idade']} | Telefone: {paciente['telefone']} | Email: {paciente['email']}")
    print("==========================\n")

# Função principal
def main():
    pacientes = carregar_pacientes()
    
    while True:
        print("=== Sistema de Cadastro de Pacientes ===")
        print("1 - Cadastrar paciente")
        print("2 - Listar pacientes")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            cadastrar_paciente(pacientes)
        elif escolha == "2":
            listar_pacientes(pacientes)
        elif escolha == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente!")

if __name__ == "__main__":
    main()
