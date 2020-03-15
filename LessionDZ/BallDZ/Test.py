import sys, pygame, math


class Ball:
    def __init__(self, points, obj):
        self.x, self.y = points
        self.ball_rect = obj.get_rect()
        self.circle = obj
        self.pull = False
        self.was = [False, False]
        self.harm = None
        self.speed = [40, 40]

def check_distance (b1, b2):
    d = (abs(b1.ball_rect.center[0] - b2.ball_rect.center[0])**2 + abs(b1.ball_rect.center[1] - b2.ball_rect.center[1])**2)**0.5
    return d <= abs(2 * math.sqrt(2) * (b1.ball_rect.right - b1.ball_rect.center[0]))


pygame.init()
screen_size = width, height = 1280, 720
size = width / 0.1, height / 0.1
DX, DY = 0.1, 0.1
black = 0, 0, 0


def convert(x, y):
    return (math.floor(x * DX), math.floor(y * DY))


pygame.time.set_timer(pygame.USEREVENT, 10)

screen = pygame.display.set_mode(screen_size)
AmBalls = []
Positions = [(size[0]/4, size[1]/4), (size[0]*3/4, size[1]/4),(size[0]/4, size[1]*3/4), (size[0]*3/4, size[1]*3/4)]
for i in range(len(Positions)):
    AmBalls.append(Ball(Positions[i], pygame.image.load("intro_ball.gif")))

while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        sys.exit()
    else:
        for b in AmBalls:
            if event.type == pygame.MOUSEBUTTONDOWN and b.ball_rect.collidepoint(event.pos) and not b.pull:
                b.pull = True
            elif event.type == pygame.MOUSEMOTION and b.pull:
                b.x, b.y = event.pos[0] / DX, event.pos[1] / DY
            elif event.type == pygame.MOUSEBUTTONUP and b.pull:
                b.pull = False
            elif event.type == pygame.USEREVENT:
                b.x, b.y = b.x + b.speed[0], b.y + b.speed[1]
                if b.ball_rect.left < 0 or b.ball_rect.right > width:
                    b.harm=None

                    if not b.was[0]:
                        b.speed[0] = -b.speed[0]
                        b.was[0] = True
                else:
                    b.was[0] = False
                if b.ball_rect.top < 0 or b.ball_rect.bottom > height:
                    b.harm=None
                    if not b.was[1]:
                        b.speed[1] = -b.speed[1]
                        b.was[1] = True
                else:
                    b.was[1] = False
        for b1 in range(len(AmBalls)):
            for b2 in range(b1, len(AmBalls)):
                # if (AmBalls[b1].ball_rect.left == AmBalls[b2].ball_rect.right or AmBalls[b1].ball_rect.right == AmBalls[b2].ball_rect.left) and b1!=b2 and check_distance(AmBalls[b1], AmBalls[b2]) and (AmBalls[b1].harm!=AmBalls[b2] or AmBalls[b2].harm!=AmBalls[b1]):
                if (abs(AmBalls[b1].ball_rect.left - AmBalls[b2].ball_rect.right) < 5 or abs(AmBalls[b1].ball_rect.right - AmBalls[b2].ball_rect.left) <5) and b1!=b2 and check_distance(AmBalls[b1], AmBalls[b2]) and (AmBalls[b1].harm!=AmBalls[b2] or AmBalls[b2].harm!=AmBalls[b1]):
                    AmBalls[b1].speed[0] = -AmBalls[b1].speed[0]
                    AmBalls[b2].speed[0] = -AmBalls[b2].speed[0]
                    AmBalls[b1].harm=AmBalls[b2]
                    AmBalls[b2].harm=AmBalls[b1]
                elif ((abs(AmBalls[b1].ball_rect.top-AmBalls[b2].ball_rect.bottom)<5 or abs(AmBalls[b1].ball_rect.bottom - AmBalls[b2].ball_rect.top)<5))and b1!=b2 and check_distance(AmBalls[b1], AmBalls[b2]) and (AmBalls[b1].harm!=AmBalls[b2] or AmBalls[b2].harm!=AmBalls[b1]):
                    AmBalls[b1].speed[1] = -AmBalls[b1].speed[1]
                    AmBalls[b2].speed[1] = -AmBalls[b2].speed[1]
                    AmBalls[b1].harm=AmBalls[b2]
                    AmBalls[b2].harm=AmBalls[b1]
    screen.fill(black)
    for b in AmBalls:
        new_coords = convert(b.x,b.y)
        b.ball_rect.center = new_coords
        screen.blit(b.circle,b.ball_rect)

    pygame.display.flip()
