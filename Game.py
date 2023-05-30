import tkinter as tk
import enviroment as ev

n = 6
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

    sx = 50
    sy = 50
    fx = 600 + sx
    fy = 600 + sy
    # 矩形の描画
    sq1 = canvas.create_rectangle(sx,sy,fx,fy, fill="white",width = 3, tag="rect")
    h = int((fx - sx)/6)
    w = int((fy - sy)/6)
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

def change_field():
    map = ev.map_create(n)
    ev.map_view(map)
    for m in range(len(map)):
        print(m)
        if map[m][1] != 1:
            print(m,"lh"+str(int(m/(n)))+str(m%(n)))
            canvas.itemconfig("lh"+str(int(m/(n)))+str(m%(n)), fill="white")
        if map[m][2] != 1:
            print(m,"lw"+str(int(m/(n)))+str(m%(n)))
            canvas.itemconfig("lw"+str(int(m/(n)))+str(m%(n)), fill="white")
            #'''
    #canvas.itemconfig("lh01", fill="white")
    #canvas.itemconfig("lh02", fill="white")
    #canvas.itemconfig("lw01", fill="white")
    #canvas.itemconfig("lw02", fill="white")
    
if __name__ == '__main__':
    window()
    change_field()
    root.mainloop()