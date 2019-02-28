import os
from parameter import *
# 将地图字符串转化为列表
map_list = []
res = MAP.split("\n")
for item in res:
    if item != "":
        item = list(item)
        map_list.append(item)
# 打印地图
for i in range(MAP_HEIGUT):
    for j in range(MAP_WIDTH):
        print(map_list[i][j], end="")
    print("")
#调用参数
x = X
y = Y
exit_x = EXIT_X
exit_y = EXIT_Y

while x != exit_x or y != exit_y:
    ch = input("请输入行走的方向(quit:是退出)：")
    #行走d方向
    if (ch == "d"):
        if map_list[y][x+1] != "#":
            map_list[y][x] = " "
            x += 1
            map_list[y][x] = "O"
        os.system("clear")
        for i in range(MAP_HEIGUT):
            for j in range(MAP_WIDTH):
                print(map_list[i][j], end="")
            print("")
        continue

    #行走s方向
    elif (ch == "s"):
        if map_list[y+1][x] != "#":
            map_list[y][x] = " "
            y += 1
            map_list[y][x] = "O"
        os.system("clear")
        for i in range(MAP_HEIGUT):
            for j in range(MAP_WIDTH):
                print(map_list[i][j], end="")
            print("")
        continue

    #行走a方向
    elif (ch == "a"):
        if map_list[y][x-1] != "#":
            map_list[y][x] = " "
            x -= 1
            map_list[y][x] = "O"
        os.system("clear")
        for i in range(MAP_HEIGUT):
            for j in range(MAP_WIDTH):
                print(map_list[i][j], end="")
            print("")
        continue

    #行走w方向
    elif (ch == "w"):
        if map_list[y-1][x] != "#":
            map_list[y][x] = " "
            y -= 1
            map_list[y][x] = "O"
        os.system("clear")
        for i in range(MAP_HEIGUT):
            for j in range(MAP_WIDTH):
                print(map_list[i][j], end="")
            print("")
        continue

    elif (ch == "quit"):
        print("游戏退出。")
        break

    else:
        print("输入错误!")

if x == exit_x and y == exit_y:
    print("恭喜你已经脱出迷宫。")