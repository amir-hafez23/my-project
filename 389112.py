import pygame
import math

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pattern Lock - PyGame")

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (100, 100, 255)
GREEN = (0, 255, 100)
RED = (255, 0, 0)

# ساخت ۹ نقطه
RADIUS = 25
points = []
for y in range(3):
    for x in range(3):
        px = 100 + x * 100
        py = 150 + y * 100
        points.append({'x': px, 'y': py, 'touched': False})

# رمز پیش‌فرض (با اندیس صفرشده: مثلاً 1→2→3 یعنی [0, 1, 2])
PASSWORD = [0, 1, 2]
pattern = []
dragging = False
msg = ""

def reset_pattern():
    global pattern, dragging
    for p in points:
        p['touched'] = False
    pattern = []
    dragging = False

def distance(p1, p2):
    return math.hypot(p1['x'] - p2['x'], p1['y'] - p2['y'])

def get_point_index_at_pos(pos):
    for i, p in enumerate(points):
        if distance({'x': pos[0], 'y': pos[1]}, p) < RADIUS + 10 and not p['touched']:
            return i
    return None

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # رسم خطوط بین نقاط انتخاب‌شده
    if len(pattern) >= 2:
        for i in range(len(pattern)-1):
            a = points[pattern[i]]
            b = points[pattern[i+1]]
            pygame.draw.line(screen, BLUE, (a['x'], a['y']), (b['x'], b['y']), 4)

    # رسم خط تا موس
    if dragging and pattern:
        last_point = points[pattern[-1]]
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, GRAY, (last_point['x'], last_point['y']), mouse_pos, 2)

    # رسم نقاط
    for i, p in enumerate(points):
        color = GREEN if p['touched'] else GRAY
        pygame.draw.circle(screen, color, (p['x'], p['y']), RADIUS)

    # پیام پایین
    font = pygame.font.SysFont(None, 32)
    text = font.render(msg, True, RED if msg == "Wrong!" else GREEN)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            reset_pattern()
            dragging = True
            idx = get_point_index_at_pos(event.pos)
            if idx is not None:
                pattern.append(idx)
                points[idx]['touched'] = True

        elif event.type == pygame.MOUSEMOTION and dragging:
            idx = get_point_index_at_pos(event.pos)
            if idx is not None:
                pattern.append(idx)
                points[idx]['touched'] = True

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            msg = "Correct!" if pattern == PASSWORD else "Wrong!"

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
