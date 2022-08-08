import pygame
from random import randrange
from sound import play_sound

box = 32
resolution = 19 * box

x, y = randrange(box, resolution - box, box), randrange(box * 3, resolution - box, box)
apple = randrange(box, resolution - box, box), randrange(box * 3, resolution - box, box)

snake = [(x, y)]
length = 1

dx, dy = 0, 0 #directions of movement
movement = {"W": True, "S": True, "A": True, "D": True,}

fps = 5 #also governs the speed of the snake
score = 0

pygame.init()
screen = pygame.display.set_mode([resolution, resolution])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont("Arial", 26, bold=True)
end_score = pygame.font.SysFont("Arial", 66, bold=True)

background = pygame.image.load("./img/ground.png").convert()
food = pygame.image.load("./img/food.png").convert()

while True:
    screen.blit(background, (0, 0))
    #screen.fill(pygame.Color("black"))
    [(pygame.draw.rect(screen, pygame.Color("green"), (i, j, box - 1, box - 1))) for i, j in snake] #drawing the snake
    screen.blit(food, apple)
    #pygame.draw.rect(screen, pygame.Color("red"), (*apple, box, box)) #drawing the apple

    show_score = font_score.render(f"SCORE: {score}", 1, pygame.Color("orange"))
    screen.blit(show_score, (5, 5))

    x += dx * box
    y += dy * box
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(box, resolution - box, box), randrange(box * 3, resolution - box, box)
        play_sound(2, 0)
        length += 1
        fps += 1
        score += 1


    if x < box or x > 17 * box or y < 3 * box or y > 17 * box or len(snake) != len(set(snake)): #borders gameover check or eat itself gameover check
        play_sound(3, 0)
        while True:
            show_end = font_score.render("GAME OVER", 1, pygame.Color("orange"))
            screen.blit(show_end, (resolution // 2 - 60, resolution // 2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
        break


    pygame.display.flip() #surface update
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and movement["W"]:
        dx, dy = 0, -1
        play_sound(dx, dy)
        movement = {"W": True, "S": False, "A": True, "D": True, }
    if key[pygame.K_s] and movement["S"]:
        dx, dy = 0, 1
        play_sound(dx, dy)
        movement = {"W": False, "S": True, "A": True, "D": True, }
    if key[pygame.K_a] and movement["A"]:
        dx, dy = -1, 0
        play_sound(dx, dy)
        movement = {"W": True, "S": True, "A": True, "D": False, }
    if key[pygame.K_d] and movement["D"]:
        dx, dy = 1, 0
        play_sound(dx, dy)
        movement = {"W": True, "S": True, "A": False, "D": True, }

#if __name__ == '__main__':
#    print_hi('PyCharm')
