import pygame
import sys
import time
# 初始化Pygame
pygame.init()

size = width,height = 1200, 800
speed = [-2, 1]
bg = (255, 255, 255)

clock = pygame.time.Clock()
# 创建指定大小的窗口，建立了事件了，返回surface对象，显示一个黑幕
screen = pygame.display.set_mode(size)
print(screen)
# 设置窗口标题
pygame.display.set_caption('初次见面，清大家多安关照！')

#加载图片 返回surface对象
turtle = pygame.image.load ("turtle.png")

# 获得图像的位置矩形 surface对象有一个矩形位置
position = turtle.get_rect()

while True:
    
    for event in pygame.event.get() :
        print(str(pygame.event.get()) +'1')#事件和事件队列,事件监听机制
        if event.type == pygame.QUIT:
            #time.sleep(100)      #sleep()不同,它会被挂起,会卡死，说明还一个事件处理线程和主程序在并行执行
            pygame.time.delay(10)#delay()是循环等待,该进程还在运行,占用处理器
            pygame.quit()
            sys.exit()
            
    #移动图像

    position = position.move(speed)
    
    if position.left < 0 or position.right > width:
            
        # 翻转图像
        turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]
    if position.top < 0 or position. bottom > height:
        speed[1]= -speed[1]

    screen.fill(bg)#填充背景
    screen.blit(turtle,position)#更新图像
    pygame.display.flip()#更新界面，为什么没有传入screen参数，应该是set_mode时候记住的
    #pygame.time.delay(10)
    clock.tick(200)
