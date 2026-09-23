from PPlay.uikit import Button

def executar_menu(janela, width, height):
    btn_play = Button(200, 50, "Iniciar", cor_base="darkgray")
    btn_diff = Button(200, 50, "Dificuldade", cor_base="darkgray")
    btn_rank = Button(200, 50, "Rankings", cor_base="darkgray")
    btn_ext = Button(200, 50, "Sair", cor_base="darkgray")

    btn_play.x = width / 2 - btn_play.width / 2
    btn_diff.x = width / 2 - btn_play.width / 2
    btn_rank.x = width / 2 - btn_play.width / 2
    btn_ext.x = width / 2 - btn_play.width / 2

    btn_play.y = height / 10 * 2 - btn_play.height / 2
    btn_diff.y = height / 10 * 4 - btn_play.height / 2
    btn_rank.y = height / 10 * 6 - btn_play.height / 2
    btn_ext.y = height / 10 * 8 - btn_play.height / 2

    while True:
        janela.set_background_color((0, 0, 0))
        
        btn_play.draw()
        btn_diff.draw()
        btn_rank.draw()
        btn_ext.draw()

        if btn_play.is_clicked():
            return 1  
        if btn_diff.is_clicked():
            return 2  
        if btn_ext.is_clicked():
            return -1 
            
        janela.update()