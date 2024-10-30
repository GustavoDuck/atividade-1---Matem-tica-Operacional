# Verificação de Semelhança de Triângulos

Este programa permite verificar a semelhança entre dois triângulos utilizando três critérios diferentes: Lado-Ângulo-Lado (LAL), Ângulo-Ângulo (AA) e Lado-Lado-Lado (LLL). O usuário pode inserir os lados e ângulos dos triângulos e escolher o critério de semelhança desejado.

## Funcionalidades

- **Critérios de Semelhança**:
  - LAL (Lado-Ângulo-Lado)
  - AA (Ângulo-Ângulo)
  - LLL (Lado-Lado-Lado)

## Estrutura do Código

### Funções

1. **`obter_numero(mensagem)`**
   - Solicita ao usuário um número e permite a saída do programa ao digitar "!s".
   - Retorna um número do tipo float se a entrada for válida, ou solicita novamente em caso de erro.

2. **`escolher_criterio()`**
   - Apresenta as opções de critérios de semelhança para o usuário.
   - Retorna a opção escolhida, permitindo também a saída do programa.

3. **`verifica_lal(lados1, lados2, angulo1, angulo2, tolerancia=1e-5)`**
   - Verifica se dois triângulos são semelhantes pelo critério LAL, comparando as proporções dos lados e o ângulo entre eles.

4. **`verifica_aa(angulo1, angulo2, angulo3, angulo4)`**
   - Verifica se dois triângulos são semelhantes pelo critério AA, comparando dois pares de ângulos.

5. **`verifica_lll(lados1, lados2)`**
   - Verifica se dois triângulos são semelhantes pelo critério LLL, comparando as proporções de todos os lados.

6. **`checar_seme(tri1, tri2, criterio)`**
   - Chama a função de verificação apropriada com base no critério escolhido e retorna uma mensagem confirmando ou negando a semelhança.

### Programa Principal

O programa principal executa as seguintes etapas:

1. **Escolha do Critério**: O usuário escolhe entre LAL, AA ou LLL.
2. **Entrada dos Dados do Primeiro Triângulo**: Dependendo do critério escolhido, o programa solicita os lados e/ou ângulos do primeiro triângulo.
3. **Entrada dos Dados do Segundo Triângulo**: O programa solicita os lados e/ou ângulos do segundo triângulo, de maneira semelhante ao primeiro.
4. **Verificação de Semelhança**: A função `checar_seme` é chamada para determinar se os triângulos são semelhantes com base nos dados inseridos.
5. **Resultado**: O resultado da análise é exibido ao usuário, indicando se os triângulos são semelhantes segundo o critério escolhido.

## Exemplo de Uso

- Ao executar o programa, o usuário escolhe um critério, insere os lados e ângulos dos triângulos, e o resultado é apresentado.
