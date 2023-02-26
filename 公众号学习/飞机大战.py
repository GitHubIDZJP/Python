import os
import sys
import time
import pygame

# 屏幕宽度
SCREEN_WIDTH = 500
# 屏幕高度
SCREEN_HEIGHT = 250
# 图片绝对路径
IMG_PATH = os.path.join(os.getcwd(), "img")
# 鼠标按键标识
MOUSE_MOVE = False


class HeroPlane(object):
   def __init__(self):
       super(HeroPlane, self).__init__()
       self.image = pygame.image.load(os.path.join(IMG_PATH, "hero_show_1.png"))
       self.rect = self.image.get_rect()
       self.rect.x = 0  # 飞机x轴位置
       self.rect.y = int(SCREEN_HEIGHT - self.rect.height) / 2  # 飞机y轴位置
       self.is_running = True

       self.bullet_list = pygame.sprite.Group()
       self.last_time = time.time()

   def move_level(self, level):
       # 防止飞机移出屏幕外， 增加判断
       if 0 <= level <= SCREEN_WIDTH - self.rect.width:
           self.rect.x = level
       elif level < 0:
           self.rect.x = 0
       elif level > SCREEN_WIDTH - self.rect.width:
           self.rect.x = SCREEN_WIDTH - self.rect.width

   def move_vertical(self, vertical):
       if 0 <= vertical <= SCREEN_HEIGHT - self.rect.height:
           self.rect.y = vertical
       elif vertical < 0:
           self.rect.y = 0
       elif vertical > SCREEN_HEIGHT - self.rect.height:
           self.rect.y = SCREEN_HEIGHT - self.rect.height


def main():
   pygame.init()
   # 初始化显示模块
   pygame.display.init()
   # 创建窗口
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   # 设置窗口标题
   pygame.display.set_caption("python小demo 飞机大战")
   # 设置窗口icon
   # pygame.display.set_icon(pygame.image.load(os.path.join(IMG_PATH, "icon.png")))

   # 加载背景图片
   background = pygame.image.load(os.path.join(IMG_PATH, "test_bj.png"))
   # 初始化英雄类
   hero = HeroPlane()

   def event_check():
       """
       事件检测，这边做了一个简单的示例
       return:
       """
       global MOUSE_MOVE
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               # 接收到退出事件后退出程序
               pygame.quit()
               sys.exit()
           elif event.type == pygame.MOUSEBUTTONDOWN:
               MOUSE_MOVE = True
           elif event.type == pygame.MOUSEBUTTONUP:
               MOUSE_MOVE = False

       if MOUSE_MOVE:
           x, y = pygame.mouse.get_pos()
           hero.move_level(x)
           hero.move_vertical(y)

   def update_hero():
       screen.blit(hero.image, (hero.rect.x, hero.rect.y))

   while True:
       # 事件检测
       event_check()

       # 将背景图片绘制到窗口上
       screen.blit(background, (0, 0))

       # 更新英雄在屏幕上的位置
       update_hero()

       # 更新屏幕上内容
       pygame.display.update()
       time.sleep(0.02)


if __name__ == "__main__":
   main()