#!/usr/bin/python3

from random import randint , choice
import pygame




#classes
class drop:
    def __init__(self,surface , color , x, y , width , height ,gravity):
        self.surface = surface
        self.color = color 
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.time = 0
        self.g= gravity 
    def fall(self):
        self.y =int( self.y + (self.g/2)*self.time**2 )    
        if self.y > 700:
            self.y = -1*randint(300,1500)
            self.time = 0.03 
        self.time += 0.01
        pygame.draw.rect(self.surface , self.color ,[ self.x , self.y , self.width , self.height ])

#colors
#colors are in rgb (red , green , blue) format 
gloomywhite = (220 , 220 , 220 )
white = (255 , 255 , 255)
un = (230, 230, 250)
purple = ( 138, 43, 226 )
blue = ( 0 , 0 , 230 )
rainblue = (36, 113, 163 ) 
clock = pygame.time.Clock()
#

pygame.init()
gamedisplay = pygame.display.set_mode((900,600))
pygame.display.set_caption('PurpleRain')
pygame.display.update()

gameexit = False
is_keydown = False
drops = []
widths = [i for i in range(1,5)]
heights = [i for i in range(15,40,4)]
gravities = [ i for i in range(2,20,4)]
size = list(zip(widths , heights,gravities))

#making the rain drops
for i in range(500):
    x = randint(10,890)
    y = -1*randint(300 , 1500)
    width , height , g = choice(size) 
    raindrop = drop(gamedisplay , purple,x,y,width , height,g)  
    drops.append(raindrop)

#main loop
while not gameexit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameexit=True
     
    gamedisplay.fill(un)
        
    for d in drops:
        d.fall()        
    pygame.display.update()
    clock.tick(70)

pygame.display.quit()
quit()

