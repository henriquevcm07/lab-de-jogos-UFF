from PPlay.uikit import Button

def executar_dificuldade(janela, teclado, width, height):
    btn_fac = Button(200, 50, "Fácil", cor_base="darkgray")
    btn_med = Button(200, 50, "Médio", cor_base="darkgray")
    btn_dif = Button(200, 50, "Díficil", cor_base="darkgray")

    btn_fac.set_position(width / 2 - btn_fac.width / 2, height / 5 * 1 - btn_fac.height / 2)
    btn_med.set_position(width / 2 - btn_fac.width / 2, height / 5 * 2 - btn_fac.height / 2)
    btn_dif.set_position(width / 2 - btn_fac.width / 2, height / 5 * 3 - btn_fac.height / 2)

    janela.update()  # descarta o clique que veio da tela anterior

    while True:
        janela.set_background_color((0, 0, 0))

        btn_fac.draw()
        btn_med.draw()
        btn_dif.draw()

        if teclado.key_down("ESC"):
            return 0, None  

        if btn_fac.is_clicked():
            return 1, 1  
        if btn_med.is_clicked():
            return 1, 2
        if btn_dif.is_clicked():
            return 1, 3

        janela.update()