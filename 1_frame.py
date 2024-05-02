import pygame

# 초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 게임 루프
running = True  # 게임이 실행중인지 여부
while running:
    # 이벤트 루프
    for event in pygame.event.get():  # 이벤트 발생
        if event.type == pygame.QUIT:  # 0창이 닫히는 이벤트인 경우
            running = False  # 게임이 더 이상 실행되지 않음

# 게임 종료
pygame.quit()
