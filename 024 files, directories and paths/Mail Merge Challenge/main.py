names = []

with open("Input/Names/invited_names.txt") as nomes:
    for name in nomes:
        names.append(name.strip())




with open("Input/Letters/starting_letter.txt") as carta:
    texto = carta.read()




for name in names:
    with open(f"Output/ReadyToSend_for_{name}.txt", "w") as newFile:
        novoTexto=texto.replace('[name]', f'{name}')
        newFile.write(novoTexto)