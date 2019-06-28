n = int( input( "Digite um número > 1: " ) )
 
if n <= 1:
    exit("Entre com um número > 1.")
 
a = 0
print(a)
 
b = 1
print(b)
 
i = 2
 
while i <= n:
    seq = b + a
 
    print(seq)
 
    a = b
    b = seq
 
    i = i + 1
 
print("Fim!")