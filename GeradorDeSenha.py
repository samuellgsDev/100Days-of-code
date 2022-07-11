# Dia 5
# Crie um gerador de senhas que gere senhas em ordem aleatória.
import random
from typing import List, Any

dados_letra: list[str | Any] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dados_numero: list[str] = ['0','1','2','3','4','5','6','7','8','9']
dados_caractere: list[str | Any] = ['!','@','#','$','%','&','*','(',')','_','+','=','{','}','[',']','|','\\',';',':','"','<','>','?','.','/']
letra = int(input("Com quantas letras você quer sua senha ? "))
simbolos = int(input("Com quantos simbolos voce quer sua senha ? "))
numeros = int(input("Com quantos numeros voce quer a sua senha ? "))
senha = []
for i in range(letra):
    senha.append(dados_letra[random.randint(0,25)])
for i in range(simbolos):
    senha.append(dados_caractere[random.randint(0,25)])
for i in range(numeros):
    senha.append(dados_numero[random.randint(0,9)])
random.shuffle(senha)
nova_senha = ''.join(senha)
print(nova_senha)
