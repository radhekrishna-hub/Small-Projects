from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import requests
from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from PIL import Image,ImageTk

root = Tk()
root.title("Sky Cast")
root.geometry("900x500+300+200")
root.resizable(False,False)


#search box
search_img = PhotoImage(file="1781677139963.png")
myimg = Label(image=search_img)
myimg.place(x=20,y=20)


textfield = tk.Entry(root,justify="center",width=17,font=("Poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

# functions
def getweather():
    city = textfield.get().strip()

    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    try:
        geolocator = Nominatim(
            user_agent="skycast_weather_app",
            timeout=20
        )

        location = geolocator.geocode(city)

        if location is None:
            messagebox.showerror("Error", "City not found")
            return

        obj = TimezoneFinder()

        result = obj.timezone_at(
            lng=location.longitude,
            lat=location.latitude
        )

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")

        clock.config(text=current_time)
        name_label.config(text="CURRENT WEATHER")

        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=475d0fddab2cd40e4d77c6e976de1f1d"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        
        
        w.config(text=wind)
        d.config(text=description)
        p.config(text=pressure)
        h.config(text=humidity)





    except Exception as e:
        print(e)
        messagebox.showerror("Error", str(e))


search_icon = PhotoImage(file="1781680260043.png")
myimg_icon = Button(image=search_icon,border=0,cursor="hand2",bg="#404040",command=getweather)
myimg_icon.place(x=400,y=34)

# Logo
# img = Image.open("1781677715044.png")
# img = img.resize((120,120))


logo_img = PhotoImage(file="1781677715044.png")
logo_img = logo_img.subsample(3,3)
logo = Label(root,image=logo_img,width=400)
logo.place(x=500,y=34)

# bottom box
frame_img = PhotoImage(file="1781677151442.png")
frame_myimg = Label(image=frame_img)
frame_myimg.pack(padx=5,pady=5,side=BOTTOM)

# time
name_label = Label(root,font=('arial',15,'bold'))
name_label.place(x=30,y=100)
clock = Label(root,font=("helvetica",20))
clock.place(x=30,y=130)



# labels

label1 = Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x = 120, y = 400)

label2 = Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x = 225, y = 400)

label3 = Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x = 430, y = 400)

label4 = Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x = 650, y = 400)

t=Label(font=("Arial",70,'bold'),fg="#ee666d")
t.place(x=200,y=200)

c= Label(font=("Arial",15,'bold'))
c.place(x=200,y=300)

w=Label(text="...",font=("Arial",20,'bold'),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("Arial",20,'bold'),bg="#1ab5ef")
h.place(x=250,y=430)
d=Label(text="...",font=("Arial",20,'bold'),bg="#1ab5ef")
d.place(x=430,y=430)
p=Label(text="...",font=("Arial",20,'bold'),bg="#1ab5ef")
p.place(x=660,y=430)

root.mainloop()

