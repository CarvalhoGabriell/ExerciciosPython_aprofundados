import random
import emoji
num1 = random.random()  ## Esse método retorna um numero FLOAT entre 0 e 1.
num = random.randint(1,99)  ## Esse método retorna um numero aleatorio INTEIRO.
print(num1)
print(num)

print(emoji.emojize(" Qual é seu nome? :moyai:", use_aliases=True))


nomes = ['Gabriel', 'Fernanda', 'Cleybson']  ## Criando uma lista com STRINGS
escolhido = random.choice(nomes)

print("O sorteado foi {}".format(escolhido))




