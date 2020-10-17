class ArvoreCodigoHuffman:
	#é só para debug
	# navega pela árvore e imprime os elementos em pré-ordem
	def percorrer(self, no):
		if no is None: 
		#se o nó for null
			return

		if no.esquerda is not None:  
		#se o nó da esquerda for null
			self.percorrer(no.esquerda) 
			#percorrer para esquerda da arvore
		
		if no.isLeaf(): 
		#se encontrar o nó desejado
			print (no)  
			#printa o nó
		
		if no.direita is not None: 
			# se o nó da direita não for null 
			self.percorrer(no.direita)  
			# percorre para a direita da arvore

	
	def codificacao(self,no):
		# gera o código em binário para cada nó da árvore
		# esse código representa o caminho da raiz até o dado nó
		if no is None: 
			return

		if no.esquerda is not None:
			# sempre que for para a esquerda, concatena '1' ao código do filho
			no.esquerda.binario = no.binario +'1'	
			self.codificacao(no.esquerda)

		if no.direita is not None:
			# sempre que for para a direita, concatena '0' ao código do filho
			no.direita.binario = no.binario + '0'	
			self.codificacao(no.direita)

		return


		