"""Funcionamento do jogo Jo Ken Pô

Provê métodos para sortear uma opção para o PC (Nicole), além de um
que apura o jogo entre o jogador e a Nicole
"""

import random

__author__ = "Diego Mendes Rodrigues"
__copyright__ = "Copyright 2020, drSolutions - Agência Digital"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Diego Mendes Rodrigues"
__email__ = "diego [at] drsolutions.com.br"
__status__ = "Production"


class Jogo:
    """Funcionamento do jogo Jo Ken Pô"""

    def opcaoPc(self):
        """Sortear uma opção para o PC (Nicole)"""
        return random.randint(1, 3)

    def apurarVencedor(self, nomeJogador:str, opcaoJogador:int, opcaoPc:int):
        """Apurar se o vencedor é o jogador ou o PC (Nicole)"""
        jokenpo = ['Pedra', 'Papel', 'Tesoura']

        print(f'\n{nomeJogador}: {jokenpo[(opcaoJogador - 1)]} X '
              f'Nicole: {jokenpo[(opcaoPc - 1)]}\n')

        if opcaoJogador == opcaoPc:
            print('Empate entre você e a Nicole!\n')
        elif opcaoJogador == 1:
            if opcaoPc == 2:
                print('A Nicole ganhou!\n')
            elif opcaoPc == 3:
                print('Você ganhou!\n')
        elif opcaoJogador == 2:
            if opcaoPc == 3:
                print('A Nicole ganhou!\n')
            elif opcaoPc == 1:
                print('Você ganhou!\n')
        elif opcaoJogador == 3:
            if opcaoPc == 1:
                print('A Nicole ganhou!\n')
            elif opcaoPc == 2:
                print('Você ganhou!\n')
