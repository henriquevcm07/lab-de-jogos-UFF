from PPlay.window import Window
from PPlay.uikit import Button
from PPlay.keyboard import Keyboard
from PPlay.sprite import Sprite

width = 800
height = 640

teclado = Keyboard()
janela = Window(width,height,"Space Invaders",resizavel=False)
tela = 0
rodando = True
dificuldade = 1
while(rodando):
    match tela:
        case 0:
            btn_play = Button(200,50,"Iniciar",cor_base="darkgray")
            btn_diff = Button(200,50,"Dificuldade",cor_base="darkgray")
            btn_rank = Button(200,50,"Rankings",cor_base="darkgray")
            btn_ext = Button(200,50,"Sair",cor_base="darkgray")

            btn_rank.x = width/2 - btn_play.width/2
            btn_play.x = width/2 - btn_play.width/2
            btn_diff.x = width/2 - btn_play.width/2
            btn_ext.x = width/2 - btn_play.width/2

            btn_play.y = height/10 *2 - btn_play.height/2
            btn_diff.y = height/10 *4 - btn_play.height/2
            btn_rank.y = height/10 *6 - btn_play.height/2
            btn_ext.y = height/10 *8 - btn_play.height/2
            
            while True:
                janela.set_background_color((0,0,0))
                janela.update()
                btn_ext.draw()
                btn_play.draw()
                btn_rank.draw()
                btn_diff.draw()
                if btn_play.is_clicked():
                    tela = 1
                    break
                if btn_diff.is_clicked():
                    tela = 2
                    break
                if btn_ext.is_clicked():
                    rodando = False
                    break
                
        case 1:
            while True:
                janela.set_background_color((0,0,0))
                janela.update()
                
                if teclado.key_down("ESC"):
                    tela = 0
                    break
        case 2:
            
            btn_fac = Button(200,50,"Fácil",cor_base="darkgray")
            btn_med = Button(200,50,"Médio",cor_base="darkgray")
            btn_dif = Button(200,50,"Díficil",cor_base="darkgray")
            
            btn_fac.set_position(width/2 - btn_fac.width/2,height/5 *1 - btn_fac.height/2)
            btn_med.set_position(width/2 - btn_fac.width/2,height/5 *2 - btn_fac.height/2)
            btn_dif.set_position(width/2 - btn_fac.width/2,height/5 *3 - btn_fac.height/2)
            
            while True:
                janela.set_background_color((0,0,0))
                janela.update()
                if teclado.key_down("ESC"):
                    tela = 0
                    break
                if btn_fac.is_clicked():
                    dificuldade = 1
                    tela = 1
                    break
                if btn_med.is_clicked():
                    dificuldade = 2
                    tela = 1
                    break
                if btn_dif.is_clicked():
                    dificuldade = 3
                    tela = 1
                    break
                btn_fac.draw()
                btn_med.draw()
                btn_dif.draw()