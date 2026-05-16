from pygame import*

#window
background = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong game")
window.fill(background)










#FPS
clock = time.Clock()
FPS = 60










#game loop
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)