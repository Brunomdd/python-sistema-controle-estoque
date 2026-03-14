# Sistema de Controle de Estoque (Python)

Projeto desenvolvido em Python para simular um sistema simples de controle de estoque de um pequeno mercado utilizando o terminal.

O objetivo deste projeto é praticar conceitos fundamentais de programação como:

- lógica de programação
- controle de fluxo
- validação de entrada de dados
- organização de código em funções
- manipulação de listas e dicionários

---

## Funcionalidades

O sistema permite:

• Listar todos os produtos cadastrados  
• Adicionar novos produtos ao estoque  
• Vender produtos existentes  
• Repor produtos no estoque  
• Calcular o valor total do estoque  

---

## Regras do Sistema

- O produto deve existir para ser vendido
- A quantidade vendida não pode ser maior que o estoque disponível
- A reposição deve ser maior que zero
- O sistema valida entradas inválidas do usuário

---

## Estrutura dos Produtos

Os produtos são armazenados em uma lista de dicionários com a seguinte estrutura:

```python
{
    "nome": "Arroz",
    "preco": 25.0,
    "estoque": 10
}
