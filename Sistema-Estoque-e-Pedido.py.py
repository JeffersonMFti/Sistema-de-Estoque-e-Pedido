#Sistema Estoque/Pedido Jefferson Monteiro

class Estoque:
    itens = {}
    def incluir(self, c, d, p):
        self.itens.update({ c :[d, p]})

    def excluir(self, c):
        self.itens.pop(c)

    def descricao(self, c):
        return self.itens[c][0]

    def preco(self, c):
        return self.itens[c][1]

    def listar(self):
        print("-----------------------------")
        for c in self.itens:
            print(c, self.descricao(c), self.preco(c))
        print("-----------------------------")

class Pedido:
    def __init__(self, n, c):
        self.numero = n
        self.cliente = c
        self.total = 0
        self.itens = []

    def incluir(self, c, d, q, p):
        self.itens.append([c, d, q, p])
        self.total += (q * p)

    def listar(self):
        n = 0
        print("-----------------------------")
        print("N.o:", self.numero, "Cliente:")
        print("-----------------------------")
        for c, d, q, p in self.itens:
            print(n, c, d, q, p)
            n += 1
        print("-----------------------------")
        print("Total:", self.total)
        print("-----------------------------")

    def excluir(self, n):
        self.itens.pop(n)
        self.total = 0
        for c, d, q, p in self.itens:
            self.total += (q * p)

#Inicio do Programa

e = Estoque()
pd = Pedido(100, "Antonio")

pSair = False

while not pSair:
    opcao = input("[PRINCIPAL] Selecione <E>stoque <P>edido <S>air")

    if opcao.upper() == "S":
        pSair = True
    elif opcao.upper() == "E":
        sSair = False
        while not sSair:
            opcao = input("[ESTOQUE] Selecione <I>ncluir <E>xcluir <L>istar <V>oltar")
            if opcao.upper() == "V":
                sSair = True
            elif opcao.upper() == "I":
                c = input("Codigo:")
                d = input("Descricao:")
                p = float(input("Preco:"))
                e.incluir(c, d, p)
            elif opcao.upper() == "E":
                c = input("Codigo:")
                e.excluir(c)
            elif opcao.upper() == "L":
                e.listar()
            else:
                print("Opção Invalida")

    elif opcao.upper() == "P":
        sSair = False
        while not sSair:
            opcao = input("[PEDIDO] Selecione <I>ncluir <E>xcluir <L>istar <V>oltar")
            if opcao.upper() == "V":
                sSair = True
            elif opcao.upper() == "I":
                c = input("Codigo:")
                q = int(input("Qtde:"))
                pd.incluir(c, e.descricao(c), q, e.preco(c))
                e.incluir(c, d, p)
            elif opcao.upper() == "E":
                n = int(input("N.o Item:"))
                pd.excluir(n)
            elif opcao.upper() == "L":
                pd.listar()
            else:
                print("Opção Invalida")
        else:
            print("Opção Invalida")

print(">>>>> Programa Finalizado")
