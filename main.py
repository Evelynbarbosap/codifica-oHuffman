from ListaNo import ListaNo
from ArvoreCodigoHuffman import ArvoreCodigoHuffman

def openFile(file_name):	
	# pega o texto incial	
		try:
			file = open(file_name, "r")
			texto = file.read()
			file.close()
		except IOError:
			print ("Erro ao abrir o arquivo")
		return texto

########## Main ##############

lista = list(openFile("entrada.txt"))
x = ArvoreCodigoHuffman()
ListaNo = ListaNo(lista)
ListaNo.criaArv()
#caracter, frequencia, codigo
print(' caracter| Frequencia| Huffman code ')
print('-------------------------------------')
x.codificacao(ListaNo.raiz[0])
x.percorrer(ListaNo.raiz[0])

print("\n\nLista/texto original: ")
print(lista)
