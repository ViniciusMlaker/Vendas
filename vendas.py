# Arthur Ribeiro Araújo
# Emerson Sebastião dos Santos
# Matheus Latorre de Assis
# Vinícius Mlaker de Oliveira Dias

def carregarArquivo():
    pedidos = [] # Iniciamos uma lista que receberá cada linha (pedido) do CSV como um dicionário diferente
    arquivo = open("VENDAS.txt", "r") # Arquivo de vendas aberto para leitura
    linha = arquivo.readline().rstrip().split(";") # Lemos a primeira linha do arquivo, limpamos o \n escondido no final da linha e definimos os separadores como ";"

    while linha != ['']: # Laço que se repete até encontrar um termo em branco na lista (que seria uma linha em branco no arquivo)
        pedidos.append({ # Adicionamos à lista o primeiro dicionário "código = inteiro do primeiro valor", "quantidade = inteiro do segundo valor" e "valor unitário = float do terceiro valor"
            'código': int(linha[0]),
            'quantidade': int(linha[1]),
            'valor unitário': float(linha[2])
        })
        linha = arquivo.readline().rstrip().split(";") # Repetimos o laço para adicionar as outras linhas a lista de pedidos

    arquivo.close() # Fechamos o arquivo que já está carregado na memória
    return pedidos # Função retorna a lista de dicionários gerada pelo arquivo

def calcularTotal(pedido):
    return pedido['quantidade'] * pedido['valor unitário']

def totalGeral(pedidos):
    totalGeral = 0
    
    for pedido in pedidos:
        totalGeral += calcularTotal(pedido)

    print(f"Total geral = R$ {totalGeral:.2f}\n")

def receberCodigos(pedidos):
    codigo = None
    limite = range(10000, 21001)

    while codigo != 0:
        codigo = int(input("Digite o código: "))

        if codigo in limite:
            total = 0

            for pedido in pedidos:
                if pedido['código'] == codigo:
                    total += calcularTotal(pedido)

            print(f"Total vendido do produto {codigo} = R$ {total:.2f}\n")

        elif codigo == 0:
            print("Fim do programa")
        else:
            print(f"{codigo} Código inválido (deve ser entre 10000 e 21000)\n")
            
pedidos = carregarArquivo()
totalGeral(pedidos)
receberCodigos(pedidos)