# Arthur Ribeiro Araújo
# Emerson Sebastião dos Santos
# Matheus Latorre de Assis
# Vinícius Mlaker de Oliveira Dias

def carregarArquivo():
    pedidos = []
    arquivo = open("VENDAS.txt", "r")
    linha = arquivo.readline().rstrip().split(";")

    while linha != ['']:
        pedidos.append({
            'codigo': int(linha[0]),
            'quantidade': int(linha[1]),
            'valor unitário': float(linha[2])
        })
        linha = arquivo.readline().rstrip().split(";")

    arquivo.close()
    return pedidos

def calcularTotal(pedido):
    return pedido['quantidade'] * pedido['valor unitário']

def totalGeral(pedidos):
    totalGeral = 0
    
    for pedido in pedidos:
        totalGeral += calcularTotal(pedido)

    print(f"Total geral = R$ {totalGeral:.2f}")

def receberCodigos(pedidos):
    codigo = None
    limite = range(10000, 21001)

    while codigo != 0:
        codigo = int(input("Digite o código: "))

        if codigo in limite:
            total = 0

            for pedido in pedidos:
                if pedido['codigo'] == codigo:
                    total += calcularTotal(pedido)

            print(f"Total vendido do produto {codigo} = R$ {total:.2f}\n")

        elif codigo == 0:
            print("Fim do programa")
        else:
            print(f"{codigo} Código inválido (deve ser entre 10000 e 21000)\n")
            
pedidos = carregarArquivo()
totalGeral(pedidos)
receberCodigos(pedidos)