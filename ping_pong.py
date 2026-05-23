from pygame import *



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

        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()

        if keys[K_i] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_k] and self.rect.y < win_height - 150:
            self.rect.y += self.speed


#Window setup
background = (200, 255, 255)

win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong Game")

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSES!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSES!', True, (180, 0, 0))


#Create player
racket1 = Player('racket.png', 0, 100, 5, 50, 150)
racket2 = Player('racket.png', 540, 100, 5, 50, 150)

#ball
ball = GameSprite('ball.png', 200, 200, 5, 50, 50)

#FPS
clock = time.Clock()
FPS = 60

#ball speed
speed_x = 3
speed_y = 3

#Game loop
game = True
finish = False
while game:

    #Background refresh
    window.fill(background)

    #Events
    for e in event.get():
        if e.type == QUIT:
            game = False

    #Auto ball movement
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1
    
    #collisions with ball
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1

    #losing condition
    if ball.rect.x == 0:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x > 550:
        finish = True
        window.blit(lose2, (200, 200))


    #Update
    racket1.update_l()
    racket2.update_r()
    ball.update()

    #reset
    racket1.reset()
    racket2.reset()
    ball.reset()

    #Update screen
    display.update()

    #FPS limit
    clock.tick(FPS)