class Empregado:

    def __init__(self, nome, salario):
        self.__nome = nome
        self._salario = salario

    def getNome(self):
        return self.__nome

    def setNome(self, name):
        self.__nome = name

    def getSalario(self):
        return self._salario
    
    def setSalario(self, valor):
        self._salario = valor