import sys, pygame
pygame.init()

#bg = pygame.image.load("bg.png") #.convert()




class judgmentarrows:
    def __init__(self, kind):
        

        self.kind = kind
        
        # spawn pos
        if kind == "left":
            
            self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.flip(self.image, True, False)
            
            #self.x = 50
        elif kind == "down":
            self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.rotate(self.image, -90) 
          #  self.x = 150
        elif kind == "up":
            self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.rotate(self.image, 90) 
           # self.x = 250

        elif kind == "right":
            self.image = pygame.image.load("arrow.png")
           # self.x = 350

        self.image = pygame.transform.scale(self.image, (150, 150))


class Arrow:
    def __init__(self, kind):
        

        self.kind = kind
        
        # spawn pos
        if kind == "left":
            
            self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.flip(self.image, True, False)
            self.x = 100
        elif kind == "down":
            self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.rotate(self.image, -90) 
            self.x = 250
        elif kind == "up":
            self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.rotate(self.image, 90) 
            self.x = 400

        elif kind == "right":
            self.image = pygame.image.load("arrow.png")
            self.x = 550
        
        self.y = 900
        self.image = pygame.transform.scale(self.image, (150, 150))



#player instance
class player:
    def __init__(self):
        self.health = 100
        self.points = 0;





size = width, height = 800, 900
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
bg = pygame.image.load("bg.png").convert()

testimage = pygame.image.load("pochita")
testimage_rect = testimage.get_rect()



#judgementarrows

# create judgement arrows for each direction and helper list
judge_left = judgmentarrows("left")
judge_down = judgmentarrows("down")
judge_up = judgmentarrows("up")
judge_right = judgmentarrows("right")




myarrow = Arrow("up")
pochita =  pygame.image.load("pochita")

#img_with_flip = Arrow("left")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


        


   # testimage_rect = testimage_rect.move(speed)
   # if ballrect.left < 0 or ballrect.right > width:
    #    speed[0] = -speed[0]
   # if arrow1_rect.top < 0 or arrow1_rect.bottom > height:
   #     speed[1] = -speed[1]
    

    
    
  
    myarrow.y -=5
    screen.fill(black)
    screen.blit(bg, (0,0))

  

    screen.blit(pochita, (225, 150))
    screen.blit(myarrow.image, (myarrow.x, myarrow.y))

    


  # judgement arrows, do not edit
    screen.blit(judge_left.image, (100, 0))
    screen.blit(judge_down.image, (250, 0))
    screen.blit(judge_up.image, (400, 0))
    screen.blit(judge_right.image, (550, 0))

    if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT: pygame.draw.rect(screen, black, (0, 400, 700, 300))
         elif event.key == pygame.K_DOWN: sys.exit()
         elif event.key == pygame.K_UP: sys.exit()
         elif event.key == pygame.K_RIGHT: sys.exit()
   
   
    pygame.display.flip()
