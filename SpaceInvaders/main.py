from PPlay.window import Window
from PPlay.keyboard import Keyboard

from menu import executar_menu
from game import executar_jogo
from diff import executar_dificuldade

janela = Window(800, 600)
teclado = Keyboard()
width = janela.width
height = janela.height

tela = 0
dificuldade = 1
rodando = True

while rodando:
    match tela:
        case 0:
            tela = executar_menu(janela, width, height)
            if tela == -1:
                rodando = False
                
        case 1:
            tela = executar_jogo(janela, teclado, width, height, dificuldade)
            
        case 2:
            proxima_tela, nova_dif = executar_dificuldade(janela, teclado, width, height)
            tela = proxima_tela
            if nova_dif is not None:
                dificuldade = nova_dif

janela.close()