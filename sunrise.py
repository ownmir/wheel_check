# здесь подключаются модули
import pygame

# здесь определяются константы, классы и функции
FPS = 30
WIN_WIDTH = 550
WIN_HEIGHT = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 150, 100)

# здесь происходит инициация, создание объектов и др.
pygame.init()

clock = pygame.time.Clock()

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# радиус и координаты круга
r = 30
x = WIN_WIDTH // 2
# x = 0 - r  # скрываем за левой границей
# y = WIN_HEIGHT // 2  # выравнивание по центру по вертикали
y = WIN_HEIGHT - r #
blue_part = 0
mid_part = 0
sc.fill(BLACK)

# если надо до цикла отобразить объекты на экране
# pygame.display.update()
pygame.display.set_caption("Sunrising")

# главный цикл
while True:
    # pygame.display.set_caption("Before")
    # задержка
    # clock.tick(FPS)


    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    # --------
    # изменение объектов и многое др.
    # --------

    # pygame.display.set_caption("Tick")
    # clock.tick(1)
    pygame.draw.circle(sc, ORANGE, (x, y), r)
    # обновление экрана
    pygame.display.update()

    # если полностью скрылся за правой границей
    if y <= 0 + r:
        y = WIN_HEIGHT - r
        break
    else:  # во всех остальных случаях
        y -= 1  # в следующем кадре круг сместится,
        # от значения зависит "скорость движения"
        # 
        
        if blue_part < 255:
            blue_part += 1
        else:
            blue_part = 255
            # clock.tick(5)
            if mid_part < 145:
                mid_part += 1
            else:
                mid_part = 145
        COLOR = tuple((0, mid_part, blue_part))
        sc.fill(COLOR)
        #if mid_part == 0:
        #    pygame.display.set_caption(str(blue_part))
        #else:
        #    pygame.display.set_caption(str(blue_part) + ' ' + str(mid_part))

    clock.tick(FPS)
    # pygame.display.set_caption("Tuck")
    # clock.tick(1)
    # pygame.display.update()


