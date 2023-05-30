import tkinter as tk
import enviroment as ev

n = 6
sx = 50
sy = 50
fx = 600 + sx
fy = 600 + sy
h = int((fx - sx)/6)
w = int((fy - sy)/6)

root = tk.Tk()
canvas = tk.Canvas(root, bg = "white")

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
    canvas2 = tk.Canvas(root, bg = "white")
    button1=tk.Button(canvas2,text="左")
    button1.pack(side=tk.BOTTOM)
    button2=tk.Button(canvas2,text="右")
    button2.pack(side=tk.BOTTOM)
    button3=tk.Button(canvas2,text="下")
    button3.pack(side=tk.BOTTOM)
    button4=tk.Button(canvas2,text="上")
    button4.pack(side=tk.BOTTOM)
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
def start():
    return 0
def move(map):
    p = start()
    pre = p
    m = int(input())
    #0 上
    #1 下
    #2 右
    #3 左
    if m == 0  and map[p][3] == 0:
        p -= n
        canvas.move("act",0, -h)
    elif m == 1  and map[p][2] == 0:
        p += n
        canvas.move("act",0, h)
    elif m == 2  and map[p][1] == 0:
        p += 1
        canvas.move("act",-w, 0)
    elif m == 3  and map[p][0] == 0:
        p -= 1
        canvas.move("act", w, 0)
    else:
        print('not move')
    return p
    

if __name__ == '__main__':
    window()
    map = ev.map_create(n)
    make(map)
    move(map)
    root.mainloop()