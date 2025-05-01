import time
from pyfiglet import Figlet
from termcolor import colored
import random

def display_welcome():
    """نمایش پیام خوش آمدگویی با انیمیشن"""
    f = Figlet(font='slant')
    welcome_text = f.renderText('Welcome Parents!')
    
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    
    for i in range(len(welcome_text.split('\n')[0])):
        colored_text = ''
        for line in welcome_text.split('\n'):
            colored_line = colored(line[:i], random.choice(colors)) + line[i:]
            colored_text += colored_line + '\n'
        print(colored_text)
        time.sleep(0.05)
        print("\033[H\033[J")  # پاک کردن صفحه

def display_congratulations():
    """نمایش پیام تبریک"""
    messages = [
        "تقدیر و تشکر از حضور گرم شما",
        "جشن امروز را با حضور خود نورانی کردید",
        "قدردان حمایت‌های بی‌دریغ شما هستیم",
        "همراهی شما مایه افتخار ماست",
        "با مشارکت شما، مدرسه ما سرزنده‌تر است"
    ]
    
    for msg in messages:
        print(colored("✿✿✿ " + msg + " ✿✿✿", 'light_magenta', attrs=['bold']))
        time.sleep(1.5)

def display_animation():
    """نمایش انیمیشن ساده"""
    symbols = ['🌸', '🎉', '🎈', '🏆', '🎓', '👏']
    for _ in range(10):
        print(' '.join([random.choice(symbols) for _ in range(20)]))
        time.sleep(0.3)
        print("\033[H\033[J")

def main():
    """تابع اصلی برنامه"""
    try:
        display_welcome()
        time.sleep(1)
        
        print(colored("\n" + "="*50, 'yellow'))
        print(colored(" جشن پایان سال تحصیلی ", 'light_cyan', attrs=['bold']))
        print(colored("مدرسه نمونه ایران", 'light_cyan', attrs=['bold']))
        print(colored("="*50 + "\n", 'yellow'))
        
        display_congratulations()
        time.sleep(2)
        
        print("\n")
        display_animation()
        
        print(colored("\nبا آرزوی بهترین‌ها برای شما و فرزندان عزیزتان", 'light_green'))
        print(colored("برنامه‌های جشن آغاز می‌شود...", 'light_blue', attrs=['bold']))
        
    except KeyboardInterrupt:
        print(colored("\nبرنامه خاتمه یافت.", 'red'))

if __name__ == "__main__":
    main()