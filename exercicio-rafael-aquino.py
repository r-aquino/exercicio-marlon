# Crie um repositório com o nome de sua preferência no github e deixe-o público.
# Faça os exercícios a seguir (pesquise a vontade e tente bastante, é assim que se aprende):
# Faça um Programa que converta metros para centímetros.
# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
# Envie os exercícios pro seu github, copie o link do repositório e cole-o aqui.

medidaemmetro = float(input("Insira o valor em metros: "))
medidaemcentimetro = medidaemmetro * 100
print("O valor em cm é:", medidaemcentimetro)

sexo = input("Insira o sexo: M-masculino ou F-feminino: ")

while sexo != "F" and sexo != "f" and sexo != "M" and sexo != "m":
    print("Sexo inválido")
    sexo = input("Insira apenas M ou F para o sexo: M-masculino ou F-feminino: ")

if sexo == "F" or sexo == "f":
    print("Sexo feminino")
elif sexo == "M" or sexo == "m":
    print("Sexo masculino")

usuario, senha = input("Insira um nome de usuário: "), input("Insira uma senha: ")

while usuario == senha: 
    print("A senha não pode ser igual ao nome de usuário. ")
    usuario, senha = input("Insira um nome de usuário: "), input("Insira uma senha: ")

print("Cadastro realizado!")

