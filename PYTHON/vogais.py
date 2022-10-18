def corta_vogais(informacao):
    informacao.lower()
    vogais = "aeiou"
    for i in range(len(vogais)):
        informacao = informacao.replace(vogais[i],
        " ")
    print(informacao) 

corta_vogais(input("informe um nome ou frase: "))