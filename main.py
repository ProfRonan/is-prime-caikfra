number = int(input('Digite um número inteiro: '))
i = 1
while True:
    i = i + 1
    if number == 1:
        print("Não primo")
        break
    if number <=0:
        print("Número inválido")
        break
    if number % i ==0 and i !=number:
        print("Não primo")
        break
    if number % i ==0 and i ==number:
        print("Primo")
        break
