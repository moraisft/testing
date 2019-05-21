def saudacao(nome,idade,naturalidade):
	print("Olá,",nome,"!\nTem",idade,"anos de idade\ne é natural de",naturalidade,".")

def cinema (idade):
	if idade < 12:
		print("Só pode ver filmes para menores de 12")
	elif idade > 12 and idade <18:
		print("Pode ver filmes para menores de 18")
	else
		print("Pode ver tudo")