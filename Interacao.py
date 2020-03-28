"""Integração entre o jogador e o jogo Jó Ken Pô

Provê métodos para solicitar o nome do jogador, solicitar a opção no jogo
"""

__author__ = "Diego Mendes Rodrigues"
__copyright__ = "Copyright 2020, drSolutions - Agência Digital"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Diego Mendes Rodrigues"
__email__ = "diego [at] drsolutions.com.br"
__status__ = "Production"


class Interacao:
    """Integração entre o jogador e o jogo Jó Ken Pô"""

    def solicitarNome(self):
        """Solicitar o nome do jogador"""
        nome = ''
        while True:
            nome = input('\nQual o seu nome?\n')
            if len(nome) > 0:
                break

        print('')
        return nome.split()[0].title()

    def opcao(self):
        """Solicitar a opção do Jó Ken Pô do jogador"""
        opcao = 0
        while opcao not in [1, 2, 3]:
            try:
                opcao = int(input('Qual sua opção?\n'))
            except:
                pass
        print('')
        return opcao
