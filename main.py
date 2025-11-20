#!/usr/bin/env python3
import os
import random
import pygame

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

if not pygame.font:
    print("Warning: fonts disabled")
if not pygame.mixer:
    print("Warning: sound disabled")


def load_image(name, colorkey=None, scale=1, use_alpha=False, hue_tint=None):
    fullname = os.path.join(data_dir, name)
    img = pygame.image.load(fullname)

    if use_alpha:
        image = img.convert_alpha()
    else:
        image = img.convert()

    if scale != 1:
        image = pygame.transform.scale_by(image, scale)

    if hue_tint is not None:
        # convert color name to RGB if necessary
        if isinstance(hue_tint, str):
            hue_tint = pygame.Color(hue_tint)[:3]  # get RGB tuple

        tint_surf = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        tint_surf.fill((*hue_tint, 0))  # RGB, alpha=0
        image.blit(tint_surf, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)

    return image


def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    return pygame.mixer.Sound(fullname)


class Arrow(pygame.sprite.Sprite):
    def __init__(self, direction, hue_tint=None):
        super().__init__()
        self.direction = direction

        img = load_image("arrow.png", use_alpha=True, hue_tint=hue_tint)
        img = pygame.transform.scale(img, (150, 150))  # scale down
        self.image = img

        screen_width, screen_height = pygame.display.get_surface().get_size()
        lane_spacing = 150
        ARROW_TYPES = ["LEFT", "DOWN", "UP", "RIGHT"]
        group_width = lane_spacing * (len(ARROW_TYPES) - 1)
        group_left = screen_width / 2 - group_width / 2
        i = ARROW_TYPES.index(direction)
        x = group_left + i * lane_spacing
        self.rect = self.image.get_rect(midtop=(x, screen_height))

        # hitbox
        hit_w, hit_h = 80, 60  # experiment with smaller size
        self.hitbox = pygame.Rect(0, 0, hit_w, hit_h)
        self.hitbox.center = self.rect.center


        # Choose orientation + x-position
        if direction == "LEFT":
            img = pygame.transform.flip(img, True, False)
        elif direction == "DOWN":
            img = pygame.transform.rotate(img, -90)
        elif direction == "UP":
            img = pygame.transform.rotate(img, 90)
        elif direction == "RIGHT":
            pass
        else:
            raise ValueError("Invalid arrow direction")

        img = pygame.transform.scale(img, (150, 150))

        self.image = img
        self.rect = self.image.get_rect(midtop=(x, screen_height))

    def update(self, dt, speed):
        self.rect.y -= speed * dt
        self.hitbox.y -= speed * dt  # move hitbox along with sprite
        if self.rect.bottom < -50:
            self.kill()
            return True
        return False



class Pochita(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = load_image("pochita.png", use_alpha=True)
        self.rect = self.image.get_rect()

        # Center him on the screen
        screen_w, screen_h = pygame.display.get_surface().get_size()
        self.rect.center = (screen_w // 2, screen_h // 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((1536, 914))
    pygame.display.set_caption("Dance Dance Revolution: Pochita Edition")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 48)

    background = load_image("background-3.png")

    # Groups
    all_sprites = pygame.sprite.Group()
    moving_arrows = pygame.sprite.Group()

    # Pochita
    pochita = Pochita()
    all_sprites.add(pochita)

    # Judgement arrows (static)
    judge_left = Arrow("LEFT")
    judge_down = Arrow("DOWN")
    judge_up = Arrow("UP")
    judge_right = Arrow("RIGHT")

    # Move judgement arrows to the top
    for j in (judge_left, judge_down, judge_up, judge_right):
        j.rect.y = 50
        all_sprites.add(j)

    ARROW_TYPES = ["LEFT", "DOWN", "UP", "RIGHT"]
    static_arrows = {
        "LEFT": judge_left,
        "DOWN": judge_down,
        "UP": judge_up,
        "RIGHT": judge_right
    }

    # Map keys to directions
    key_map = {
        pygame.K_a: "LEFT",
        pygame.K_s: "DOWN",
        pygame.K_w: "UP",
        pygame.K_d: "RIGHT",
    }

    score = 100
    spawn_timer = 0
    SPAWN_DELAY = 1.0
    ARROW_SPEED = 400

    def spawn_arrow():
        direction = random.choice(ARROW_TYPES)
        arrow = Arrow(direction, hue_tint="purple")
        all_sprites.add(arrow)
        moving_arrows.add(arrow)

    score = 100
    spawn_timer = 0
    SPAWN_DELAY = 1.0
    ARROW_SPEED = 400

    running = True
    dt = 0

    while running:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in key_map:
                    direction = key_map[event.key]
                    # check collisions
                    HIT_TOLERANCE = 75  # vertical window

                    for arrow in moving_arrows.sprites():
                        if arrow.direction != direction:
                            continue

                        static_rect = static_arrows[direction].rect
                        zone_top = static_rect.top - HIT_TOLERANCE
                        zone_bottom = static_rect.bottom + HIT_TOLERANCE

                        if arrow.hitbox.bottom >= zone_top and arrow.hitbox.top <= zone_bottom:
                            # Successful hit
                            moving_arrows.remove(arrow)
                            all_sprites.remove(arrow)
                            score += 10
                            break

        # Spawn arrows
        spawn_timer += dt
        if spawn_timer >= SPAWN_DELAY:
            spawn_arrow()
            spawn_timer = 0

        # Update arrows
        for arrow in moving_arrows.sprites():
            missed = arrow.update(dt, ARROW_SPEED)
            if missed:
                score -= 10

        # Score
        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.fill((0, 0, 0))             # optional black fill
        screen.blit(background, (0, 0))    # background
        all_sprites.draw(screen)           # sprites (Pochita + arrows)
        screen.blit(score_surf, (10, 10))  # score on top

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

    pygame.quit()


if __name__ == "__main__":
    main()
