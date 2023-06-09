import random as rn

def map_range(map_c,n):
    #[0,0,0,0] 全て空いている
    #[0,0,0,1] 上だけ塞がっている
    #[0,0,1,0] 下だけ塞がっている
    #[0,1,0,0] 右だけ塞がっている
    #[1,0,0,0] 左だけ塞がっている
    #[1,1,1,1] 全て塞がっている
    for m in range(len(map_c)):
        if m < n:
            map_c[m][3] = 1
        elif map_c[m-n][2] == 1:
            map_c[m][3] = 1
        if m % n == 0:
            map_c[m][0] = 1
        elif map_c[m-1][1] == 1:
            map_c[m][0] = 1
        if m % n == n-1:
            map_c[m][1] = 1
        if m >= n*(n-1):
            map_c[m][2] = 1
    return map_c

def map_create(n):
    #0 [0,0,0,0] 右と下は空いている
    #1 [0,0,1,0] 下は塞がっている
    #2 [0,1,0,0] 右は塞がっている
    map_c = []
    map_test = []
    for i in range(n):
        map_part = []
        for j in range(n):
            r = rn.randint(0,3)
            if r == 0 or j == n-1  or i == n-1:
                map_c.append([0,0,0,0])
                map_part.append([0,0,0,0])
            elif r % 2 == 1:
                map_c.append([0,0,1,0])
                map_part.append([0,0,1,0])
            elif r % 2 == 0:
                map_c.append([0,1,0,0])
                map_part.append([0,1,0,0])
        map_test.append(map_part)
    map = map_range(map_c,n)
    return map

def map_view(map,n):
    for m in range(len(map)):
        if m % n == 0:
            print('')
        print(map[m],end='')
    print('')