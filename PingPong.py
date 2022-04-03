from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, spd=10, x=20, y=20, w=35, h=35):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.spd = spd
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        win.blit(self.image ,(self.rect.x, self.rect.y))

class Racket(GameSprite):
        def move1(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_UP] and self.rect.x > 0:
                self.rect.y -= self.spd
            if keys_pressed[K_DOWN] and self.rect.y < win_height-125:
                self.rect.y += self.spd
        def move2(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_w] and self.rect.x > 0:
                self.rect.y -= self.spd
            if keys_pressed[K_s] and self.rect.y < win_height-125:
                self.rect.y += self.spd

class Ball(GameSprite):
    def move(self):
        pass

win_width = 800
win_height = 400

win = display.set_mode((win_width, win_height))
display.set_caption('КАЛЬКУЛЯТОР.bat')

bg = transform.scale(image.load("DAaaa.png"), (win_width, win_height))

mixer.init()
mixer.music.load('shiiva-raw-castle.mp3')
mixer.music.play()
hit_sound = mixer.Sound('kick.wav')


Ball = Ball("Ball.png", 10, 350, 200, 40, 40)

racket1 = Racket("Platform.png", 10, 25, 140, 25, 90)
racket2 = Racket("platform2.png", 10, 750, 140, 25, 90)


FPS = 60
clock = time.Clock()
game = True
stop = False

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    win.blit(bg, (0,0))
    Ball.draw()
    Ball.update()
    racket1.draw()
    racket2.draw()
    racket1.move1()
    racket2.move2()
    
    display.update()
    clock.tick(FPS)