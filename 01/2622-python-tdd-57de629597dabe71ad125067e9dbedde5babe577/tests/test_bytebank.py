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


    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        # Given
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)

        # When
        resultado = lucas.sobrenome()

        # Then - desfecho
        assert resultado == esperado




