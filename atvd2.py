# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.
def verificar_paridade(numero):
    if numero%2 == 0:
        return f"{numero} é um número par."
    else:
        return f"{numero} é um número ímpar."
    
n1 = int(input("escreva um número para verificar a sua paridade: "))

ver = verificar_paridade(n1)

print(ver)
    