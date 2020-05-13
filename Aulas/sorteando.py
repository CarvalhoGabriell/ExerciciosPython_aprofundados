import random

nome1 = input("Qual o priemiro aluno? ")
nome2 = input("Qual o segundo aluno? ")
nome3 = input("Qual o terceiro aluno? ")
nome4 = input("Qual o quarto aluno? ")
nome5 = input("Qual o quinto aluno? ")

listaNomes = [nome1,nome2,nome3,nome4,nome5]

random.shuffle(listaNomes)

print("A ordem do sorteio para a aprentação é: ")
print(listaNomes)