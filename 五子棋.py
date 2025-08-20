import pygame as pg
import time

def check_win(board, i, j):
    player = board[i][j]
    count_horizontal = 0
    offset = 1
    while j+offset < len(board[0]) and board[i][j+offset] == player:
        count_horizontal = count_horizontal + 1
        offset = offset + 1
    offset = 1
    while j-offset >= 0 and board[i][j-offset] == player:
        count_horizontal = count_horizontal + 1
        offset = offset + 1
    if count_horizontal == 4:
        return True

    count_vertical = 0
    offset = 1
    while i+offset < len(board) and board[i+offset][j] == player:
        count_vertical = count_vertical + 1
        offset = offset + 1
    offset = 1
    while i-offset >= 0 and board[i-offset][j] == player:
        count_vertical = count_vertical + 1
        offset = offset + 1

    if count_vertical == 4:
        return True

    count_ul2lr = 0
    offset = 1
    while i+offset < len(board) and j+offset < len(board[0]) and board[i+offset][j+offset] == player:
        count_ul2lr = count_ul2lr + 1
        offset = offset + 1

    offset = 1
    while i-offset >=0 and j-offset >=0 and board[i-offset][j-offset] == player:
        count_ul2lr = count_ul2lr + 1
        offset = offset + 1

    if count_ul2lr == 4:
        return True

    count_ur2ll = 0
    offset = 1
    while i+offset < len(board) and j-offset >=0 and board[i+offset][j-offset] == player:
        count_ur2ll = count_ur2ll + 1
        offset = offset + 1

    offset = 1
    while i-offset >=0 and j+offset < len(board[0]) and board[i-offset][j+offset] == player:
        count_ur2ll = count_ur2ll + 1
        offset = offset + 1

    if count_ur2ll == 4:
        return True

    return False


#pygame初始化
pg.init()
font = pg.font.Font(None, 200)  # Use default font, size 50

#設定視窗
width, height = 800, 800
screen = pg.display.set_mode((width, height))
pg.display.set_caption("五子棋")

#建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((199, 167, 82))
for i in range(15):
    pg.draw.line(bg, (100, 100, 100),(50, 50+50*i), (750, 50+50*i), 2)
for i in range(15):
    pg.draw.line(bg, (100, 100, 100), (50+50*i, 50), (50+50*i, 750), 2)
screen.blit(bg, (0,0))
pg.display.update()

board = [[-1] * 15 for _ in range(15)]
PLAYER_1 = 0
PLAYER_1_COLOR = (50, 50, 50)
PLAYER_2 = 1
PLAYER_2_COLOR = (150, 150, 150)

running = True
game_round = 0
while running:
    ev = pg.event.get()
    for event in ev:
        if event.type == pg.MOUSEBUTTONUP:
            x, y = pg.mouse.get_pos()
            x_inter = round(x / 50.0)
            y_inter = round(y / 50.0)
            print(x, y, x_inter, y_inter)
            pos_i, pos_j = y_inter-1, x_inter-1
            if board[pos_i][pos_j] == -1:
                if game_round % 2 == 0:
                    player = PLAYER_1
                else:
                    player = PLAYER_2
                board[pos_i][pos_j] = player
                if 1 <= x_inter <= 15 and 1 <= y_inter <= 15:
                    # right pos
                    if game_round % 2 == 0:
                        color = PLAYER_1_COLOR
                    else:
                        color = PLAYER_2_COLOR
                    pg.draw.circle(bg, color, (x_inter*50, y_inter*50), 20, 0)
                    screen.blit(bg, (0, 0))
                    pg.display.update()
                    if check_win(board, pos_i, pos_j):
                        print("!!!")
                        text_surface = font.render("K.O.", True, (255, 0, 0))  # White text, anti-aliased
                        screen.blit(text_surface, (300, 300))
                        pg.display.update()
                        time.sleep(3)
                        running = False

                    game_round = game_round + 1

        if event.type == pg.QUIT:
            running = False

pg.quit()