"""Interface do jogo Jó Ken Pô

Provê métodos para exibir cabeçalho, traços e informações para o jogador
"""

import os
from time import sleep

__author__ = "Diego Mendes Rodrigues"
__copyright__ = "Copyright 2020, drSolutions - Agência Digital"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Diego Mendes Rodrigues"
__email__ = "diego [at] drsolutions.com.br"
__status__ = "Production"


class Interface:
    """Interface do jogo Jó Ken Pô"""

    def cabecalho(self):
        """Limpar a tela e exibir o cabeçalho"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print('┌' + '─' * 50 + '┐')
        print('│' + 'Jó Ken Pô'.center(50) + '│█')
        print('└' + '─' * 50 + '┘█')
        print(' ' + '▀' * 52)

    def traco(self):
        """Exibir o traço de separação utilizado entre etapas do jogo"""
        print('─' * 53)

    def instrucoes(self, nome:str):
        """Exibir as instruções para o jogador"""
        print(f'\nOlá {nome}, meu nome é Nicole.'
              f'\n\nBem-vindo ao jogo Jó Ken Pô.\n')
        print('Você deverá selecionar sua escolha, digitando um\n'
              'número entre 1 e 3.\n\n'
              '1 - Papel\n'
              '2 - Tesoura\n'
              '3 - Pedra\n')

    def joKenPo(self):
        """Exibir JÓ KEN PÔ na tela"""
        print('\n' + 'J Ó'.center(53))
        sleep(0.7)
        print('K E N'.center(53))
        sleep(0.7)
        print('P Ô\n'.center(53))
        sleep(0.7)
