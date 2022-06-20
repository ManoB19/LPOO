from empregado import Empregado

class Gerente(Empregado):

    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.__departamento = departamento

    def getDepartamento(self):
        return self.__departamento
    
    def setDepartamento(self, local):
        self.__departamento = local

class Vendedor(Empregado):

    def __init__(self, nome, salario, percentualComissao):
        super().__init__(nome, salario)
        self.__percentualComissao = percentualComissao

    def getPercentualComissao(self):
        return (self.__percentualComissao/100)
    
    def setPercentualComissao(self, valor):
        self.__percentualComissao = valor

    def setSalario(self):
        return super().setSalario(self.getSalario() * ( 1 + self.getPercentualComissao()))