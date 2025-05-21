id = 0
nome = ""
salario = 0.0
brasileiro = False
resposta = ""

id = int(input("DIgite o CPF sem pontos: "))
nome = input("Qual o seu nome? ")
salario = float(input("Digite o seu salário: "))

resposta = input("Você é Brasileiro? sim/nao ")
brasileiro = resposta == "sim"

if brasileiro:
    print("Você é Brasileiro!")

else:
    print("Você não é Brasileiro!")