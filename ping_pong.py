from pygame import*



#GameSprite class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Player class
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_l] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_k] and self.rect.y < win_height - 500:
            self.rect.y += self.speed

#window
background = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong game")
window.fill(background)

#racket1
racket1 = Player('racket.png', 0, 100, 5, 100 , 150)



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
    racket1.update_l()


    racket1.reset()