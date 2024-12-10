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
        
        #Senão, o ponteiro proximo do elemento a ser inserido vai receber o topo da pilha. O topo da lista vai ser a caixa a ser inserida e  o tamanho aumenta.
        else:
            elemento.prox = self.top
            self.top = elemento
            self.size += 1
            return
        
    #Pra remover {TEM QUE SER O ITEM DO TOPO!!!}: elemento é o topo da lista. Atualizo o topo para a caixa que é o prox do elemento a ser deletado: (top.prox)
    def pop (self):
        elemento = self.top
        self.top = self.top.prox

        #Se o elemento a ser excluido for o unico, então atualizo o top da pilha para None
        if self.top == self.header:
            self.top = None
        return elemento
    
#Devo criar uma função para atualizar a pilha ?
    def atualizarPilha():
        #caso a paridade seja igual
        if ((caixa_anterior % 2) == 0 and (caixa_atual % 2) == 0) or (caixa_anterior % 2) != 0 and (caixa_atual % 2) != 0:
            caixa_atual.qtd_pacotes = caixaAtual.qtd_pacotes - caixaAnterior.qtd_pacotes #Lembrar de transformar em positivo, independente do resultado.
            #deletar a caixa anterior da pilha e adiciona caixa atual no topo 
            header = caixa_atual.qtd_pacotes

    

# no main eu devo pegar os inputs que especificam quantas pilhas serão processadas
#e as pilhas que virão sempre depois de uma linha vazia.

#fazer a recursao em cada pilha e entregar o re


