import pygame, sys
import random

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

screen = pygame.display.set_mode((800,800))
clock  = pygame.time.Clock()

fps = 120

def update_caption():
    pygame.display.set_caption("biball | fps: "+str(round(clock.get_fps())))

def get_compliment():
    compliment = f"Eh, not far, only {len(balls)} balls."
    if len(balls) == 1:
        compliment = f"1 BALL. YOU'RE SERIOUS."
    if len(balls) >= 100:
        compliment = f"Oh ok! Not that far from achievement, you got {len(balls)} balls!"
    if len(balls) >= 200:
        compliment = f"{len(balls)} BALLS?! HOW DID YOUR COMPUTER HANDLE THAT?!"
    if len(balls) >= 300:
        compliment = f"{len(balls)} balls. Your desktop would be overflowing."
    if len(balls) >= 400:
        compliment = f"Why and how. Why {len(balls)} balls and how {len(balls)} balls."
    if len(balls) >= 500:
        compliment = f"BALLS! {len(balls)} BALLS!"
    if len(balls) >= 600:
        compliment = f"nah nah nah ur crazy bruh like {len(balls)} balls DAMN"
    if len(balls) >= 700:
        compliment = f"{len(balls)} balls, what a shipping nightmare. (like if they were meatballs in case you were worried)"
    if len(balls) >= 800:
        compliment = f"{len(balls)} balls... {808 - len(balls)} {'ball' if 800-len(balls)==1 else 'balls'} to go before you reach 808. >:D"
    if len(balls) == 808:
        compliment = f"Aw, yeah. 808 balls. What a chad, bro >:D"
    if len(balls)  > 808:
        compliment = f"Dang... Just {len(balls) - 808} balls past 808... >:("
    if len(balls) >= 900:
        compliment = f"YOOO JUST {1000 - len(balls)} {'BALL' if 1000-len(balls)==1 else 'BALLS'} AWAY FROM 1000!"
    if len(balls) >= 1000:
        compliment = f"BROOOOOOOOO YOU MADE IT TO {len(balls)} LITTERALLY {len(balls) - 1000} ABOVE 1000!"
    return compliment

bounce_counter_thingy = 0
bct_max = 50

class Ball:
    def __init__(self,x,y,s,grav):
        print("Ball created! Starting X,Y: "+str(x)+","+str(y)+", Ball "+str(len(balls)+1))
        self.x = x
        self.y = y
        self.s = s
        self.grav = grav
        self.dx = 0
        self.dy = self.grav
    def redraw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.s)
    def update(self):
        global bounce_counter_thingy, bct_max
        self.dy += self.grav
        if self.x <= 0:
            self.dx += (self.grav*5)-(self.dx/8)
            bounce_counter_thingy += 1
            if bounce_counter_thingy >= bct_max:
                balls.append(Ball(random.randrange(0,screen.get_width()),random.randrange(0,screen.get_height()),15,grav))
                bounce_counter_thingy = 0
        if self.x >= screen.get_width()-(self.s/2):
            self.dx -= (self.grav*5)-(self.dx/8) # Emulate loss of energy
            bounce_counter_thingy += 1
            if bounce_counter_thingy >= bct_max:
                balls.append(Ball(random.randrange(0,screen.get_width()),random.randrange(0,screen.get_height()),15,grav))
                bounce_counter_thingy = 0
        if self.y <= 0:
            self.dy += (self.grav*5)-(self.dy/6) # Emulate loss of energy but less energy lost
            bounce_counter_thingy += 1
            if bounce_counter_thingy >= bct_max:
                balls.append(Ball(random.randrange(0,screen.get_width()),random.randrange(0,screen.get_height()),15,grav))
                bounce_counter_thingy = 0
        if self.y >= screen.get_height()-(self.s/2):
            self.dy -= (self.grav*5)-(self.dx/6) # Emulate loss of energy but less energy lost
            bounce_counter_thingy += 1
            if bounce_counter_thingy >= bct_max:
                balls.append(Ball(random.randrange(0,screen.get_width()),random.randrange(0,screen.get_height()),15,grav))
                bounce_counter_thingy = 0
        self.x += self.dx
        self.y += self.dy
    def boost(self,dx,dy):
        self.dx += dx
        self.dy += dy

