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
    """
    Lê um número inteiro digitado pelo usuário.

    Continua solicitando a entrada até que o usuário
    digite um valor válido.

    Parâmetros:
        num (str): mensagem exibida para o usuário.

    Retorna:
        int: número inteiro digitado.
    """
    while True:
        try:
            valor = int(input(num))
            return valor
        except ValueError:
            print("Erro, Digite um número inteiro!")


def leiapreco(num):
    """
    Lê um número decimal representando um preço.

    Continua solicitando até que o usuário digite
    um valor válido.

    Parâmetros:
        num (str): mensagem exibida ao usuário.

    Retorna:
        float: valor do preço informado.
    """
    while True:
        try:
            valor = float(input(num))
            return valor
        except ValueError:
            print('digite apenas numero float!')


def listar_produtos(produtos):
    """
    Lista todos os produtos cadastrados no estoque.

    Parâmetros:
        produtos (list): lista contendo dicionários
        com informações dos produtos.
    """
    for p in produtos:
        print(f"nome: {p['nome']} - preço: {p['preco']:.2f} - estoque: {p['estoque']}")


def vender_produto(produtos,nome,quantidade):
    """
    Realiza a venda de um produto.

    Verifica se o produto existe e se a quantidade
    solicitada está disponível em estoque.

    Parâmetros:
        produtos (list): lista de produtos cadastrados
        nome (str): nome do produto
        quantidade (int): quantidade a ser vendida

    Retorna:
        str: 'Sucesso', 'Falha' ou 'Inexistente'
    """
    for p in produtos:
        if p["nome"].strip().lower() == nome.strip().lower():
            if p["estoque"] >= quantidade:
                p["estoque"] -= quantidade
                return "Sucesso"
            else:
                return "Falha"
    return "Inexistente"


def repor_mercadoria(produto,nome,quantidade):
    """
    Realiza a reposição de estoque de um produto.

    Parâmetros:
        produto (list): lista contendo os produtos
        nome (str): nome do produto
        quantidade (int): quantidade a ser adicionada

    Retorna:
        str: 'Sucesso', 'Falha' ou 'Inexistente'
    """
    for p in produto:
        if p["nome"].strip().lower() == nome.strip().lower():
            if quantidade > 0:
                p["estoque"] += quantidade
                return "Sucesso"
            else:
                return "Falha"
    return "Inexistente"


def somar_produtos(produtos):
    """
    Calcula o valor total de todos os produtos
    disponíveis no estoque.

    O cálculo é feito multiplicando o preço
    pela quantidade de cada produto.

    Parâmetros:
        produtos (list): lista de produtos cadastrados.

    Retorna:
        float: valor total do estoque.
    """
    total = 0
    for p in produtos:
        total += p["preco"] * p["estoque"]
    return total


def main():
    """
    Função principal do sistema.

    Responsável por:
    - Exibir o menu
    - Receber as opções do usuário
    - Controlar as operações do sistema
    - Executar o loop principal do programa
    """

    produtos = [
        {"nome": "Arroz", "preco": 25.0, "estoque": 10},
        {"nome": "Feijão", "preco": 8.5, "estoque": 20},

    ]

    print("0 - para adicionar novos produtos")
    print("1 - Listar produtos")
    print("2 - Vender produto")
    print("3 - Repor produto")
    print("4 - Total vendas")
    print("5 - Sair")

    while True:
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
                print("Quantidade inválida para reposição!")

            elif repor == "Inexistente":
                print("Esse produto não consta na nossa base de dados!")

        elif opc == 4:
            total = somar_produtos(produtos)
            print(f"O total no estoque é de {total:.2f}R$")

        elif opc ==5:
            print("Saindo do sistema ....")
            break

        else:
            print("Erro digite um valor no intervalo  entre 1 e 5.")


main()
