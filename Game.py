import tkinter as tk
import enviroment as ev
import acter as ac
import policy as po
import time 

p = 0 #position
n = 6 #map_mas_nuber
sx = 50 #left_up x point 
sy = 50 #left_up y point 
fx = 600 + sx #right_down x point
fy = 600 + sy #right_down y point
h = int((fx - sx)/n) #mass heigth
w = int((fy - sy)/n) #mass weigth

#canvase
root = tk.Tk()
canvas = tk.Canvas(root, bg = "white")
#text
t = tk.Text(canvas,height=1, width=10,font=('Times New Roman', 40, 'bold'))
tn = tk.Text(canvas,height=1, width=5,font=('Times New Roman', 40, 'bold'))
#map 
#n*nの1次元行列
#左上 0  (6*6の場合)
# 0  1  2  3  4  5
# 6  7  8  9 10 11
#・・・
#30 31 32 33 34 35
#35 がゴール
#[0,0,0,0] 左　右　下　右
map = ev.map_create(n)

#actor
a = ac.actor()

#window size
size_x = 700
size_y = 900

#finish times
finish_times = 0

def window():
    # ----------- ①Window作成 ----------- #
    root.title('MAP')   # 画面タイトル設定
    root.geometry('700x900')       # 画面サイズ設定
    root.resizable(False, False)   # リサイズ不可に設定
    # Canvasの作成
    # Canvasを配置
    canvas.pack(fill = tk.BOTH, expand = True)

    # 矩形の描画
    sq1 = canvas.create_rectangle(sx,sy,fx,fy, fill="white",width = 3, tag="rect")
    # 線の描画
    lh = []
    lw = []
    #make line 
    for i in range(n):
        for j in range(n):
            slh = "lh" + str(j) + str(i)
            slw = "lw" + str(j) + str(i)
            canvas.create_line(sx+w*(i+1), sy+h*j,sx+w*(i+1), sy+h*(j+1) ,fill="black", width = 3, tag=slh)
            canvas.create_line(sx+w*i, sy+h*(j+1),sx+w*(i+1), sy+h*(j+1) ,fill="black", width = 3, tag=slw)
    
    #make acter cercle
    canvas.create_oval(sx+w/4, sy+h/4, sx+3*w/4, sy+3*h/4, fill="red",tags='act')
    #make button
    button1=tk.Button(canvas,text="左",width=10,height=3,command=move_left)
    button1.place(x = size_x/2-300, y = 3*size_y/4)
    button2=tk.Button(canvas,text="右",width=10,height=3,command=move_right)
    button2.place(x = size_x/2-150, y = 3*size_y/4)
    button3=tk.Button(canvas,text="下",width=10,height=3,command=move_down)
    button3.place(x = size_x/2, y = 3*size_y/4)
    button4=tk.Button(canvas,text="上",width=10,height=3,command=move_up)
    button4.place(x = size_x/2+150, y = 3*size_y/4)

def finish():
    #last mass
    if a.position() == n*n-1:
        #text
        t.delete("1.0", "end")
        t.insert(1.0,'Finish')
        #actor delete
        canvas.delete('act')

        #resume
        #a.resume(canvas,sx,sy,w,h)
        
        #stop
        a.stop()

def move_up():
    a.move_up(canvas,map,n,h,t)
    finish()

def move_down():
    a.move_down(canvas,map,n,h,t)
    finish()

def move_right():
    a.move_right(canvas,map,w,t)
    finish()

def move_left():
    a.move_left(canvas,map,w,t)
    finish()


def make(map):
    #ev.map_view(map,n) #view map parameter
    for m in range(len(map)):
        #print(m)
        #empty root
        if map[m][1] != 1:
            #print(m,"lh"+str(int(m/(n)))+str(m%(n))) #empty road
            canvas.itemconfig("lh"+str(int(m/(n)))+str(m%(n)), fill="white")
        if map[m][2] != 1:
            #print(m,"lw"+str(int(m/(n)))+str(m%(n))) #empty road
            canvas.itemconfig("lw"+str(int(m/(n)))+str(m%(n)), fill="white")
            #'''
    #canvas.itemconfig("lh01", fill="white")
    #canvas.itemconfig("lh02", fill="white")
    #canvas.itemconfig("lw01", fill="white")
    #canvas.itemconfig("lw02", fill="white")
    
def move():
    #policy make
    a.poli = po.policy_set(a.poli)
    #move select
    m = po.policy_select(a.poli)
    #text
    tn.delete("1.0", "end")
    tn.insert(1.0,str(a.count) + ' : ' + str(m))
    if m == 0:
        move_up()
    elif m == 1:
        move_down()
    elif m == 2:
        move_right()
    elif m == 3:
        move_left()
    else:
        pass
    #after 100mm next move
    if a.mv == True and a.count <= finish_times:
        canvas.after(100,move)
    else:
        finish()
    
if __name__ == '__main__':
    window()#make filed
    t.place(x = 250,y = 800)#make text box
    tn.place(x = 50,y = 800)#make text box
    tn.insert(1.0,'0 : 0')#text
    make(map) #make road map 
    ev.map_view(map,n)#map 
    canvas.after(100,move)#move start
    root.mainloop()