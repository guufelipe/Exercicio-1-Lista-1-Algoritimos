#Crio uma classe de caixas: Com variaveis pacotes e paridade(para indicar se é par ou ímpar), e ponteiro para a próxima caixa da pilha.
class caixa ():
    prox = None
    pacotes = 0
    paridade = ""
    def __init__(self,pacotes):
        self.pacotes = pacotes
        self.proxCaixa = None
        if self.pacotes % 2 == 0:
            self.paridade = "Pár"
        else:
            self.paridade = "Ímpar"


#Crio uma classe de pilha com as seguintes caracteristicas: header, top e size
class pilha (): 
    header = caixa()
    top = None
    size = 0  
    
    #Função de inserir, que para inserir uma nova caixa nessa pilha, atualiza alguns elementos:    
    def inserir(self, elemento):

        #Se for o primeiro item a ser inserido, o topo da pilha vai ser o elemento(caixa) a ser inserido.
        #   O ponteiro de proximo do topo da pilha vai receber o header dessa pilha e aumento 1 no tamanho da pilha
        if self.top == None:
            self.top = elemento
            self.top.prox = self.header
            self.size += 1
            return  
        
        #Senão, o ponteiro proximo do elemento a ser inserido vai receber o topo da pilha. O topo da pilha vai ser a caixa a ser inserida e 
        # o tamanho aumenta.
        else:
            #Quando a paridade forem iguais eu crio um novo objeto com os valores atualizados e o coloco no topo da lista substituindo o
            #  anterior.
            if elemento.paridade == self.top.paridade:
                novaCaixa = ((elemento.pacotes - self.top.pacotes))
                novaCaixa.prox = self.top.prox
                self.top = novaCaixa
            else:
                elemento.prox = self.top
                self.top = elemento
                self.size += 1
                return
        
    #Pra remover {TEM QUE SER O ITEM DO TOPO!!!}: elemento é o topo da lista. Atualizo o topo para a caixa que é o prox do elemento a ser
    #  deletado: (top.prox)
    def pop (self):
        elemento = self.top
        self.top = self.top.prox

        #Se o elemento a ser excluido for o unico, então atualizo o top da pilha para None
        if self.top == self.header:
            self.top = None
        return elemento
    

def main():

    t = int(input())
    for i in range(0, t):
        pilha = pilha()
        pacotes = -1


        while (pacotes != 0):
            pacotes = int(input())
            caixa = caixa(pacotes)
            #caixa.pacotes = pacotes
            pilha.inserir(caixa)


main()


