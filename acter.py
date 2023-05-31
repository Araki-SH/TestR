class actor:

    def __init__(self):
        self.p = 0

    def position(self):
        return self.p

    def position_change(self,m):
        self.p += m

    def move_up(self,canvas,map,n,h,t):
        t.get("1.0", "end")
        if map[self.p][3] != 1:
            self.position_change(-n)
            canvas.move("act",0, -h)
            t.insert(1.0,'move up')
        else:
            t.insert(1.0,'do not move')

    def move_down(self,canvas,map,n,h,t):
        t.get("1.0", "end")
        if map[self.p][2] != 1:
            self.position_change(n)
            canvas.move("act",0, h)
            t.insert(1.0,'move down')
        else:
            t.insert(1.0,'do not move')

    def move_right(self,canvas,map,w,t):
        t.get("1.0", "end")
        if map[self.p][1] != 1:
            self.position_change(1)
            canvas.move("act",w, 0)
            t.insert(1.0,'move right')
        else:
            t.insert(1.0,'do not move')

    def move_left(self,canvas,map,w,t):
        t.get("1.0", "end")
        if map[self.p][0] != 1:
            self.position_change(-1)
            canvas.move("act",-w, 0)
            t.insert(1.0,'move left')
        else:
            t.insert(1.0,'do not move')

    def restart(self):
        self.p = 0