boostAmount = 0
grav = 3

# dont take the name of this list out of context
balls = []

balls.append(Ball(100,100,15,grav))

keyDown = True

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            print("See ya! - Method of closing: CLOSE BUTTON - "+get_compliment())
            running = False
        if e.type == pygame.KEYDOWN:
            keyDown = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                for ball in balls:
                    ball.boost(0,boostAmount)
            elif e.key == pygame.K_DOWN:
                for ball in balls:
                    ball.boost(0,-boostAmount)
            elif e.key == pygame.K_LEFT:
                for ball in balls:
                    ball.boost(-boostAmount,0)
            elif e.key == pygame.K_RIGHT:
                for ball in balls:
                    ball.boost(boostAmount,0)
            elif e.key == pygame.K_SPACE:
                balls.append(Ball(random.randrange(0,screen.get_width()),random.randrange(0,screen.get_height()),15,grav))
            elif e.key == pygame.K_RETURN:
                for i in range(1,boostAmount,1):
                    balls.append(Ball(random.randrange(0,screen.get_width()),random.randrange(0,screen.get_height()),15,grav))
            elif e.key == pygame.K_ESCAPE:
                print("See ya! - Method of closing: ESCAPE - "+get_compliment())
                running = False
            elif e.key == pygame.K_r:
                compliment = f"Eh, not far, only {len(balls)} balls."
                if len(balls) == 1:
                    compliment = f"1 BALL. YOU'RE SERIOUS."
                if len(balls) >= 100:
                    compliment = f"Oh ok! Not that far from achievement, you got {len(balls)} balls!"
                if len(balls) >= 200:
                    compliment = f"{len(balls)} BALLS?! HOW DID YOUR COMPUTER HANDLE THAT?!"
                if len(balls) >= 300:
                    compliment = f"{len(balls)} balls. Your desktop would be overflowing."
                if len(balls) >= 400:
                    compliment = f"Why and how. Why {len(balls)} balls and how {len(balls)} balls."
                if len(balls) >= 500:
                    compliment = f"BALLS! {len(balls)} BALLS!"
                if len(balls) >= 600:
                    compliment = f"nah nah nah ur crazy bruh like {len(balls)} balls DAMN"
                if len(balls) >= 700:
                    compliment = f"{len(balls)} balls, what a shipping nightmare. (like if they were meatballs in case you were worried)"
                if len(balls) >= 800:
                    compliment = f"{len(balls)} balls... {808 - len(balls)} {'ball' if 800-len(balls)==1 else 'balls'} to go before you reach 808. >:D"
                if len(balls) == 808:
                    compliment = f"Aw, yeah. 808 balls. What a chad, bro >:D"
                if len(balls)  > 808:
                    compliment = f"Dang... Just {len(balls) - 808} balls past 808... >:("
                if len(balls) >= 900:
                    compliment = f"YOOO JUST {1000 - len(balls)} {'BALL' if 1000-len(balls)==1 else 'BALLS'} AWAY FROM 1000!"
                if len(balls) >= 1000:
                    compliment = f"BROOOOOOOOO YOU MADE IT TO {len(balls)} LITTERALLY {len(balls) - 1000} ABOVE 1000!"
                balls = []
                bounce_counter_thingy = 0
                boostAmount = 0
                print("Simulation reset! "+compliment)
            keyDown = False
            boostAmount = 0
    update_caption()
    screen.fill(BLACK)
    for ball in balls:
        ball.update()
        ball.redraw()
    if boostAmount != 0:
        screen.blit(pygame.font.SysFont("Arial", 20).render(str(boostAmount), True, WHITE, BLACK),(0,0))
    if keyDown:
        boostAmount += 1
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit(0) # criminal
