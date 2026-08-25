from PPlay.sprite import Sprite
from PPlay.window import Window
from PPlay.keyboard import Keyboard

width = 800
height = 600

velpad = 425
velbola = 500 

janela = Window(width,height,'Pong')
bola = Sprite("./assets/circle-16.png")
teclado = Keyboard()
bola.set_position(width/2 - bola.width/2,height/2 - bola.height/2)
vely = 0
velx = 0

pad1 = Sprite("./assets/Pad.png",1)
pad1.set_position(30, height/2 - pad1.height/2)
pad2 = Sprite("./assets/Pad.png",1)
pad2.set_position(width - 30 - pad2.width,height/2 - pad2.height/2)

contador1 = 0
contador2 = 0

while True:
    dt = janela.delta_time()
    centro2 = pad2.y + pad2.height/2
    centro1 = pad1.y + pad1.height/2
    centroBolax = bola.x + bola.width/2
    centroBolay = bola.y + bola.height/2
    
    
    if bola.y < 0:
        bola.y = 0
        vely *= -1 
    if bola.y + bola.height > height:
        bola.y = height - bola.height
        vely *= -1

    if bola.x <= 0:
        bola.x = width/2
        bola.y = height/2
        velx = 0 
        vely = 0
        contador1 += 1
    if bola.x + bola.width >= width:
        bola.x = width/2
        bola.y = height/2
        velx = 0
        vely = 0
        contador2 += 1
    
    if bola.collided(pad1):
        bola.x = pad1.x + pad1.width
        velx *= -1.05
    if bola.collided(pad2):
        bola.x = pad2.x -bola.width
        velx *= -1.05

    if bola.y - bola.height > centro2 and centro2 +pad2.height/2 < height:
        pad2.y += velpad * dt
    if bola.y + bola.height < centro2 and centro2 -pad2.height/2 > 0:
        pad2.y -= velpad * dt
        

    if teclado.key_pressed("SPACE") and velx == 0:
        velx = -velbola
        vely = velbola
    if teclado.key_pressed("DOWN") and pad1.y + pad1.height <= height:
        pad1.y += velpad *dt
    if teclado.key_pressed("UP") and pad1.y >= 0:
        pad1.y -= velpad *dt
    
    bola.y += vely * dt
    bola.x += velx * dt
    
    janela.set_background_color((0,0,255))   
    janela.update()
    bola.draw()   
    pad1.draw()   
    pad2.draw()
    janela.draw_text(contador2,width/4,height/10,tamanho= 50, cor=(255,255,255))
    janela.draw_text(contador1,3*width/4,height/10,tamanho= 50, cor=(255,255,255))