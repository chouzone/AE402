# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:54:56 2020

@author: ruby8
"""


import pygame,random
#from math import pi

BLACK = (0,0,0)
WHITE = (255,255,255)
R = (255,0,0)
G = (0,255,0)
B = (0,0,255)

pygame.init()
size = (400,400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minecraft")
snow_list=[]
for i in range(50):
    x=random.randrange(0,400)
    y=random.randrange(0,400)
    snow_list.append([x,y])

done = False
clock = pygame.time.Clock()

draw= pygame.draw

while not done:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done = True
    
    #pygame.draw.rect(screen,B,(350,250,100,100),2) #矩行
    #pygame.draw.polygon(screen,R,((20,20),(30,30),(140,40)),10)
    for i in range(len(snow_list)):
        pygame.draw.circle(screen,WHITE,(snow_list[i]),2)
        snow_list[i][1]+=1
    
        if snow_list[i][1]>400:
            y=random.randrange(-50,-10)
            x=random.randrange(0,400)
            snow_list[i][0]=x
    
    
    
    
    pygame.display.flip()
    clock.tick(40)        
pygame.quit()

"""
def f(n):
    if n==1:
        return n
    else:
        return n*f(n-1)


print(f(5))
"""