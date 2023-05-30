class actor:

    def __init__(self):
        self.p = 0

    def position(self):
        return self.p

    def position_change(self,m):
        self.p += m

    def move_up(self,canvas,map,n,h):
        if map[self.p][3] != 1:
            self.position_change(-n)
            canvas.move("act",0, -h)
        else:
            print('not move')

    def move_down(self,canvas,map,n,h):
        if map[self.p][2] != 1:
            self.position_change(n)
            canvas.move("act",0, h)
        else:
            print('not move')

    def move_right(self,canvas,map,w):
        if map[self.p][1] != 1:
            self.position_change(1)
            canvas.move("act",w, 0)
        else:
            print('not move')

    def move_left(self,canvas,map,w):
        if map[self.p][0] != 1:
            self.position_change(-1)
            canvas.move("act",-w, 0)
        else:
            print('not move')

    def restart(self):
        self.p = 0
