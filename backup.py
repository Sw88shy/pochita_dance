import sys, pygame, random
pygame.init()

#bg = pygame.image.load("bg.png") #.convert()




class judgmentarrows:
    def __init__(self, kind, type):
        
        nothing = 0
        self.kind = kind
        self.type = type
        

        if type == "activated":
            self.image = pygame.image.load("activatedarrow.png")
        else:
            self.image = pygame.image.load("arrow.png")

        
        # spawn pos
        if kind == "left":
            
            #self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.flip(self.image, True, False)
            
            #self.x = 50
        elif kind == "down":
           # self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.rotate(self.image, -90) 
          #  self.x = 150
        elif kind == "up":
           # self.image = pygame.image.load("arrow.png")
            self.image = pygame.transform.rotate(self.image, 90) 
           # self.x = 250

        elif kind == "right":
            nothing = 0
            #self.image = pygame.image.load("arrow.png")
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





#judgementarrows

# create judgement arrows for each direction and helper list
judge_left = judgmentarrows("left","unactivated")
judge_down = judgmentarrows("down", "unactivated")
judge_up = judgmentarrows("up", "unactivated")
judge_right = judgmentarrows("right", "unactivated")

judge_left_activated = judgmentarrows("left", "activated")
judge_down_activated = judgmentarrows("down", "activated")
judge_up_activated = judgmentarrows("up", "activated")
judge_right_activated = judgmentarrows("right", "activated")




pochita =  pygame.image.load("pochita")

arrows = []

def spawn_arrow(kind):
    arrows.append(Arrow(kind))


arrowtypes = ["left", "right", "up", "down"]
last_spawn_time = 0
SPAWN_DELAY = 10000  


#img_with_flip = Arrow("left")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
        
        
        
   
          

    current_time = pygame.time.get_ticks()
    spawn_arrow(arrowtypes[random.randint(0, 3)])
    screen.fill(black)
    screen.blit(bg, (0,0))

    for arrow in arrows[:]:            # iterate over a shallow copy so we can remove safely
        arrow.y -= 10     
        screen.blit(arrow.image, (arrow.x, arrow.y)) 
        if arrow.y < -150:   # remove off screen
            arrows.remove(arrow)           # move arrow upward; change speed here if desired
  

    screen.blit(pochita, (225, 150))
    


    


  # judgement arrows, do not edit
    screen.blit(judge_left.image, (100, 0))
    screen.blit(judge_down.image, (250, 0))
    screen.blit(judge_up.image, (400, 0))
    screen.blit(judge_right.image, (550, 0))

   
    pygame.display.flip()
