## **Código Python: Sistema de Cadastro de Pacientes**

```python
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
```

---

## **Funcionalidades**

* Cadastro de pacientes com **nome, idade, telefone e email**
* Listagem completa dos pacientes cadastrados
* Persistência de dados em **arquivo JSON**
* Sistema interativo no terminal

---

## **Requisitos**

* Python 3.x
* Arquivo `pacientes.json` será criado automaticamente

---

## **Como Executar**

1. Salve o arquivo como `cadastro_pacientes.py`
2. Execute:

```bash
python cadastro_pacientes.py
```

3. Siga o menu interativo para cadastrar ou listar pacientes

---

## **Exemplo de Uso**

```text
=== Sistema de Cadastro de Pacientes ===
1 - Cadastrar paciente
2 - Listar pacientes
3 - Sair
Escolha uma opção: 1

Nome: João Silva
Idade: 30
Telefone: (83) 99999-9999
Email: joao@email.com
✅ Paciente cadastrado com sucesso!

=== Sistema de Cadastro de Pacientes ===
1 - Cadastrar paciente
2 - Listar pacientes
3 - Sair
Escolha uma opção: 2

=== Lista de Pacientes ===
1. João Silva | Idade: 30 | Telefone: (83) 99999-9999 | Email: joao@email.com
==========================
```

---

## **README.md para GitHub**

````markdown
# 🏥 Sistema de Cadastro de Pacientes

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

## Descrição
Este projeto implementa um **sistema simples de cadastro de pacientes** utilizando Python.  
Os dados são armazenados em um arquivo **JSON**, permitindo persistência entre execuções.

---

## Funcionalidades
- Cadastrar paciente (nome, idade, telefone e email)
- Listar todos os pacientes cadastrados
- Persistência de dados em arquivo JSON
- Sistema interativo no terminal

---

## Requisitos
- Python 3.x

---

## Como Executar
1. Salve o arquivo `cadastro_pacientes.py`  
2. Execute no terminal:

```bash
python cadastro_pacientes.py
````

3. Utilize o menu para cadastrar ou listar pacientes.

---

## Melhorias Futuras

* Adicionar edição e exclusão de pacientes
* Validação de dados (telefone, email, idade)
* Interface gráfica (Tkinter ou PyQt)
* Versão web com Flask ou Django

---

## Licença

Uso pessoal e acadêmico.
