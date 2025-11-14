import sys, pygame, random
pygame.init()

# ================= IMG / CLASSES ===================


class judgmentarrows:
    def __init__(self, kind, type):
        self.kind = kind
        self.type = type

        if type == "activated":
            self.image = pygame.image.load("activatedarrow.png")
        else:
            self.image = pygame.image.load("arrow.png")

        if kind == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        elif kind == "down":
            self.image = pygame.transform.rotate(self.image, -90)
        elif kind == "up":
            self.image = pygame.transform.rotate(self.image, 90)
        elif kind == "right":
            pass

        self.image = pygame.transform.scale(self.image, (150, 150))


class Arrow:
    def __init__(self, kind):
        self.kind = kind

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


# ================= GAME SETUP ===================

size = width, height = 800, 900
black = 0, 0, 0
screen = pygame.display.set_mode(size)
bg = pygame.image.load("bg.png").convert()


#health
font = pygame.font.Font(None, 48)
score = 100;


# judgement arrows (top)
judge_left  = judgmentarrows("left", "unactivated")
judge_down  = judgmentarrows("down", "unactivated")
judge_up    = judgmentarrows("up", "unactivated")
judge_right = judgmentarrows("right", "unactivated")

pochita = pygame.image.load("pochita")

# arrow list
arrows = []

def spawn_arrow(kind):
    arrows.append(Arrow(kind))

arrowtypes = ["left", "right", "up", "down"]

# timing
clock = pygame.time.Clock()
spawn_timer = 0
SPAWN_DELAY = 1.0      # seconds
ARROW_SPEED = 400       # pixels per sec


# ================= GAME LOOP ===================

while True:
    dt = clock.tick(60) / 1000.0  # deltaTime in seconds
    score_text = font.render(f"Score: {score}", True, (255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    # spawn arrow every 10 seconds
    spawn_timer += dt
    if spawn_timer >= SPAWN_DELAY:
        spawn_arrow(random.choice(arrowtypes))
        spawn_timer = 0

    # draw background

    # draw static objects
    

    screen.fill(black)
    screen.blit(bg, (0, 0))

    # draw static objects
    screen.blit(pochita, (225, 150))
    screen.blit(score_text, (10, 850)) 
    # update + draw arrows
    for arrow in arrows[:]:
        arrow.y -= ARROW_SPEED * dt
        screen.blit(arrow.image, (arrow.x, arrow.y))

        if arrow.y < -100:
            arrows.remove(arrow)
            score -= 1


    # judgement arrows
    screen.blit(judge_left.image, (100, 0))
    screen.blit(judge_down.image, (250, 0))
    screen.blit(judge_up.image, (400, 0))
    screen.blit(judge_right.image, (550, 0))

    pygame.display.flip()
