import sys, pygame
pygame.init()




class judgmentarrows:
    def __init__(self, kind):
        

        self.kind = kind
        
        # spawn pos
        if kind == "left":
            
            self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.flip(self.image, True, False)
            self.x = 50
        elif kind == "down":
            self.image = pygame.image.load("arrow.png")
            self.x = 150
        elif kind == "up":
            self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.rotate(self.image, 90) 
            self.x = 250

        elif kind == "right":
            self.image = pygame.image.load("arrow.png")
            self.x = 350

        self.image = pygame.transform.scale(self.image, (200, 200))


class Arrow:
    def __init__(self, kind):
        

        self.kind = kind
        
        # spawn pos
        if kind == "left":
            
            self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.flip(self.image, True, False)
            self.x = 50
        elif kind == "down":
            self.image = pygame.image.load("arrow.png")
            self.x = 150
        elif kind == "up":
            self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.rotate(self.image, 90) 
            self.x = 250

        elif kind == "right":
            self.image = pygame.image.load("arrow.png")
            self.x = 350

        self.image = pygame.transform.scale(self.image, (200, 200))



#player instance
class player:
    def __init__(self):
        self.health = 100
        self.points = 0;





size = width, height = 1920, 1080
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

testimage = pygame.image.load("pochita")
testimage_rect = testimage.get_rect()






myarrow = Arrow("up")
img_with_flip = Arrow("up")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    testimage_rect = testimage_rect.move(speed)
   # if ballrect.left < 0 or ballrect.right > width:
    #    speed[0] = -speed[0]
   # if arrow1_rect.top < 0 or arrow1_rect.bottom > height:
   #     speed[1] = -speed[1]
    
  
   
    screen.fill(black)
    screen.blit(testimage, testimage_rect)
    screen.blit(img_with_flip.image, img_with_flip.image.get_rect())
    pygame.display.flip()
