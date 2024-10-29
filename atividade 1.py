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

def verifica_lal(lados1, lados2, angulo1, angulo2):
    proporcao_lados = lados1[0] / lados2[0] == lados1[1] / lados2[1]
    angulo_congruente = angulo1 == angulo2
    return proporcao_lados and angulo_congruente

def verifica_aa(angulos1, angulos2):
    return angulos1 == angulos2

def verifica_lll(lados1, lados2):
    return all(l1 / l2 == lados1[0] / lados2[0] for l1, l2 in zip(lados1, lados2))

def checar_seme(tri1, tri2, criterio):
    if criterio == "LAL":
        return "Semelhança LAL confirmada." if verifica_lal(tri1[:2], tri2[:2], tri1[2], tri2[2]) else "Semelhança LAL não confirmada."
    elif criterio == "AA":
        return "Semelhança AA confirmada." if verifica_aa(tri1[2:], tri2[2:]) else "Semelhança AA não confirmada."
    elif criterio == "LLL":
        return "Semelhança LLL confirmada." if verifica_lll(tri1[:3], tri2[:3]) else "Semelhança LLL não confirmada."

# Programa principal
criterio = escolher_criterio()

print("\nInforme os lados e ângulos do primeiro triângulo (ou '!s' para encerrar):")
triangulo1 = [
    obter_numero("Lado 1: "),
    obter_numero("Lado 2: "),
    obter_numero("Lado 3: "),
    obter_numero("Ângulo 1: "),
    obter_numero("Ângulo 2: ")
]

print("\nInforme os lados e ângulos do segundo triângulo (ou '!s' para encerrar):")
triangulo2 = [
    obter_numero("Lado 1: "),
    obter_numero("Lado 2: "),
    obter_numero("Lado 3: "),
    obter_numero("Ângulo 1: "),
    obter_numero("Ângulo 2: ")
]

resultado = checar_seme(triangulo1, triangulo2, criterio)
print("\nResultado da análise:", resultado)
