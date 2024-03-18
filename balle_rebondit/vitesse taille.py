import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1240, 640))
clock = pygame.time.Clock()
running = True
dt = 0
taille = 10
r=100
v=200
b=0
velocitex = 5
velocitey = 5

rc = True
bc=True
vc=True

screen.fill("black")
pygame.draw.circle(screen, "white", (screen.get_width() / 2, screen.get_height() / 2), 300)
pygame.draw.circle(screen, "black", (screen.get_width() / 2, screen.get_height() / 2), 295)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

start = pygame.time.get_ticks()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    
    if rc:
        r= (r+1)
    else:
        r= (r-1)
    
    if vc:
        v= (v+3)
    else:
        v= (v-3)
    
    if bc:
        b= (b+5)
    else:
        b= (b-5)

    if b > 252:
        bc = False
    elif b< 4:
        bc = True

    if r > 254:
        rc = False
    elif r< 2:
        rc = True

    if v > 253:
        vc = False
    elif v< 3:
        vc = True

    if v<50 and r<50 and b<50:
        v+=24
        b+=40
        r+=15
    
    pygame.draw.circle(screen, "black", player_pos, taille+1)
    
    pygame.draw.circle(screen, (r,v,b), player_pos, taille)
    player_pos.y += velocitey
    player_pos.x += velocitex
    velocitey+=0.2
    print(velocitey+velocitex)

    if taille+1 + (295-taille*2)<math.sqrt((player_pos.x - screen.get_width() / 2)**2 + (player_pos.y - screen.get_height() / 2)**2):
        temp = velocitey
        pourcentx = (abs(player_pos.x - screen.get_width() / 2)/(271+taille)-1)*-1
        pourcenty = (abs(player_pos.y - screen.get_height() / 2)/(271+taille)-1)*-1
        pourcentx = pourcentx - pourcenty
        if pourcentx>1:
            pourcentx = 1
        elif pourcentx<-1:
            pourcentx = -1
        #print(pourcentx)
        print()
        taille +=0.1

        if player_pos.y>screen.get_height() / 2 and player_pos.x<= screen.get_width() / 2 or player_pos.y<=screen.get_height() / 2 and player_pos.x> screen.get_width() / 2 :
            current = pygame.time.get_ticks()
            if current - start >50:
                ok = True
                start = pygame.time.get_ticks()
            else : 
                ok = False
        
        if player_pos.y>screen.get_height() / 2 :
            if player_pos.x> screen.get_width() / 2 and velocitex+velocitey>0:
                velocitey = -velocitey * pourcentx + velocitex * (abs(pourcentx)-1)
            elif player_pos.x<= screen.get_width() / 2 and ok:
                velocitey = -velocitey * pourcentx - velocitex * (abs(pourcentx)-1)
        elif player_pos.y<=screen.get_height() / 2 :
            if player_pos.x> screen.get_width() / 2 and ok:
                velocitey = -(velocitey * pourcentx + velocitex * (abs(pourcentx)-1))
            elif player_pos.x<= screen.get_width() / 2 and velocitex+velocitey<0:
                velocitey = -(velocitey * pourcentx - velocitex * (abs(pourcentx)-1))

        if player_pos.y>screen.get_height() / 2 :
            if player_pos.x> screen.get_width() / 2 and velocitex+temp>0:
                velocitex = velocitex * pourcentx + temp * (abs(pourcentx)-1)
            elif player_pos.x<= screen.get_width() / 2 and ok:
                velocitex = velocitex * pourcentx - temp * (abs(pourcentx)-1)
        elif player_pos.y<=screen.get_height() / 2 :
            if player_pos.x> screen.get_width() / 2 and ok:
                velocitex = -(-velocitex * pourcentx + temp * (abs(pourcentx)-1))
            elif player_pos.x<= screen.get_width() / 2 and velocitex+temp<0:
                velocitex = -(-velocitex * pourcentx - temp * (abs(pourcentx)-1))

        velocitex = velocitex *1.21
        velocitey = velocitey *1.21

    

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()