"""
Jogo Jo Ken Pô
"""

import Interacao as jkpInteracao
import Interface as jkpInterface
import Jogo as jkpJogo

__author__ = "Diego Mendes Rodrigues"
__copyright__ = "Copyright 2020, drSolutions - Agência Digital"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Diego Mendes Rodrigues"
__email__ = "diego [at] drsolutions.com.br"
__status__ = "Production"

# Instânciar as classes
interface = jkpInterface.Interface()
interacao = jkpInteracao.Interacao()
jogo = jkpJogo.Jogo()

# Exibir o cabeçalho
interface.cabecalho()

# Solicitar o nome do jogador
nome = interacao.solicitarNome()
interface.traco()

# Exibir as intruções, opção do jogador e selecionar a opção do PC (Nicole)
interface.instrucoes(nome)
opcaoJogador = interacao.opcao()
opcaoPc = jogo.opcaoPc()

# Exbibir JO KEN PÔ
interface.traco()
interface.joKenPo()
interface.traco()

# Apurar o vencedor
jogo.apurarVencedor(nome, opcaoJogador, opcaoPc)
interface.traco()
