class actor:
    def __init__(self):
        self.posi = 0 #position
        self.mv = True #can move
        self.poli = [0,0,0,0] #policy 左　右　下　上
        self.count = 0 #step count

    #return position
    def position(self):
        return self.posi

    def position_change(self,m):
        self.posi += m

    def count_up(self):
        self.count += 1
    
    def move_up(self,canvas,map,n,h,t):
        t.delete("1.0", "end")
        if map[self.posi][3] != 1 and self.mv == True:
            self.position_change(-n)
            canvas.move("act",0, -h)
            t.insert(1.0,'move up')
        else:
            t.insert(1.0,'do not move')
        self.count_up()

    def move_down(self,canvas,map,n,h,t):
        t.delete("1.0", "end")
        if map[self.posi][2] != 1 and self.mv == True:
            self.position_change(n)
            canvas.move("act",0, h)
            t.insert(1.0,'move down')
        else:
            t.insert(1.0,'do not move')
        self.count_up()

    def move_right(self,canvas,map,w,t):
        t.delete("1.0", "end")
        if map[self.posi][1] != 1 and self.mv == True:
            self.position_change(1)
            canvas.move("act",w, 0)
            t.insert(1.0,'move right')
        else:
            t.insert(1.0,'do not move')
        self.count_up()

    def move_left(self,canvas,map,w,t):
        t.delete("1.0", "end")
        if map[self.posi][0] != 1 and self.mv == True:
            self.position_change(-1)
            canvas.move("act",-w, 0)
            t.insert(1.0,'move left')
        else:
            t.insert(1.0,'do not move')
        self.count_up()

    #resume 
    def resume(self,canvas,sx,sy,w,h,):
        self.posi = 0
        self.mv = True
        canvas.create_oval(sx+w/4, sy+h/4, sx+3*w/4, sy+3*h/4, fill="red",tags='act')

    #restart
    def restart(self):
        self.mv = True

    #stop
    def stop(self):
        self.mv = False
