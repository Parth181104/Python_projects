# from tkinter import *
# import pyspeedtest


# def speedcheck():
#     sp = pyspeedtest.SpeedTest()
#     sp.get_servers()
#     down = str(round(sp.download()/(10**6),3)) + "Mbps"
#     up = str(round(sp.upload()/(10**6),3)) + "Mbps"
#     lab_down.config(text=down)
#     lab_up.config(text=up)



# sp = Tk()
# sp.title("INTERNET SPEED TEST")
# sp.geometry("500x700")
# sp.config(bg='cyan')

# lab = Label(sp,text="INTERNET SPEED TEST",font=('Times New Roman',20,"bold"))
# lab.place(x=60,y=40,height=50,width=380)

# lab = Label(sp,text="DOWNLOAD SPEED",font=('Times New Roman',30,"bold"))
# lab.place(x=60,y=110,height=50,width=380)

# lab_down = Label(sp,text="00",font=('Times New Roman',30,"bold"))
# lab_down.place(x=60,y=180,height=50,width=380)

# lab = Label(sp,text="UPLOAD SPEED",font=('Times New Roman',30,"bold"))
# lab.place(x=60,y=290,height=50,width=380)

# lab_up = Label(sp,text="00",font=('Times New Roman',30,"bold"))
# lab_up.place(x=60,y=360,height=50,width=380)


# button = Button(sp,text='CHECK SPEED',font=("Times New Roman",30,"bold"),relief=RAISED,bg='red')
# button.place(x=60,y=450,height=50,width=380)

# speedcheck()

# sp.mainloop()

from tkinter import *
import pyspeedtest

def speedcheck():
    sp = pyspeedtest
    sp.get_servers()  # This selects the best server based on ping
    down = str(round(sp.download()/(10**6), 3)) + " Mbps"
    up = str(round(sp.upload()/(10**6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("INTERNET SPEED TEST")
sp.geometry("500x700")
sp.config(bg='cyan')

label1 = Label(sp, text="INTERNET SPEED TEST", font=('Times New Roman', 20, "bold"))
label1.place(x=60, y=40, height=50, width=380)

label2 = Label(sp, text="DOWNLOAD SPEED", font=('Times New Roman', 30, "bold"))
label2.place(x=60, y=110, height=50, width=380)

lab_down = Label(sp, text="00", font=('Times New Roman', 30, "bold"))
lab_down.place(x=60, y=180, height=50, width=380)

label3 = Label(sp, text="UPLOAD SPEED", font=('Times New Roman', 30, "bold"))
label3.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=('Times New Roman', 30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text='CHECK SPEED', font=("Times New Roman", 30, "bold"), relief=RAISED, bg='red', command=speedcheck)
button.place(x=60, y=450, height=50, width=380)

sp.mainloop()
