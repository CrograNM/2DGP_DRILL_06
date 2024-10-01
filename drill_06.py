# 2021184033 조성욱
from pico2d import *

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

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

playing = True
running = False
isLeft = False
x = 800 // 2
y = 90
dx = 0
dy = 0
frame = 0

# fill here
while playing:

        # 버퍼 비우기
        clear_canvas()
        # 버퍼 채우기 : 배경
        ground.draw(400, 300, 800, 600)
        # 버퍼 채우기 : 캐릭터
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        frame = (frame + 1) % 8
        # character.clip_composite_draw(frame * 38, 80, 38, 80, 0, 'h', x, y, 38, 80)

        # 좌표 이동

        # 버퍼에 따라 그리기 및 이벤트 입력
        update_canvas()
        handle_events() # 종료 확인용
        delay(0.05)

close_canvas()

