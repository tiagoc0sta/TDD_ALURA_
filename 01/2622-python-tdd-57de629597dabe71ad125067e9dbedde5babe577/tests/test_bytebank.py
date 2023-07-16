from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given - Contexto
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        # When - ação
        resultado = funcionario_teste.idade()

        # Then - desfecho
        assert resultado == esperado


    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho_(self):
        # Given
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)

        # When
        resultado = lucas.sobrenome()

        # Then - desfecho
        assert resultado == esperado


    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_9000(self):
        #Given
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        #When
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

