# 2021184033 조성욱
from pico2d import *
import random


def handle_events():
    global playing
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            playing = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                playing = False
    pass
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
    # 두개의 점만 그리기
    global boy_x, boy_y, arrow_x, arrow_y, frame
    x1, y1 = boy_x, boy_y
    x2, y2 = arrow_x, arrow_y

    for i in range(0, 100):
        t = i / 100

        boy_x = (1-t)*x1 + t*x2
        boy_y = (1-t)*y1 + t*y2
        buffer_draw()
        handle_events()  # 종료 확인용
        if playing == False: break
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

move_line()
while playing:
        buffer_draw()
        handle_events()  # 종료 확인용
        delay(0.05)

close_canvas()

