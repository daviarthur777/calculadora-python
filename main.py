import operacoes 

while True:

 print("Bem-vindo à calculadora!")
 print("Escolha a operação:")
 print("1. Somar")
 print("2. Subtrair")
 print("3. Multiplicar")
 print("4. Dividir")


 opçao=int(input("Digite a opção desejada: "))

 if opçao in [1, 2, 3, 4]:
    num1 =float(input("Digite o primeiro número: "))
    num2 =float(input("Digite o segundo número: "))

    if opçao == 1:
        resultado = operacoes.somar(num1, num2)
        print(f"O resultado da soma é: {resultado}")
    elif opçao == 2:
        resultado = operacoes.subtrair(num1, num2)
        print(f"O resultado da subtração é: {resultado}")
    elif opçao == 3:
        resultado = operacoes.multiplicar(num1, num2)
        print(f"O resultado da multiplicação é: {resultado}")
    elif opçao == 4:
        if num2 == 0:
            print("Não é possível dividir por zero.")
        else:
            resultado = operacoes.dividir(num1, num2)
        print(f"O resultado da divisão é: {resultado}")
            
    

 else:
    print("opçao invalida.")

 continuar = input("Deseja continuar a operaçao? (s/n): ")
 if continuar=="n":
    print("Obrigado por usar a calculadora!")
    break


