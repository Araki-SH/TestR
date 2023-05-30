def start():
    return 0

    #[0,0,0,0] 全て空いている
    #[0,0,0,1] 上だけ塞がっている
    #[0,0,1,0] 下だけ塞がっている
    #[0,1,0,0] 右だけ塞がっている
    #[1,0,0,0] 左だけ塞がっている
    #[1,1,1,1] 全て塞がっている
def move(n,map,a_m,p):
    #0 上
    #1 下
    #2 右
    #3 左
    if a_m == 0 and a_m >= n and map[p][3] == 0:
        p -= n
    elif a_m == 1 and a_m <= n*(n-1) and map[p][2] == 0:
        p += n
    elif a_m == 2 and a_m % 6 != 5 and map[p][1] == 0:
        p += 1
    elif a_m == 3 and a_m % 6 != 0 and map[p][0] == 0:
        p -= 1
    else:
        print('not move')
    return p
    