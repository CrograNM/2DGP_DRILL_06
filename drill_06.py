# 2021184033 조성욱
from pico2d import *
import random
import math

def handle_events():
    global playing
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            playing = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                playing = False

def buffer_draw():
    global frame
    # 버퍼 비우기
    clear_canvas()
    # 버퍼 채우기 : 배경, 화살표, 캐릭터 순서
    ground.draw(400, 300, 800, 600)
    arrow.clip_draw(0, 0, 50, 50, arrow_x, arrow_y)
    # 캐릭터는 화살표를 바라보며 이동
    if arrow_x > boy_x :
        character.clip_draw(frame * 100, 100, 100, 100, boy_x, boy_y)
    else :
        character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', boy_x, boy_y, 100, 100)
    frame = (frame + 1) % 8
    # 버퍼에 따라 그리기
    update_canvas()

def move_line():
    global boy_x, boy_y, arrow_x, arrow_y, frame
    x1, y1 = boy_x, boy_y
    x2, y2 = arrow_x, arrow_y

    t = 0
    speed = 0.1  # t의 변화 속도 (거리에 따라 조정 가능)
    while t <= 1:
        # t 값을 변화시키면서 boy_x와 boy_y를 갱신
        boy_x = (1 - t) * x1 + t * x2
        boy_y = (1 - t) * y1 + t * y2
        buffer_draw()
        handle_events()  # 종료 확인용
        if playing == False: break

        # 거리에 따라 속도를 조절한다 -> 거리가 멀수록 속도가 큼
        distance = math.sqrt((x2 - boy_x) ** 2 + (y2 - boy_y) ** 2)
        speed = 0.01 + distance / 10000
        if speed > 0.03 : speed = 0.03    # 최대 속도 조절
        t += speed

        delay(0.05)

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

playing = True
isLeft = False

boy_x = 800 // 2
boy_y = 600 // 2
arrow_x = random.randrange(0, 800)
arrow_y = random.randrange(0, 600)
frame = 0

while playing:
    move_line()
    arrow_x = random.randrange(0, 800)
    arrow_y = random.randrange(0, 600)

close_canvas()
