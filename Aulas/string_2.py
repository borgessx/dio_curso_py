nome = "Gabriel"
idade = 18
profissao = "Aux Administrativo"
liguagem = "Python"
saldo = 50.46756

dados = {"nome":"Gabriel","idade":18,"saldo":50.46756}

print("Nome: %s Idade: %d" %(nome,idade))
print("Nome: {} Idade: {}" .format(nome,idade))
print("Nome: {1} Idade: {0}" .format(nome,idade))
print("Nome: {1} Idade: {0}" .format(nome,idade))
print("Nome: {0} {0} Idade: {1} Nome: {0}" .format(nome,idade))
print("Nome: {Name} Idade: {Age}" .format(Name=nome,Age=idade))
print("Nome: {nome} Idade: {idade}" .format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:0.2f}#mesma coisa de :.2f")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")