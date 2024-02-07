'''Declarando a variável para o usuário
digitar o valor a ser convertido'''
valorInserido = input("fala garoto: ")

'''Declarando o vetor que irá receber os módulos (restos)
das divisões e que irá representar o número binário, já convertido'''
binario = []

i = 0

'''Por questões do Python, o valor inserido pelo usuário
será convertido em inteiro'''
valorDecimal = int(valorInserido)

'''Nesta condicional, enquanto o valor decimal for maior do
que 1, as divisões continuarão a ser realizadas, e os módulos
da divisão serão acumuladas no vetor.'''
while (valorDecimal > 1):
    binario.append(int(valorDecimal % 2))
    valorDecimal = valorDecimal / 2
    i += 1
    

if(valorDecimal == 1):
    binario.append(int(valorDecimal))
    
binario.reverse()
    
print (binario)
print ("Nº de iterações: ", i)
