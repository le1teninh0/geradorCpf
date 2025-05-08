from random import randint

def menu():
   print("""
    =*=*=*=*=*=*=*=*=*=*=
     1 - Gerar CPF
     2 - Verificar CPF
     0 - Sair
    =*=*=*=*=*=*=*=*=*=*=
    """)

def calculaDigitos(cpf):
    numeros = cpf
    soma = 0
    digitos = ""
    for i in range(9):
        soma += int(numeros[i]) * (10 - i)
    digito1 = "0" if (soma * 10) % 11 > 9 else str((soma * 10) % 11)
    numeros += digito1

    soma = 0
    for i in range(10):
        soma += int(numeros[i]) * (11 - i)
    digito2 = "0" if (soma * 10) % 11 > 9 else str((soma * 10) % 11)
    numeros += digito2

    return numeros[9::]


def gerarCPF():
    cpf = ''
    while len(cpf) <= 8:
        numero = str(randint(0, 9))
        cpf += numero

    cpf += calculaDigitos(cpf)
    
    return cpf

def validarCPF(cpf):
    numeros = cpf[:9]
    digitos = cpf[9::]
    return True if digitos ==  calculaDigitos(numeros) else False

while True:
    menu()
    escolha = int(input("Opção: "))
    if escolha == 0:
        break
    elif escolha == 1:
        print(gerarCPF())
    elif escolha == 2:
        cpf = input("Digite o CPF(xxx.xxx.xxx-xx): ").replace(".", "").replace("-", "")
        valido = validarCPF(cpf)
        print("CPF válido" if valido else "CPF inválido")
