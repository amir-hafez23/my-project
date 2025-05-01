import pygame
import arabic_reshaper
from bidi.algorithm import get_display
import sys
import math
import random

pygame.init()

# تنظیمات پنجره
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("جشن پایان سال تحصیلی")

# رنگ پس‌زمینه
BACKGROUND_COLOR = (10, 10, 40)

# بارگذاری فونت فارسی (مطمئن شو Vazir.ttf کنار فایل هست)
try:
    font = pygame.font.Font("Vazir.ttf", 36)
except:
    print("❗ فونت Vazir.ttf پیدا نشد. لطفاً آن را کنار فایل پایتون قرار دهید.")
    sys.exit()

# لیست پیام‌ها
messages = [
    "🎓 جشن پایان سال تحصیلی مبارک!",
    "🌟 تبریک به دانش‌آموزان ممتاز 🌟",
    "📚 شما باعث افتخار مدرسه هستید!",
    "🙏 از حضور گرم والدین گرامی سپاس‌گزاریم",
    "💐 از زحمات معلمان عزیز قدردانی می‌کنیم",
    "🎤 شعر جشن:",
    "«علم چون نوری بتابد در دل پاک شما\nمی‌شود روشن مسیر زندگی از پرتو آن»",
    "✨ با آرزوی موفقیت روزافزون برای همه شما ✨",
]

# تابع آماده‌سازی متن فارسی
def render_text(text, color):
    reshaped = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped)
    lines = bidi_text.split("\n")
    surfaces = [font.render(line, True, color) for line in lines]
    return surfaces

# پارامترهای حلقه‌ی متحرک
angle_offset = 0
segments = 80
radius = 220
line_length = 25
clock = pygame.time.Clock()
msg_index = 0
msg_timer = pygame.time.get_ticks()

running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    center = (WIDTH // 2, HEIGHT // 2)

    # بررسی رویداد خروج
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # رسم حلقه‌ی متحرک
    for i in range(segments):
        angle = math.radians((360 / segments) * i + angle_offset)
        x1 = int(center[0] + radius * math.cos(angle))
        y1 = int(center[1] + radius * math.sin(angle))
        x2 = int(center[0] + (radius + line_length) * math.cos(angle))
        y2 = int(center[1] + (radius + line_length) * math.sin(angle))
        color = pygame.Color(0)
        color.hsva = ((i * 360 / segments + angle_offset) % 360, 100, 100, 100)
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 3)

    # حرکت حلقه
    angle_offset += 1
    if angle_offset >= 360:
        angle_offset = 0

    # تغییر متن هر 3 ثانیه
    if pygame.time.get_ticks() - msg_timer > 3000:
        msg_index = (msg_index + 1) % len(messages)
        msg_timer = pygame.time.get_ticks()

    # نمایش متن در مرکز
    text_surfaces = render_text(messages[msg_index], (255, 255, 255))
    total_height = sum([s.get_height() for s in text_surfaces])
    y_offset = center[1] - total_height // 2
    for surface in text_surfaces:
        rect = surface.get_rect(center=(center[0], y_offset + surface.get_height() // 2))
        screen.blit(surface, rect)
        y_offset += surface.get_height() + 5

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
