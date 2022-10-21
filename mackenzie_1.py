import os

def main():
    os.system('cls')
    print('[1] Converter de binário/octal/hexadecimal para decimal\n[2] Converter de decimal para binário/octal/hexadecimal\n')
    select = int(input('Input: '))

    if select == 1:
        menu1()
    elif select == 2:
        menu2()
    else:
        main()

def menu1():
    os.system('cls')

    binario = lambda x: int(x, 2)
    octal = lambda x: int(x, 8)
    hexa = lambda x: int(x, 16)

    print('[1] Converter Binario \n[2] Converter Octal \n[3] Converter Hexadecimal\n[4] Voltar para o menu principal\n')

    opt = int(input('Opção: '))
    y= input('Valor: ')

    if opt == 1:
       print(binario(y))
    elif opt == 2:
        print(octal(y))
    elif opt == 3:
        print(hexa(y))
    elif opt == 4:
        main()
    else:
        menu1()
    
    os.system('pause')

def menu2():
    os.system('cls')
    print('[1] Converter para binário\n[2] Converter para octal\n[3] Converter para hexadecimal\n[4] Voltar para o menu principal\n')
    opt = int(input('Opção: '))
    z = int(input('Valor: '))

    if opt == 1:
       print(bin(z))
    elif opt == 2:
        print(oct(z))
    elif opt == 3:
        print(hex(z))
    elif opt == 4:
        main()
    else:
        menu2()
    
    os.system('pause')

while True:
    if __name__ == '__main__':
        main()