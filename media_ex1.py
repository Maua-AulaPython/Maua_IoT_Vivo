N = 3

def soma(x, y): 
	return x+y

def media(soma, quant):
    return soma/quant
    
def entrada():
	return int(input("Digite uma nota: "))

x = entrada()
y = entrada()
z = entrada()

print('media das 3 notas: ', (media(soma(soma(x, y), z), N)))

# Nota: 0.7
# Comentario: O que acontece se a media nao for um numero inteiro? considerando a elegancia do codigo.
