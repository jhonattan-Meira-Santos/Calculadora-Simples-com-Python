def Soma (num1,num2):
    Total=num1+num2
    return Total
def Subtracao (num1,num2):
    Total=num1-num2
    return Total
def Multiplicacao (num1,num2):
    Total=num1*num2
    return Total
def divisao (num1,num2):
    Total=num1/num2
    return Total
Iniciar = '2'
while Iniciar != 'sair':
    print('''Pressione o que deseja:
    1 - Calculadora simples
    2 - Sair do programa
    Escolha: ''')
    Opcao=int(input())
    if Opcao == 1:
        print("Tudo certo, agora digite os valores que você deseja calcular: ")
        Valor1= int(input())
        print("Segundo valor: ")
        Valor2= int(input())
        print('''Agora, escolha qual tipo de conta deseja fazer.
        Soma = +
        Subtração = -
        Multiplicação = *
        Divisão = /
        Digite o sinal: ''')
        sinal=input()
        if sinal == "+":
            print("o Resultado da soma entre ",Valor1,sinal,Valor2, "foi :",Soma(Valor1,Valor2))
        elif sinal == "-":
            print("o Resultado da soma entre ",Valor1,sinal,Valor2, "foi :",Subtracao(Valor1,Valor2))
        elif sinal == "*":
            print("o Resultado da soma entre ",Valor1,sinal,Valor2, "foi :",Multiplicacao(Valor1,Valor2))
        elif sinal =="/":
            print("o Resultado da soma entre ",Valor1,sinal,Valor2, "foi :",divisao(Valor1,Valor2))
        else:
            print("Você não digitou um sinal de operação válido, por favor insira novamente")
    if Opcao==2:
        print('Programa Finalizado')
        Iniciar='sair'