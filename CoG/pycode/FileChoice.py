import os
from tkinter import Tk
from tkinter import StringVar
from tkinter import LEFT
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

def App():
    # 参照ボタンのイベント
    # button1クリック時の処理
    def button1_clicked():
        fTyp = [("",".csv")]
        iDir = os.path.abspath(os.getcwd())
        filepath = filedialog.askopenfilenames(filetypes = fTyp,initialdir = iDir)
        file1.set(filepath)

    # button2クリック時の処理
    def button2_clicked():
        messagebox.showinfo('FileReference Tool', u'Reference Files ↓↓\n' + file1.get())
        print(file1.get())
    #Exit時の処理
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    # rootの作成
    root = Tk()
    root.title('FileReference Tool')
    root.resizable(False, False)

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 参照ボタンの作成
    button1 = ttk.Button(root, text=u'Reference', command=button1_clicked)
    button1.grid(row=0, column=3)

    # ラベルの作成
    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('ファイル>>')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルパス表示ラベルの作成
    file1 = StringVar()
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=50)
    file1_entry.grid(row=0, column=2)

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=(0,5))
    frame2.grid(row=1)

    # 参照確認の作成
    button2 = ttk.Button(frame2, text='Check', command=button2_clicked)
    button2.pack(side=LEFT)

    # Exitボタンの作成
    button3 = ttk.Button(frame2, text='Exit', command=on_closing)
    button3.pack(side=LEFT)
    #return file1
    
    root.mainloop()

    return eval(file1.get())
