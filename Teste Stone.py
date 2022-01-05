despesas = [] #lista com todas as informacoes de despesas da viagem
valoresPessoas = {} #dicionario que irá receber o nome e os valores de cada pessoa
indicador = 1 #indica se a pessoa deseja continuar incluindo valores da viagem ou nao
print('Olá! \nVamos comecar a contar as despesas da viagem\n')

while indicador == 1:
    print('Informe as seguintes informacoes:')
    valoresPessoas['despesa'] = str(input('Nome da despesa: ')) #variável para receber o nome da pessoa
    if valoresPessoas['despesa'] == '':
            while valoresPessoas['despesa'] == '':
                valoresPessoas['despesa'] = str(input('Digite um nome para a despesa: '))
    nPessoas = int(input('Quantas pessoas estarao incluidas na despesa? ')) #numero de pessoas que estao incluidas
    pessoas = [] #lista com as pessoas
    for i in range(0, nPessoas):
        pessoa = str(input('Nome da pessoa: ')) #nome da pessoa
        if pessoa == '':
            while pessoa == '':
                pessoa = str(input('Digite um nome valido para a pessoa: '))
        pessoas.append(pessoa.lower().capitalize())
    valoresPessoas['nomes'] = []
    valoresPessoas['nomes'].extend(pessoas) #inclui a lista de nomes da pessoas no dicionario
    quantidade = int(input('Quantidade de itens comprados ou servico contratado: ')) #variável para receber a quantidade do que foi comprado
    valorUnitario = abs(int(input('Digite o valor unitário em centavos: '))) #variável para receber o valor unitário do que foi comprado/contratado
    valorPorPessoa = []
    for i in range(0, nPessoas - 1):
        p = int(valorUnitario*abs(quantidade)/nPessoas) #preco para cada pessoa
        valorPorPessoa.insert(i, p)
    valorPorPessoa.insert(nPessoas, (valorUnitario*abs(quantidade) - p*(nPessoas-1)))
    valoresPessoas['valorPorPessoa'] = []
    valoresPessoas['valorPorPessoa'].extend(valorPorPessoa) #inclui a lista de valores por cada pessoa no dicionario
    despesas.append(valoresPessoas.copy())

    indicador = int(input('Deseja adicionar mais despesas? Digite o número correspondente ao que deseja \n 1 - Sim \n 2 - Nao \n'))

    if indicador != 1 and indicador != 2: #caso a pessoa digite algo diferente das opcoes apresentadas a ele, a pessoa entrará no seguinte loop:
        while indicador != 1 and indicador != 2: #dentro desse loop, só sairá quando digitar uma das opcoes:
            indicador = int(input('Informe uma das opcoes: \n 1 - Sim \n 2 - Nao \n'))

todasPessoas = [] #lista com o nome de todas as pessoas incluidas em alguma despesa
for i in range(0, len(despesas)):
    todasPessoas = todasPessoas + despesas[i]['nomes']
todasPessoas = list(set(todasPessoas))

cadaUmDeve = [] #lista que receberá um dicionario com as informacoes de cada pessoa
quantoCadaUmDeve = {} #dicionario para receber os nomes, os valores de quanto cada um deve, e quais foram suas despesas

for i in range(0, len(todasPessoas)):
    deve = 0 #variavel que irá acumular a soma dos valores devedores
    for n in range(0, len(despesas)):
        for m in range(0, len(despesas[n]['nomes'])):
            if todasPessoas[i] == despesas[n]['nomes'][m]:
                quantoCadaUmDeve[todasPessoas[i]] = deve + despesas[n]['valorPorPessoa'][m] #atribui o valor devedor à key, que, nesse caso, é o nome da pessoa
                deve += despesas[n]['valorPorPessoa'][m]
cadaUmDeve.append(quantoCadaUmDeve.copy())

print(cadaUmDeve) #mostra a lista de dicionarios exigido no teste: com a chave (o nome da pessoa) e seu respectivo valor devedor

for k, v in quantoCadaUmDeve.items():
    print('{} deve pagar: R${:.2f}'.format(k, v/100))
