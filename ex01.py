#Vai receber uma pilha de caixas empilhadas, e cada caixa vai armazenar o valor de quantos pacotes estão contidas na caixa.

# Devemos analisar a paridade entre o novo elemento e o que vem antes dele e caso eles tenham a mesma paridade ambas devem ser substituida por uma nova caixa
# Que agora tem a quantidade de pacotes igual a diferença entre os pacotes da caixa anterior e da caixa nova. (qtds_pacotes_novo - qtd_pacotes_anterior)


#Criando a classe que vai representar cada caixa definindo como atributos: Quantidade de pacotes na caixa e o direcionamento para a caixa que vem abaixo dela
class caixa:
    qtd_pacotes = 0
    caixa_anterior = None

    def _init_ (self, qtd_pacotes):
        self.caixa_anterior = None
        self.qtd_pacotes = qtd_pacotes
    
#Criar a classe pilha com as funções de atualizarpilha para conseguir subtrair a qtd de pacotes da caixa do topo com a que vem logo em seguida.
#E essa atualização deve ocorrer enquanto a paridade entre o primeiro item e o seguinte sejam iguais.
class pilha:
    top = None
    size = 0

#Na função de atualizar a pilha eu devo criar a lógica para subtrair os valores dos dois ultimos itens da pilha e atualizar o header da pilha para dar continuidade de forma recursiva
    def atualizarlista():
        #caso a paridade seja igual
        if ((caixa_anterior % 2) == 0 and (caixa_atual % 2) == 0) or (caixa_anterior % 2) != 0 and (caixa_atual % 2) != 0:
            caixa_atual.qtd_pacotes = caixaAtual.qtd_pacotes - caixaAnterior.qtd_pacotes #Lembrar de transformar em positivo, independente do resultado.
            #deletar a caixa anterior da pilha e adiciona caixa atual no topo 
            header = caixa_atual.qtd_pacotes

    

# no main eu devo pegar os inputs que especificam quantas pilhas serão processadas
#e as pilhas que virão sempre depois de uma linha vazia.

#fazer a recursao em cada pilha e entregar o re


