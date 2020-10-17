#	Objetos dessa classe serão os nós para a árvore binária de Huffman.
	
#	conteudo - conteúdo que cada nó irá guardar um caractere;

#	frequencia - frequência de cada caractere no texto;

#	binario - código em binário que representa o caminho da raiz até dado nó;

#	esquerda - o filho da esquerda do nó;

#	direita - filho da direita;

#	isLeaf() - retorna true se o nó é uma folha da árvore.

class No:
	
	conteudo = 0
	binario = ""

	def __init__(self, conteudo, frequencia, binario, esquerda, direita):
		self.conteudo = conteudo
		self.frequencia = frequencia
		self.binario = binario
		self.esquerda = esquerda
		self.direita = direita

	def __repr__(self):
		return repr(( self.conteudo, self.frequencia, self.binario ))

	def isLeaf(self):
		return self.esquerda is None and self.direita is None