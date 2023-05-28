def isEmpty(list):
    return len(list) == 0


Estados = ['EMPILHAR', 'DESEMPILHAR', 'FINAL']
estado = Estados[0]
cadeia = "abbaXabba"
pilha = []
pos = 0
valor = str()

while pos <= len(cadeia) -1:

    valor = cadeia[pos]
    if(not isEmpty(pilha)):
        topoPilha = pilha[0]
        print(f'Estado Atual: {estado}')
        print(f'Pilha: {pilha}')

    if(estado == Estados[0]):

        if(isEmpty(pilha) and valor == 'a'):
            pilha.insert(0,'Y')
            pos += 1

        elif(topoPilha == 'X' and valor == 'b'):
            pilha.insert(0,'Y')
            pos += 1 

        elif(topoPilha ==  'X' and valor == 'a'):
            pilha.insert(0,'X')
            pos += 1

        elif(topoPilha == 'Y' and valor == 'a'):
            pilha.insert(0,'X')
            pos += 1

        elif(topoPilha == 'Y' and valor == 'b'):
            pilha.insert(0,'Y')
            pos += 1
            
        else: 
            pos += 1
            estado = Estados[1]
    elif(estado == Estados[1]):

        if(topoPilha == 'X' and valor == 'a'):
            pilha.pop(0)
            pos += 1

        elif(topoPilha == 'X' and valor == 'b'):
            pilha.pop(0)
            pos += 1

        elif(topoPilha == 'Y' and valor == 'a'):
            pilha.pop(0)
            pos += 1

        elif(topoPilha == 'Y' and valor == 'b'):
            pilha.pop(0)
            pos += 1

        elif(isEmpty(pilha)):
            estado = Estados[2]
            break

        else: 
            print('Cadeia não aceita.')

print('Cadeia escolhida pertece a linguagem de L = { wXwr | w pertece a {a|b}* e wr é w invertido}' )
pos += 1




    