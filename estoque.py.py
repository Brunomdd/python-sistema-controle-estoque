#Sistema de Controle de Estoque (Console)
#Desenvolva um sistema em Python para controle de estoque de produtos em um pequeno mercado.
#Cada produto deve conter:
#nome
#preço
#quantidade em estoque
#O sistema deve permitir:
#Listar todos os produtos com seus respectivos estoques
#Vender um produto, reduzindo a quantidade em estoque
#O produto deve existir
#A quantidade vendida não pode ser maior que o estoque disponível
#Repor produtos existentes no estoque
#A quantidade de reposição deve ser maior que zero
#O programa deve funcionar em loop até o usuário encerrar manualmente e deve validar todas as entradas do usuário

def leiaint(num):
    while True:
        try:
            valor = int(input(num))
            return valor
        except ValueError:
            print("Erro, Digite um número inteiro!")



def leiapreco(num):
    while True:
        try:
            valor = float(input(num))
            return valor
        except ValueError:
            print('digite apenas numero float!')


def listar_produtos(produtos):
    print("\n=== PRODUTOS ===")
    for p in produtos:
        print(f"Nome: {p['nome']} | Preço: R${p['preco']:.2f} | Estoque: {p['estoque']}")

def vender_produto(produtos,nome,quantidade):
    for p in produtos:
        if p["nome"].strip().lower() == nome.strip().lower():
            if p["estoque"] >= quantidade:
                p["estoque"] -= quantidade
                return "Sucesso"
            else:
                return "Falha"
    return "Inexistente"


def repor_mercadoria(produto,nome,quantidade):
    for p in produto:
        if p['nome'] == nome:
            if quantidade > 0:
                p['estoque'] += quantidade
                return "Sucesso"
            else:
                return "Falha"
    return "Inexistente"


def somar_produtos(produtos):
    total = 0
    for p in produtos:
        total += p["preco"] * p["estoque"]
    return total


def main():
    produtos = [
        {"nome": "Arroz", "preco": 25.0, "estoque": 10},
        {"nome": "Feijão", "preco": 8.5, "estoque": 20},
        {"nome": "Macarrão", "preco": 4.5, "estoque": 30},
        {"nome": "Óleo", "preco": 7.9, "estoque": 15},
        {"nome": "Açúcar", "preco": 5.2, "estoque": 18},
        {"nome": "Sal", "preco": 2.5, "estoque": 25},
        {"nome": "Leite", "preco": 4.8, "estoque": 40},
        {"nome": "Café", "preco": 12.9, "estoque": 12},
        {"nome": "Farinha", "preco": 6.3, "estoque": 16},
        {"nome": "Biscoito", "preco": 3.9, "estoque": 22}
    ]


    while True:
        print("0 - para adicionar novos produtos")
        print("1 - Listar produtos")
        print("2 - Vender produto")
        print("3 - Repor produto")
        print("4 - Total vendas")
        print("5 - Sair")

        opc = leiaint("digite o número: ")
        if opc == 0:
            nome = str(input('nome: '))
            if not nome:
                print('não pode deixar vazio!')
                continue
            preco = leiapreco("preço: ")
            estoque = leiaint('quantidade: ')
            produtos.append({"nome":nome,"preco":preco,"estoque":estoque})

        elif opc == 1:
            listar_produtos(produtos)
        elif opc == 2:
            nome= str(input('nome: '))
            if not nome:
                print('erro nao pode deixar vazio!')
                continue
            quantidade = leiaint("quantidade: ")
            if quantidade <= 0:
                print("Erro, quantidade inválida.")
                continue
            vender = vender_produto(produtos,nome,quantidade)
            if vender == "Sucesso":
                print("Venda concluida com sucesso!")
            elif vender == "Falha":
                print("Não foi possivel vender esse produto")
            elif vender == "Inexistente":
                print("Esse produto não consta na nossa base de dados!")
        elif opc == 3:
            nome = str(input('nome: '))
            if not nome:
                print('erro nao pode deixar vazio!')
                continue
            quantidade = leiaint("quantidade: ")
            if quantidade <= 0:
                print("Erro, quantidade inválida.")
                continue
            repor = repor_mercadoria(produtos,nome,quantidade)
            if repor  == "Sucesso":
                print("Produto foi para reposição com sucesso!")
            elif repor == "Falha":
                print("Não há necessidade de repor o produto!")
            elif repor == "Inexistente":
                print("Esse produto não consta na nossa base de dados!")
        elif opc == 4:
            total = somar_produtos(produtos)
            print(f"O total no estoque é de {total:.2f}R$")
        elif opc ==5:
            print("Saindo do sistema ....")
            break
        else:
            print("Erro digite um valor no intervalo  entre 0 e 5.")


main()


