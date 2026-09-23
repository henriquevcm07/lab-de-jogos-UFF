from PPlay.sprite import Sprite

def executar_jogo(janela, teclado, width, height, dificuldade):
    nave = Sprite("./assets/nave--.png")
    nave.set_position(width / 2 - nave.width / 2, height - 100)
    vel = 200
    tiros = []
    cooldown = 0
    L = 3
    C = 6
    matriz_inimigos = [[None for _ in range(C)] for _ in range(L)]
    sentido = 1
    for i in range(L):
        for j in range(C):
            matriz_inimigos[i][j] = Sprite("./assets/monster.png")
            matriz_inimigos[i][j].set_position(\
                j*matriz_inimigos[i][j].width*1.5, \
                i*matriz_inimigos[i][j].height*1.5)

    while True:
        dt = janela.delta_time()  
        fps = int(1/dt) 
        if cooldown > 0:
            cooldown -= dt
            if cooldown < 0:
                cooldown = 0

        janela.set_background_color((0, 0, 0))

        if teclado.key_pressed("LEFT") and nave.x > 0:
            nave.x -= vel * dt
        if teclado.key_pressed("RIGHT") and nave.x + nave.width < width:
            nave.x += vel * dt

        if teclado.key_down("SPACE") and cooldown == 0:
            novo_tiro = Sprite("./assets/shot.png")
            novo_tiro.x = nave.x + nave.width / 2 - novo_tiro.width / 2
            novo_tiro.y = nave.y - nave.height / 2
            tiros.append(novo_tiro)
            cooldown = 0.3 *dificuldade

        for tiro in tiros[:]:
            tiro.y -= vel * dt
            if tiro.y + tiro.height < 0:
                tiros.remove(tiro)

        bateu_na_borda = False
        for linha in matriz_inimigos:
            for inimigo in linha:
                if inimigo is not None: 
                    if (inimigo.x <= 0 and sentido == -1) or (inimigo.x + inimigo.width >= width and sentido == 1):
                        bateu_na_borda = True
                        break
            if bateu_na_borda:
                break
        if bateu_na_borda:
            sentido *= -1
            for linha in matriz_inimigos:
                for inimigo in linha:
                    if inimigo is not None:
                        inimigo.y += 20
                
        for linha in matriz_inimigos:
            for inimigo in linha:
                if inimigo is not None:
                    inimigo.x += vel * dt * sentido
                    
        for tiro in tiros[:]:
            tiro_colidiu = False
            for i in range(L):
                for j in range(C):
                    inimigo = matriz_inimigos[i][j]
                    if inimigo is not None and tiro.collided(inimigo):
                        matriz_inimigos[i][j] = None
                        tiros.remove(tiro)
                        tiro_colidiu = True
                        break
                if tiro_colidiu:
                    break
        for linha in matriz_inimigos:
            for inimigo in linha:
                if inimigo is not None and inimigo.y + inimigo.height >= nave.y:
                    return 0
                    
        nave.draw()
        for tiro in tiros:
            tiro.draw()
        for linha in matriz_inimigos:
            for inimigo in linha:
                if inimigo is not None:
                    inimigo.draw()
                    
        janela.draw_text(f"fps: {fps}", 10, 10, size=20, color = (255,255,255),bold=True)
        if teclado.key_down("ESC"):
            return 0 

        janela.update()