from sense_emu import SenseHat, ACTION_PRESSED, ACTION_RELEASED
from signal import pause
from collections import deque
from time import sleep
X = [255, 0, 0]  # temp
D = [0, 0, 255]  # des

W = [0, 255, 0]  # wall
O = [255, 255, 255]  # white, path

S = [255, 147, 7]  # 길

x = 0
y = 0

desy=7
desx=5

aflag=0



map = [
    O, W, O, O, O, O, O, O,
    O, W, O, O, W, O, W, O,
    O, W, O, O, W, O, W, O,
    O, W, O, O, O, O, W, O,
    O, O, O, W, O, O, W, O,
    O, O, O, W, O, W, W, O,
    O, O, O, W, O, O, W, O,
    W, O, W, O, O, D, O, O
]
# 하 우 상 좌 순
dirx = [0, 1, 0, -1]
diry = [1, 0, -1, 0]
visited = [0 for i in range(64)]
pathy = []
pathx = []

sense = SenseHat()
def gtop():  # 표시된 길을 다시 원래 색으로, 매 입력마다 호출
    global S, O, X, D, W
    for idx, i in enumerate(map):
        if i == S:
            map[idx] = O


def mkpth(spathy, spathx):
    global S
    print(spathy,spathx)
    for idx, i in enumerate(spathy):
        dy = i
        dx = spathx[idx]
        print(dy,dx)
        map[(dx) + (dy * 8)] = S
        # sense.set_pixel(dx, dy, S)


def dfs(sy, sx):
    global X, D, W, O, visited, pathy, pathx, aflag
    if aflag == 1:
        return


    for i in range(0, 4):
        dy = sy + diry[i]
        dx = sx + dirx[i]
        print(dy,dx)

        if (dy < 0 or dy > 7 or dx < 0 or dx > 7):
            print ("A",dy,dx)
            continue

        # if(dx + (dy * 8))>63:
        #     continue

        if map[dx + (dy * 8)] == W:
            print("B", dy, dx)
            continue

        # 방문한 곳은 다시 X
        if visited[dx + (dy * 8)] == 1:
            print("C", dy, dx)
            continue

        # Des 찾았다!
        if map[dx + (dy * 8)] == D:
            print("mkp")
            mkpth(pathy, pathx)

            aflag=1
            return
            #visited = [0 for i in range(64)]

        visited[dx + (dy * 8)] = 1

        pathx.append(dx)
        pathy.append(dy)
        dfs(dy, dx)
        pathx.pop()
        pathy.pop()
        visited[dx + (dy * 8)] = 0


def pushed_up():
    gtop()
    global y, x

    if y-1 < 0:
        y = 0
    elif (map[(x) + ((y-1) * 8)] == W):
        print("hi")
    else:
        y -= 1
    dfs(y, x)


def pushed_down():
    gtop()
    global y, x
    # gtop()

    if y+1 > 7:
        y = 7
    elif (map[(x) + ((y+1) * 8)] == W):
        print("hi")
    else:
        y += 1
    dfs(y, x)

def pushed_left():
    global x, y
    gtop()

    if x-1 <0:
        x = 0
    elif map[(x-1) + (y * 8)] == W:
        print("hi")
    else:
        x -= 1
    dfs(y, x)


def pushed_right():
    global x, y
    gtop()

    if x+1 > 7:
        x = 7
    elif map[x+1 + (y * 8)] == W:
        print("hi")
    else:
        x += 1
    dfs(y, x)


def refresh():
    global W, D, X, O, S, map
    # sense.clear()
    sense.set_pixels(map)
    sense.set_pixel(x, y, 255, 0, 0)



while True:
    refresh()
    ori = sense.get_orientation_degrees()
    if (180>=ori["pitch"]>0):
        pushed_up()
    elif(ori["pitch"]<0):
        pushed_down()

    if (180 >= ori["roll"] >0):
        pushed_left()
    elif(ori["roll"] <0):
        pushed_right()

    if(x==desx and y==desy):
        print("success")
        break
    print("a")
    refresh()
    print(map)
    sleep(1)


# sense.stick.direction_up = pushed_up
# sense.stick.direction_down = pushed_down
# sense.stick.direction_left = pushed_left
# sense.stick.direction_right = pushed_right
# sense.stick.direction_any = refresh

pause()

