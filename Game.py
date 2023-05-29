import tkinter as tk


def Environment():
    print('test') 

def window():
    # ----------- ①Window作成 ----------- #
    root.title('tkinterの使い方')   # 画面タイトル設定
    root.geometry('700x900')       # 画面サイズ設定
    root.resizable(False, False)   # リサイズ不可に設定
    # Canvasの作成
    canvas = tk.Canvas(root, bg = "white")
    # Canvasを配置
    canvas.pack(fill = tk.BOTH, expand = True)

    sx = 50
    sy = 50
    fx = 600 + sx
    fy = 600 + sy
    # 矩形の描画
    sq1 = canvas.create_rectangle(sx,sy,fx,fy, fill="white",width = 3, tag="rect")
    n = 6
    h = int((fx - sx)/6)
    w = int((fy - sy)/6)
    # 線の描画
    lh = []
    lw = []
    for i in range(n):
        for j in range(n):
            slh = "lh" + str(i) + str(j)
            slw = "lw" + str(i) + str(j)
            canvas.create_line(sx+w*i, sy+h*j,sx+w*i, sy+h*(j+1) ,fill="black", width = 3, tag=slh)
            canvas.create_line(sx+w*i, sy+h*j,sx+w*(i+1), sy+h*j ,fill="black", width = 3, tag=slw)
    canvas.itemconfig("lh00", fill="white")
if __name__ == '__main__':
    Environment()
    root = tk.Tk()
    window()
    root.mainloop()