# Lógica do Algoritmo para Verificação de Semelhança de Triângulos

Este programa foi desenvolvido para verificar a semelhança entre triângulos utilizando três critérios distintos: Lado-Ângulo-Lado (LAL), Ângulo-Ângulo (AA) e Lado-Lado-Lado (LLL). Abaixo está a explicação detalhada da lógica utilizada no algoritmo.

## 1. Entrada de Dados

- O programa solicita ao usuário que escolha um critério de semelhança entre os triângulos:
    - **LAL** (Lado-Ângulo-Lado)
    - **AA** (Ângulo-Ângulo)
    - **LLL** (Lado-Lado-Lado)
- Dependendo da escolha do critério, o programa pede ao usuário que insira os valores dos lados e/ou ângulos dos dois triângulos.

## 2. Verificação da Semelhança

- O programa utiliza funções específicas para verificar a semelhança de acordo com o critério escolhido:
    - **Função `verifica_lal`:** 
        - Compara os dois lados proporcionais e o ângulo entre eles.
    - **Função `verifica_aa`:**
        - Compara os dois ângulos de cada triângulo.
    - **Função `verifica_lll`:**
        - Compara todos os lados para verificar se estão em proporção.

## 3. Retorno do Resultado

- Após realizar as verificações, a função `checar_seme` retorna uma mensagem indicando se a semelhança foi confirmada ou não, com base nos critérios especificados.
