class stack:
    #inicializamos a pilha
    def __init__(self):
        self.items = []
    #funcao para deletar um item da pilha
    def pop(self ,item):
        self.items.remove(item)
        return item
    #funcao para adicionar o item na lista
    def push(self, item):
        self.items.append(item)
    #funcao para verificar se a pilha esta vazia , se vazia retorna true
    def isEmpty(self):
        return self.items == []
    #funcao para mostrar o tamanho da pilha
    def size(self):
        return len(self.items)
    #funcao para mostrar o item do topo
    def peek(self):
        return self.items[len(self.items)-1]
pilha = stack()

pilha.push(7)
pilha.push(8)
pilha.push(9)
pilha.push(10)
pilha.push(11)
pilha.push(12)
print("Tamanho da Pilha",pilha.size())
print("Topo da Pilha",pilha.peek())
print(pilha.pop(12))
print("Tamanho da Pilha",pilha.size())
print("Topo da Pilha",pilha.peek())
print("A pilha esta FALSE(Contem itens) TRUE(Vazia) :",pilha.isEmpty())
