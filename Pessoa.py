class Pessoa:
    def __init__(self):#Método construtor
        self.nome = ""
        self.telefone = ""
        self.endereco = ""

    #Métodos de acesso
    def getNome(self):
        return self.nome

    def getTelefone(self):
        return self.telefone

    def getEndereco(self):
        return self.endereco

    def setNome(self, nome):
        self.nome = nome

    def setTelefone(self, telefone):
        self.telefone = telefone

    def setEndereco(self, endereco):
        self.endereco = endereco

    #Cadastrar
    def cadastrar(self, nome, telefone, endereco):
        self.setNome(nome)
        self.setTelefone(telefone)
        self.setEndereco(endereco)

    #Consultar Pessoa
    def consultarTudo(self):
        return "Nome: {}\nTelefone: {}\nEndereço: {}".format(self.getNome(), self.getTelefone(), self.getEndereco())


