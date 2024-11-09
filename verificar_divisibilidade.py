# Utilizando Python, descubra se o número 5776 é divisível por 3. Justifique.
# Apesar do problema ser fácil quis dificultar a minha vida e me desafiar em criar um programa de divisibilidade

def solicitar_numero(num):
    while True:
        try:
            i = float(input(num))
            if i <= 0:
                print("Digite um número maior que zero!")
            else:
                return i
        except ValueError:
            print("Entrada inválida! Digite um valor válido")


def pergunta_loop():
    resposta = input("Você gostaria de repetir o programa? (S/N)").lower()
    return resposta == 's'


while True:

    num_1 = solicitar_numero("Digite o valor do primeiro número:")
    num_2 = solicitar_numero("Digite o valor do segundo número: ")

    if num_2 > num_1 or num_1 % num_2 != 0:
        print(num_1, "não é divisível por", num_2)
    else:
        print(num_1, "é divisível por", num_2)
    if not pergunta_loop():
        break
