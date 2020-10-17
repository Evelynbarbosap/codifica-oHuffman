#	Essa classe guardará uma lista com todos os caracteres do texto lido, cada caractere vai ser atribuído a um nó e ordenados em ordem crescente de frequência. A partir dessa lista ordenada será criada a árvore binária.

#	raiz - será uma lista de objetos da classe No, mas quando a árvore estiver formada seu primeiro e único elemento será a raiz da árvore;

#	texto - uma lista de caracteres que representa todo o texto, é usado para gerar a lista e o texto em binário.

#	insereRaiz() - insere um objeto na raiz/cabeça da lista;

#	insere() - insere um objeto no fim da lista, mas se houver algum objeto com o mesmo caractere então só incrementa a frequência desse objeto,  um sorted() é usado para deixar a lista sempre ordenada em ordem crescente de frequência;

#	criaLista() - cria uma lista de caracteres a partir do texto, instancia os objetos No e insere com os métodos anteriores;

#	printLista() - imprime na tela, um a um, os objetos guardados na lista;

#	criaArv() - cria a Árvore de Huffman. Primeiro, chama o método para criar a lista e a partir da lista formada começa a criação da árvore.
#		Cria-se um novo objeto da classe No, sem caractere, com a frequência sendo a soma da frequência dos dois primeiros elementos das listas e seus filhos da esquerda e direita são, respectivamente, esses dois primeiros elementos da lista. Os dois primeiros elementos são retirados da lista e o objeto criado anteriormente é inserido na lista.


from No import No

class ListaNo:

	raiz = 0
	texto = ''

	def __init__(self, lista):
		self.texto = lista

	def insereRaiz(self, novo):	
	#insere o primeiro elemento da lista
		self.raiz = [novo] 
		return

	def insere(self, novo):
	#insere o elemento no fim da lista
		for item in self.raiz:
			if item.conteudo == novo.conteudo:	
			# se houver outro elemento na lista com o mesmo caractere
				item.frequencia += 1					
				# a frequência é incrementada
				self.raiz = sorted(self.raiz, key=lambda no: no.frequencia) 
				# e a lista reordenada
				return							
				# e finaliza o for

		self.raiz += [novo]				
		# se não, o novo objeto é inserido
		self.raiz= sorted(self.raiz, key=lambda no: no.frequencia) 
		# e a lista reordenada
		
		return

	def criaLista(self):
		for caracter in self.texto:
			if self.raiz == 0:
			# se a lista está vazia
			# insere o primeiro elemento
				self.insereRaiz(No(caracter,1,'', None, None)) 
				# para guardar o caractere em si

			else: 
			# se não, insere o elemento nomalmente
				self.insere(No(caracter,1,'', None, None)) 
				# para guardar o caractere em si

		return

	def printLista(self): 
		# exibe cada elemento separadamente
		for tup in self.raiz:
			print (tup)
		
		return

	def criaArv(self):
		
		self.criaLista()	
		# chama o método para a criar a lista

		while len(self.raiz)>1:
		# esse laço executa até restar apenas um elemento na lista, que será a raiz da árvore

			novo = No("",self.raiz[0].frequencia + self.raiz[1].frequencia,'',self.raiz[0],self.raiz[1])	
			# cria o nó intermediário

			#deleta os dois primeros elementos			
			del self.raiz[0]	
			del self.raiz[0]

			self.raiz += [novo]	#insere o nó intermediário na lista
			self.raiz = sorted(self.raiz, key=lambda no: no.frequencia) # reordena a lista

		return