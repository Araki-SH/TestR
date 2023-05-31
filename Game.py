import tkinter as tk
import enviroment as ev
import acter as ac

p = 0
n = 3
sx = 50
sy = 50
fx = 600 + sx
fy = 600 + sy
h = int((fx - sx)/n)
w = int((fy - sy)/n)

root = tk.Tk()
canvas = tk.Canvas(root, bg = "white")
t = tk.Text(canvas,height=1, width=10,font=('Times New Roman', 40, 'bold'))
map = ev.map_create(n)
a = ac.actor()
size_x = 700
size_y = 900

def window():
    # ----------- ①Window作成 ----------- #
    root.title('tkinterの使い方')   # 画面タイトル設定
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
    for i in range(n):
        for j in range(n):
            slh = "lh" + str(j) + str(i)
            slw = "lw" + str(j) + str(i)
            canvas.create_line(sx+w*(i+1), sy+h*j,sx+w*(i+1), sy+h*(j+1) ,fill="black", width = 3, tag=slh)
            canvas.create_line(sx+w*i, sy+h*(j+1),sx+w*(i+1), sy+h*(j+1) ,fill="black", width = 3, tag=slw)
    
    canvas.create_oval(sx+w/4, sy+h/4, sx+3*w/4, sy+3*h/4, fill="red",tags='act')
    button1=tk.Button(canvas,text="左",width=10,height=3,command=move_left)
    button1.place(x = size_x/2-300, y = 3*size_y/4)
    button2=tk.Button(canvas,text="右",width=10,height=3,command=move_right)
    button2.place(x = size_x/2-150, y = 3*size_y/4)
    button3=tk.Button(canvas,text="下",width=10,height=3,command=move_down)
    button3.place(x = size_x/2, y = 3*size_y/4)
    button4=tk.Button(canvas,text="上",width=10,height=3,command=move_up)
    button4.place(x = size_x/2+150, y = 3*size_y/4)

def finish():
    if a.position() == n*n-1:
        t.get("1.0", "end")
        t.insert(1.0,'Finish')
        canvas.delete('act')
        canvas.create_oval(sx+w/4, sy+h/4, sx+3*w/4, sy+3*h/4, fill="red",tags='act')
        a.restart()

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
    ev.map_view(map,n)
    for m in range(len(map)):
        #print(m)
        if map[m][1] != 1:
            #print(m,"lh"+str(int(m/(n)))+str(m%(n)))
            canvas.itemconfig("lh"+str(int(m/(n)))+str(m%(n)), fill="white")
        if map[m][2] != 1:
            #print(m,"lw"+str(int(m/(n)))+str(m%(n)))
            canvas.itemconfig("lw"+str(int(m/(n)))+str(m%(n)), fill="white")
            #'''
    #canvas.itemconfig("lh01", fill="white")
    #canvas.itemconfig("lh02", fill="white")
    #canvas.itemconfig("lw01", fill="white")
    #canvas.itemconfig("lw02", fill="white")
    
if __name__ == '__main__':
    window()
    t.place(x = 250,y = 800)
    make(map)
    root.mainloop()