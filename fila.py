class fila:
	def __init__(self):
		self.items = []
	def enqueue(self , item):
		return self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
	def isEmpty(self):
		return self.items == []
Fila = fila()
Fila.enqueue("Luan")
Fila.enqueue("fernando")
print(Fila.size())
print(Fila.items)
Fila.enqueue(9)
print(Fila.items)
print(Fila.dequeue())
print(Fila.items)
print(Fila.dequeue())
print(Fila.dequeue())
print(Fila.items)
print("A fila esta vazia ?",Fila.isEmpty())


