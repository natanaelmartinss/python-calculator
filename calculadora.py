
def interface():
    print("=========Calculadora==========")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potenciação")
    print("6. Raiz quadrada")
    print("7. Sair")

def info_receive():
    interface()
    operator = input("Selecione qual tipo de operação deseja realizar:")
    if operator not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Opção Invalida! Selecione uma válida:")
        return info_receive()
    
    if operator == "7":
        return operator, None, None

    try:
        a = float(input("Primeiro número da operação:"))
        if operator == "6":
            return operator, a, None
    except ValueError:
        print("Digite apenas números!")
        return info_receive()

    try:
        b = float(input("Segundo número da operação:"))
        if operator == "4":
            if b == 0:
                print("Impossível dividir qualquer número por zero!")
                return info_receive()
        return operator, a, b
    except ValueError:
        print("Digite apenas números!")
        return info_receive()


def operation(operator, a, b):
    match operator:

        case "1":
            result = a + b
            print(f"O resultado da sua operação é {result}!")
            
        case "2":
            result = a - b
            print(f"O resultado da sua operação é {result}!")

        case "3":
            result = a * b
            print(f"O resultado da sua operação é {result}!")

        case "4":
            result = a / b  
            print(f"O resultado da sua operação é {result}!")

        case "5":
            result = a ** b  
            print(f"O resultado da sua operação é {result}!")

        case "6":
            result = a ** 0.5 
            print(f"O resultado da sua operação é {result}!")

        case "7":
            print("Obrigado por utilizar!")

        case _:
            print("Opção inválida!")



def main():
    while True:
        operator, a, b = info_receive()
        operation(operator, a, b)
        if operator == "7":
            break

main()