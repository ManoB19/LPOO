from empregado import Empregado
from gerente import Gerente, Vendedor

def main():
    try:
        funcionario = Empregado('Eberson', 1000)
        print(f'Empregado: {funcionario.getNome()}')
        print(f'Salário do empregado: {funcionario.getSalario()}')
        funcionario.setSalario(1500)
        print(f'Novo salário: {funcionario.getSalario()}')
        print('*' * 30)

        chefe = Gerente('Baruc', 1500, 'TI')
        print(f'Chefe: {chefe.getNome()}')
        print(f'Salário do chefe: {chefe.getSalario()}')
        print(f'Departamento: {chefe.getDepartamento()}')
        chefe.setSalario(8000)
        print(f'Novo salário: {chefe.getSalario()}')
        print('*' * 30)

        vendedor = Vendedor('Mano Brown', 1000, 10)
        print(f'Vendedor: {vendedor.getNome()}')        
        print(f'Salário do vendedor: {vendedor.getSalario()}')
        print(f'Comissão: {vendedor.getPercentualComissao()}')
        vendedor.setSalario()
        print(f'Salário com comissão: {vendedor.getSalario()}')

    except:
        print("Erro")

if __name__ == "__main__":
    main()