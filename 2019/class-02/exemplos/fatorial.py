
n = int( input( "Digite um número no intervalo [1, 10]: " ) )
 
if (n >= 1) and (n <= 10):
 
    fat = 1
    
    while n > 1:
        fat = fat * n
        n = n - 1
 
    print("fatorial:", fat)
 
else:
    print("Número fora do intervalo [1, 10].")
    print("Rode o programa novamente!")
