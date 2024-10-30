def obter_numero(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada.lower() == "!s":
            print("Encerrando o programa. Obrigado!")
            exit()
        try:
            return float(entrada)
        except ValueError:
            print("Por favor, insira um número válido.")

def escolher_criterio():
    opcoes = {"1": "LAL", "2": "AA", "3": "LLL"}
    print("Escolha o critério de semelhança:")
    print("1 - LAL (Lado-Ângulo-Lado)")
    print("2 - AA (Ângulo-Ângulo)")
    print("3 - LLL (Lado-Lado-Lado)")
    while True:
        escolha = input("Digite o número do critério ou '!s' para sair: ").strip()
        if escolha in opcoes:
            return opcoes[escolha]
        elif escolha.lower() == "!s":
            print("Programa finalizado.")
            exit()
        else:
            print("Opção inválida! Escolha 1, 2, 3 ou '!s' para sair.")

def verifica_lal(lados1, lados2, angulo1, angulo2, tolerancia=1e-5):
    proporcao1 = lados1[0] / lados2[0] if lados2[0] != 0 else None
    proporcao2 = lados1[1] / lados2[1] if lados2[1] != 0 else None
    return (proporcao1 is not None and proporcao2 is not None and 
            abs(proporcao1 - proporcao2) < tolerancia and angulo1 == angulo2)

def verifica_aa(angulo1, angulo2, angulo3, angulo4):
    return angulo1 == angulo3 and angulo2 == angulo4

def verifica_lll(lados1, lados2):
    proporcao1 = lados1[0] / lados2[0] if lados2[0] != 0 else None
    proporcao2 = lados1[1] / lados2[1] if lados2[1] != 0 else None
    proporcao3 = lados1[2] / lados2[2] if lados2[2] != 0 else None
    return (proporcao1 is not None and proporcao2 is not None and proporcao3 is not None and 
            abs(proporcao1 - proporcao2) < 1e-5 and abs(proporcao2 - proporcao3) < 1e-5)

def checar_seme(tri1, tri2, criterio):
    if criterio == "LAL":
        return "Semelhança LAL confirmada." if verifica_lal(tri1[:2], tri2[:2], tri1[2], tri2[2]) else "Semelhança LAL não confirmada."
    elif criterio == "AA":
        return "Semelhança AA confirmada." if verifica_aa(tri1[0], tri1[1], tri2[0], tri2[1]) else "Semelhança AA não confirmada."
    elif criterio == "LLL":
        return "Semelhança LLL confirmada." if verifica_lll(tri1[:3], tri2[:3]) else "Semelhança LLL não confirmada."

# Programa principal
criterio = escolher_criterio()

print("\nInforme os lados e ângulos do primeiro triângulo (ou '!s' para encerrar):")
triangulo1 = []

# Solicita os dados do primeiro triângulo
if criterio == "LAL":
    triangulo1 = [
        obter_numero("Lado 1: "),
        obter_numero("Lado 2: "),
        obter_numero("Ângulo entre eles: ")
    ]
elif criterio == "AA":
    triangulo1 = [
        obter_numero("Ângulo 1: "),
        obter_numero("Ângulo 2: ")
    ]
elif criterio == "LLL":
    triangulo1 = [
        obter_numero("Lado 1: "),
        obter_numero("Lado 2: "),
        obter_numero("Lado 3: ")
    ]

print("\nInforme os lados e ângulos do segundo triângulo (ou '!s' para encerrar):")
triangulo2 = []

# Solicita os dados do segundo triângulo
if criterio == "LAL":
    triangulo2 = [
        obter_numero("Lado 1: "),
        obter_numero("Lado 2: "),
        obter_numero("Ângulo entre eles: ")
    ]
elif criterio == "AA":
    triangulo2 = [
        obter_numero("Ângulo 1: "),
        obter_numero("Ângulo 2: ")
    ]
elif criterio == "LLL":
    triangulo2 = [
        obter_numero("Lado 1: "),
        obter_numero("Lado 2: "),
        obter_numero("Lado 3: ")
    ]

resultado = checar_seme(triangulo1, triangulo2, criterio)
print("\nResultado da análise:", resultado)
