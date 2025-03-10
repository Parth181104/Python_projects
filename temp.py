from tkinter import *
from tkinter import ttk
import requests

def data_get():

    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f15e8a510bc118908f136861d6b8eef1").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pre_label1.config(text=data["main"]["pressure"])



win = Tk()
win.title("JUMBO")
win.config(bg="cyan")
win.geometry('500x550')

name_label = Label(win,text="JUMBO Weather App",font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="JUMBO Weather App",values=list_name,font=("Times New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)





w_label = Label(win,text="Weather Climate ",font=("Times New Roman",20))
w_label.place(x=25,y=260,height=50,width=200)

w_label1 = Label(win,text="",font=("Times New Roman",20))
w_label1.place(x=250,y=260,height=50,width=200)

wb_label = Label(win,text="Weather Description ",font=("Times New Roman",17))
wb_label.place(x=25,y=330,height=50,width=200)

wb_label1 = Label(win,text="",font=("Times New Roman",17))
wb_label1.place(x=250,y=330,height=50,width=200)


temp_label = Label(win,text="Temperature ",font=("Times New Roman",20))
temp_label.place(x=25,y=400,height=50,width=200)

temp_label1 = Label(win,text="",font=("Times New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=200)

pre_label = Label(win,text="Pressure ",font=("Times New Roman",20))
pre_label.place(x=25,y=470,height=50,width=200)


pre_label1 = Label(win,text="",font=("Times New Roman",20))
pre_label1.place(x=250,y=470,height=50,width=200)

done_button = Button(win,text="DONE",font=("Times New Roman",20,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()